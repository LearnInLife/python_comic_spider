# -*- coding: utf-8 -*-

# Scrapy settings for cartoon project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMAGE_STORE = os.path.join(BASE_DIR, 'images')

BOT_NAME = 'cartoon'

SPIDER_MODULES = ['cartoon.spiders']
NEWSPIDER_MODULE = 'cartoon.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'cartoon.middlewares.CartoonSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'cartoon.middlewares.RandomUserAgent': 100,
    'cartoon.middlewares.RandomProxy': 200,
}

USER_AGENTS = [
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
    'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
    'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'
]

PROXIES = [
    {"ip_port": "183.129.207.77:10000", "user_passwd": ""},
    {"ip_port": "121.42.167.160:3128", "user_passwd": ""},
    {"ip_port": "218.241.234.48:8080", "user_passwd": ""},
    {"ip_port": "14.155.112.19:9000", "user_passwd": ""},
    {"ip_port": "120.78.83.223:3128", "user_passwd": ""},
    {"ip_port": "222.186.45.122:62222", "user_passwd": ""},
    {"ip_port": "58.243.50.184:53281", "user_passwd": ""},
    {"ip_port": "114.250.25.19:80", "user_passwd": ""},
    {"ip_port": "112.115.57.20:3128", "user_passwd": ""},
    {"ip_port": "113.116.58.198:9000", "user_passwd": ""},
    {"ip_port": "114.99.255.137:8118", "user_passwd": ""},
    {"ip_port": "113.200.214.164:9999", "user_passwd": ""},
    {"ip_port": "171.37.143.73:9797", "user_passwd": ""},
    {"ip_port": "121.17.80.99:900", "user_passwd": ""},
    {"ip_port": "222.186.45.65:56721", "user_passwd": ""},
    {"ip_port": "124.160.70.155:10988", "user_passwd": ""},
    {"ip_port": "125.45.87.12:9999", "user_passwd": ""},
]

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'cartoon.pipelines.CartoonPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
