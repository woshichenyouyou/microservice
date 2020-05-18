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
    nexturlt="http://stock.jrj.com.cn/action/score/getOverallScore.jspa?isJson=0&vname=zonghe&code=%s"%nextstockno
    print(nexturlt)
    return nexturlt
class JinrongjiespiderSpider(scrapy.Spider):
    name = 'jinrongjiespider'
    allowed_domains = ['https://www.jianshu.com/']
    start_urls = ['http://stock.jrj.com.cn/action/score/getOverallScore.jspa?isJson=0&vname=zonghe&code=603817']

    def parse(self, response):
        if response.status == 404:
            print("404 error occur")
            newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
            return
        try:
            #print("response from url success")
            #print("response type is:")
            #print(type(response))
            #print("response content is:")
            #print(response)
            res = response.body.decode(response.encoding)
            #print("After decode response, type is:")
            #print(type(res))
            json_str = res.split("=", 1)[1]
            #print("js is: %s"%json_str)
            json_finalres = json.loads(json_str)
            #print("json load success")
            #print(json_finalres)
            #print(type(json_finalres))
            score=json_finalres[0]["score"]
            percent=json_finalres[0]["percent"]
            #print("score is: %s percent is: %s"%(score,percent))
            item = JinrongjieItem()
            item["stock_id"] = g_stock_id
            item["stock_names"] = g_stock_name
            item["TotalScore"] = score
            item["percent"]=percent
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
