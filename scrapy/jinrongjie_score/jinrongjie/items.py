# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JinrongjieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stock_id = scrapy.Field()
    stock_names = scrapy.Field()
    TotalScore = scrapy.Field()
    percent=scrapy.Field()
    pass
