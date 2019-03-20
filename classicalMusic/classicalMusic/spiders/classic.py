# -*- coding: utf-8 -*-
import scrapy
import logging
import time
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from scrapy import Spider,Request
import json
from classicalMusic.items import ClassicalmusicCommentItem


class ClassicSpider(scrapy.Spider):
    name = 'classic'
    allowed_domains = ['localhost:3000']
    start_urls = ['http://localhost:3000/comment/music?id=346576/']
    comment_url = 'http://localhost:3000/comment/music?id=346576&offset={offset}&limit=20'


    def start_requests(self):
            for i in range(0,1706):
                yield Request(
                    self.comment_url.format(offset=i * 20),
                    callback=self.parse_comment, dont_filter=True)

    def parse_comment(self, response):
        result = json.loads(response.text)
        item = ClassicalmusicCommentItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
                yield item
