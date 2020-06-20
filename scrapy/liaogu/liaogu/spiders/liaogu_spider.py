# -*- coding: utf-8 -*-
import scrapy


class LiaoguSpiderSpider(scrapy.Spider):
    name = 'liaogu_spider'
    allowed_domains = ['https://www.liaogu.com']
    start_urls = ['http://https://www.liaogu.com/']

    def parse(self, response):
        pass
