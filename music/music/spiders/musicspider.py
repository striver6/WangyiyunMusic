# -*- coding: utf-8 -*-
import io
import sys

import scrapy

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

from music.items import MusicItem

class MusicspiderSpider(scrapy.Spider):
    name = 'musicspider'
    allowed_domains = ['music.163.com']
    start_urls = ['http://localhost:3000/comment/music?id=186016&offset=0&&limit=20']

    def parse(self, response):

        print(response.text.encode(response.encoding).decode('utf-8'))


