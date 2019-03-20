# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,Request
import json

from MusicMenu.items import MusicmenuItem


class MenuSpider(scrapy.Spider):
    name = 'menu'
    allowed_domains = ['localhost:3000']
    start_urls = ['http://localhost:3000/']
    allplaylist_url = 'http://localhost:3000/top/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit=20&offset={offset}'

    def start_requests(self):
        for i in range(0, 66):
            yield Request(self.allplaylist_url.format(offset=i * 20), callback=self.parse_allplaylist)

        # yield Request(self.comment_url.format(offset=self.num_comment), callback=self.parse_comment,dont_filter=True)
        # yield Request(self.playlist_url, callback=self.parse_playlist)

    def parse_allplaylist(self, response):
        result = json.loads(response.text)
        item = MusicmenuItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
                yield item