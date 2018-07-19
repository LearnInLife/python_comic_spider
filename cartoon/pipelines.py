# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from cartoon import settings
import requests
import os
import random


class CartoonPipeline(object):
    def process_item(self, item, spider):
        if 'img_url' in item:
            images = []
            # 按章节保存文件夹
            dir_path = os.path.join(settings.IMAGE_STORE, item['dir_name'])
            # 文件夹不存在则创建文件夹
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            # 获取每一个图片链接
            for img_url in item['img_url']:
                # 解析链接，获取第几页
                page = item['link_url'].split('/')[-1].split('.')[0]
                # 扩展名
                type = img_url.split('/')[-1].split('.')[-1]
                # 图片名称
                img_file_name = '第' + page + '页.' + type
                # 图片保存路径
                file_path = os.path.join(dir_path, img_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                # 保存图片
                with open(file_path, 'wb') as f:
                    # 代理ip
                    proxy = random.choice(settings.PROXIES)['ip_port']
                    proxies = {
                        'http': 'http://' + proxy
                    }
                    # user-agent
                    head = {
                        'User-Agent': random.choice(settings.USER_AGENTS)
                    }
                    response = requests.get(url=img_url, proxies=proxies, headers=head)
                    for blok in response.iter_content(1024):
                        if not blok:
                            break

                        f.write(blok)

            item['image_paths'] = images
        return item
