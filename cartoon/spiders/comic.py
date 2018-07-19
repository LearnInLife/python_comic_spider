# -*- coding: utf-8 -*-
import scrapy
from cartoon.items import CartoonItem
import re


class ComicSpider(scrapy.Spider):
    name = 'comic'
    allowed_domains = ['comic.kukudm.com']
    start_urls = ['http://comic.kukudm.com/comiclist/1042/']
    # 图片链接server域名
    server_img = 'http://n5.1whour.com/'
    pattern_img = re.compile(r'\+"(.+)\'><span')

    def parse(self, response):
        # 章节的链接地址数组
        urls = response.xpath(".//tr//dl[@id='comiclistn']/dd/a[2]/@href").extract()
        # 章节的名称数组
        dir_names = response.xpath(".//tr//dl[@id='comiclistn']/dd/a[1]/text()").extract()

        # 保存章节的链接和名称，并发送请求，传递item参数
        for index in range(len(urls)):
            item = CartoonItem()
            item['link_url'] = urls[index]
            item['dir_name'] = dir_names[index]
            yield scrapy.Request(url=item['link_url'], meta={'item': item}, callback=self.parsecartoon)

    def parsecartoon(self, response):
        # 接收传递的item
        item = response.meta['item']
        # 获取章节的第一页的链接
        item['link_url'] = response.url
        # 获取该章节第一页的图片链接
        # 此图片是通过script创建的，所以先获取script文本，然后通过正则找到图片的链接
        script_text = response.xpath(".//script/text()").extract()[0]
        # 注意这里返回的图片地址,应该为列表,否则会报错
        # script_text = 'document.write("<IMG srC='"+m201001d+"kuku8comic8/201103/20110322/诚如神之所说
        # /Comic.kukudm.com_001055.jpg'><span style='display:none'><img src='"+m201001d+"kuku8comic8
        # /201103/20110322/诚如神之所说/Comic.kukudm.com_002054.jpg'></span>");'
        img_url = [self.server_img + re.findall(self.pattern_img, script_text)[0]]
        # 保存图片链接
        item['img_url'] = img_url

        yield item

        # 获取章节的页数
        page_num = response.xpath('.//td[@valign="top"]/text()').re(u'共(\d+)页')[0]
        # 根据页数，整理出本章节其他页码的链接
        p_link = item['link_url'][:-5]

        # 从第二页开始
        for page in range(2, int(page_num) + 1):
            page_link = p_link + str(page) + '.htm'
            # 根据本章节其他页码的链接发送Request请求，用于解析其他页码的图片链接，并传递item
            yield scrapy.Request(url=page_link, meta={'item': item}, callback=self.parseother)

    def parseother(self, response):
        item = response.meta['item']
        # 获取该页面的链接
        item['link_url'] = response.url
        # 此图片是通过script创建的，所以先获取script文本，然后通过正则找到图片的链接
        script_text = response.xpath(".//script/text()").extract()[0]
        # 注意这里返回的图片地址,应该为列表,否则会报错
        # script_text = 'document.write("<IMG srC='"+m201001d+"kuku8comic8/201103/20110322/诚如神之所说
        # /Comic.kukudm.com_001055.jpg'><span style='display:none'><img src='"+m201001d+"kuku8comic8
        # /201103/20110322/诚如神之所说/Comic.kukudm.com_002054.jpg'></span>");'
        img_url = [self.server_img + re.findall(self.pattern_img, script_text)[0]]
        # 保存图片链接
        item['img_url'] = img_url
        # 返回item，交给item pipeline下载图片
        yield item
