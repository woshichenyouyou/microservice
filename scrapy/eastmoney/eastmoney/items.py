# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastmoneyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stock_id = scrapy.Field()
    stock_names = scrapy.Field()
    TotalScore = scrapy.Field()
    TotalScoreCHG = scrapy.Field()
    LeadPre = scrapy.Field()
    RisePro = scrapy.Field()
    MsgCount = scrapy.Field()
    CapitalScore = scrapy.Field()
    D1 = scrapy.Field()
    ValueScore = scrapy.Field()
    MarketScoreCHG = scrapy.Field()
    Status = scrapy.Field()
    Comment = scrapy.Field()
    UpdateTime = scrapy.Field()
    pass
