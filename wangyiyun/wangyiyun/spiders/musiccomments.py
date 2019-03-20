# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy import Spider,Request
import io
import sys
import json
import pandas as pd
import pymongo
from wangyiyun.items import WangyiyunCommentItem
from wangyiyun.items import WangyiyunPlaylistItem

from wangyiyun.items import WangyiyunAllPlaylistItem

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

class MusiccommentsSpider(scrapy.Spider):
    name = 'musiccomments'
    allowed_domains = ['localhost:3000']
    start_urls = ['http://localhost:3000/comment/music?id=296883/']
    allplaylist_url = 'http://localhost:3000/top/playlist?order=hot&cat=%E5%85%A8%E9%83%A8&limit=20&offset={offset}'
    playlist_url = 'http://localhost:3000/playlist/detail?id={id}'
    comment_url = 'http://localhost:3000/comment/music?id={id}&offset={offset}&limit=20'
    num_comment = 0
    num_page = 0
    song_id = 0
    results = ''


    def start_requests(self):
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client['music']
        collection = db['menu']
        # 将数据库数据转为dataFrame
        menu = pd.DataFrame(list(collection.find()))
        num = menu['playlists']
        result = pd.DataFrame(num.iloc[0])
        for i in range(1, 66):
            data2 = pd.DataFrame(num.iloc[i])
            result = pd.concat([result, data2], ignore_index=True)
        print(result.shape)
        id = result['id']
        for i in range(0, 1000):
            yield Request(self.playlist_url.format(id=id.iloc[i]), callback=self.parse_playlist)
            ###################################################################
        # client = pymongo.MongoClient(host='localhost', port=27017)
        # db = client['music']
        # collection = db['menu']
        # # 将数据库数据转为dataFrame
        # menu = pd.DataFrame(list(collection.find()))
        # print(menu.shape)
        # id = pd.DataFrame(menu.iloc[:, 1][0])['id']
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print(id.shape)
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # for i in range(1, 10):
        #     id = id.append(pd.DataFrame(menu.iloc[:,1][i])['id'])
        #     #print(id)
        # id = pd.DataFrame(id)
        # print(id.shape)
        # print('#####################')
        # print(id.iloc[0])
        # print('#####################')
        # for i in range(0,200):
        #     yield Request(self.playlist_url.format(id=id.iloc[i,0]), callback=self.parse_playlist)
        #     time.sleep(5)
        #yield Request(self.playlist_url.format(id=2572601660), callback=self.parse_playlist)
        #########################################################

    def parse_playlist(self, response):
        result = json.loads(response.text)
        item = WangyiyunPlaylistItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
                yield item

        for j in range(0, 30):
            for k in range(0,10):
                yield Request(
                    self.comment_url.format(id=result.get('playlist').get('tracks')[j].get('id'), offset=k * 20),
                    callback=self.parse_comment, dont_filter=True)

    def parse_comment(self, response):
        result = json.loads(response.text)
        item = WangyiyunCommentItem()
        #print(response.text.encode('utf-8','ignore'))
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
                yield item

