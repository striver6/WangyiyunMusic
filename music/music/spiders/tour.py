# -*- coding: utf-8 -*-
import scrapy


class TourSpider(scrapy.Spider):
    name = 'tour'
    allowed_domains = ['https://www.booking.com/index.zh-cn.html?aid=1443406;sid=2c6f7a82e512aa30ba13443cc116f6af;keep_landing=1']
    start_urls = ['http://https://www.booking.com/index.zh-cn.html?aid=1443406;sid=2c6f7a82e512aa30ba13443cc116f6af;keep_landing=1/']

    def parse(self, response):
        pass
