# -*- coding: utf-8 -*-
import scrapy
import os
import re
import json
import sys
import chardet
from scrapy.http import Request
#from scrapy import optional_features
from commondlib import stockctl
from jinrongjie.items import JinrongjieItem

allstocksdict = stockctl.readallstock(r"../../result/stock_list.csv")   
stock_index=0
g_stock_name="hxyh"
g_stock_id="600015"
def mynexturl():
    global stock_index
    global g_stock_name
    global g_stock_id
    stock_index = stock_index + 1
    print (stock_index)
    print("%d of %d is finished."%(stock_index,len(stockctl.stock_no)))
    nextstockno = stockctl.stock_no[stock_index]
    nextstockname=stockctl.allstockdict[nextstockno]
    g_stock_id = nextstockno
    g_stock_name = nextstockname
    print(g_stock_id +"," + g_stock_name)
    nexturlt="http://hqdata.jrj.com.cn/macd/share/%s_n.js?randomNum=0.3885651580058038"%nextstockno
    print(nexturlt)
    return nexturlt
class JinrongjiespiderSpider(scrapy.Spider):
    name = 'jinrongjiespider'
    allowed_domains = ['https://www.jianshu.com/']
    start_urls = ['http://hqdata.jrj.com.cn/macd/share/600015_n.js?randomNum=0.3885651580058038']

    def parse(self, response):
        if response.status == 404:
            print("404 error occur")
            newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
            return
        try:
            print("response from url success")
            print("response type is:")
            print(type(response))
            print("response content is:")
            print(response)
            res = response.body.decode(response.encoding)
            print("After decode response, type is:")
            print(type(res))
            json_str = res.split("=", 1)[1]
    
            json_finalres = json.loads("".join(json_str))
            print("json load success")
            print(json_finalres)
            score=json_finalres["score"]["score"]
            comments=json_finalres["score"]["comment"]
            print("score is: %s comments is: %s"%(score,comments))
            item = JinrongjieItem()
            item["stock_id"] = g_stock_id
            item["stock_names"] = g_stock_name
            item["TotalScore"] = score
            item["comments"]=comments
            yield item
            newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
        except Exception as e:
            print("error occur")
            print('str(Exception):\t', str(Exception))
            print('str(e):\t\t', str(e))
            print('repr(e):\t', repr(e))
            newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
        pass
