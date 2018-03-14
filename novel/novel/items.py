# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小说的名字
    name = scrapy.Field()
    #小说的作者
    author = scrapy.Field()
    #小说的地址
    novelurl = scrapy.Field()
    #小说的状态
    novelstatus = scrapy.Field()
    #小说的字数
    novelnumber = scrapy.Field()
    #小说分类
    category = scrapy.Field()
    #小说编号
    name_id = scrapy.Field()
    #小说描述
    des = scrapy.Field()



