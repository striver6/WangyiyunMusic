# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class WangyiyunCommentItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comments = Field()

class WangyiyunPlaylistItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    playlist = Field()

class WangyiyunAllPlaylistItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    playlists = Field()
    #name = Field()