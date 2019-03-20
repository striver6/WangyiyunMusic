# -*- coding: utf-8 -*-
import time

import scrapy
import json
from scrapy import Spider, Request

from WangyiyunUser.items import WangyiyunuserItem


class UserSpider(scrapy.Spider):
    name = 'user'
    allowed_domains = ['localhost:3000']
    start_urls = ['http://localhost:3000/']
    user_url = 'http://localhost:3000/user/detail?uid={uid}'
    follows_url = 'http://localhost:3000/user/follows?uid={uid}&offset={offset}&limit={limit}'
    followers_url = 'http://localhost:3000/user/followeds?uid={uid}&offset={offset}&limit={limit}'
    start_uid = '9003'
    follows_next_page=0
    followers_next_page=0


    def start_requests(self):
        yield Request(self.user_url.format(uid=self.start_uid), self.parse_user,dont_filter = True)
        # time.sleep(5)
        yield Request(self.follows_url.format(uid=self.start_uid, limit=30, offset=0),
                      self.parse_follows,dont_filter = True)
        # time.sleep(5)
        yield Request(self.followers_url.format(uid=self.start_uid, limit=30, offset=0),self.parse_followers,dont_filter = True)
        # time.sleep(5)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = WangyiyunuserItem()

        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item
        #print(result.get('profile').get('userId'))

        yield Request(
            self.follows_url.format(uid=result.get('profile').get('userId'), limit=30, offset=0),
            self.parse_follows,dont_filter = True)
        # time.sleep(5)

        yield Request(
            self.followers_url.format(uid=result.get('profile').get('userId'), limit=30, offset=0),
            self.parse_followers,dont_filter = True)
        # time.sleep(5)

    def parse_follows(self, response):
        results = json.loads(response.text)
        print('正在判断关注者')
        if 'follow' in results.keys():
            for result in results.get('follow'):
                yield Request(self.user_url.format(uid=result.get('userId')),
                              self.parse_user,dont_filter = True)
                # time.sleep(5)

        if results.get('more') == True:
            self.follows_next_page = self.follows_next_page+1
            yield Request(self.follows_url.format(uid=self.start_uid, limit=30, offset=self.follows_next_page*30),
                          self.parse_follows,dont_filter = True)
            # time.sleep(5)

    def parse_followers(self, response):
        results = json.loads(response.text)

        if 'followeds' in results.keys():
            for result in results.get('followeds'):
                yield Request(self.user_url.format(uid=result.get('userId')),
                              self.parse_user,dont_filter = True)
                # time.sleep(5)

        if results.get('more') == True:
            self.followers_next_page=self.followers_next_page+1
            yield Request(self.followers_url.format(uid=self.start_uid, limit=30, offset=self.followers_next_page*30),
                          self.parse_followers,dont_filter = True)
            # time.sleep(5)