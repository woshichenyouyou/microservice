# -*- coding: utf-8 -*-
import os
import sys
import chardet
import scrapy
from stockscrapy.items import StockscrapyItem
from scrapy.http import Request
#from scrapy import optional_features
from commondlib import stockctl
#optional_features.remove('boto')

allstocksdict = stockctl.readallstock(r"../../result/stock_list.csv")   
stock_index=1
def mynexturl():
    global stock_index
    stock_index = stock_index + 1
    print (stock_index)
    print("%d of %d is finished."%(stock_index,len(stockctl.stock_no)))
    nextstockno = stockctl.stock_no[stock_index]
    nextstockname=stockctl.allstockdict[nextstockno]
    print(nextstockno +"," + nextstockname)
    nexturlt="http://doctor.10jqka.com.cn/%s/"%nextstockno
    print(nexturlt)
    return nexturlt
class TonghuashunSpider(scrapy.Spider):
    name = "tonghuashun"
    #rules=(Rule(LinkExtractor(allow=('\d\.shtml')),callback='parse_item',follow=True),)
    allowed_domains = ["tonghuasun.com"]
    start_urls = ('http://doctor.10jqka.com.cn/300770/')
    def parse(self, response):
        try:
#            print("response")
#            print(type(response))
#            print(response)
#            print(response.body.decode(response.encoding))
            item = StockscrapyItem()
            item['score_h']=response.xpath('//span[@class="bignum"]/text()').extract()
            item['score_l']=response.xpath('//span[@class="smallnum"]/text()').extract()
            item['stock_names']=response.xpath('//div[@class="stockname"]/a/text()').extract()
            res = response.xpath('//div[@class="column_3d"]/div[@class="label"]/text()').extract()
            #print(type(res))
            #print(res)
        
            item['score_tech'] = res[0]
            item['score_money'] = res[1]
            item['score_news'] = res[2]
            item['score_industry'] = res[3]
            item['score_basic'] = res[4]
            
            yield item
            newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
        except:
            print("error occur")
            newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
        
        
