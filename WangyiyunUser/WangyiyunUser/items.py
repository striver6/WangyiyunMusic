# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class WangyiyunuserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    level = Field()
    listenSongs = Field()
    userPoint = Field()
    mobileSign = Field()
    pcSign = Field()
    profile = Field()
    peopleCanSeeMyPlayRecord = Field()
    bindings = Field()
    adValid = Field()
    code = Field()
    createTime = Field()
    createDays = Field()
