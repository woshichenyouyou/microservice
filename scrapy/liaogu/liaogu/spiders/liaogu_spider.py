# -*- coding: utf-8 -*-
import scrapy
import os
import sys
import chardet
from liaogu.items import LiaoguItem
from scrapy.http import Request
from pathlib import Path
from bs4 import BeautifulSoup
from lxml import etree
import js2xml
from scrapy_splash import SplashRequest,SplashFormRequest

stock_index=0
global_current_stock_id="600015"
global_current_stock_name="hxzq"
global_current_stock_area="SH"
def readallstock(filepath):
    stock_id=[]
    allstockdict={}
    pwd = os.getcwd()
    print("current path is:"+pwd)
    my_file = Path(filepath)
    if my_file.is_file():
        print(filepath+" is exist")
    else:
        print(filepath+" is not exist")
    with open(filepath, 'r+') as csv_file:
        for line in csv_file:
            id  =line.split(",")[0].split(".")[0].zfill(6)
            area=line.split(",")[0].split(".")[1]
            name =line.split(",")[1].replace('\n',"")
            
            stock_id.append(id)           
            stockinfo={}
            stockinfo["id"]=id
            stockinfo["area"]=area
            stockinfo["name"]=name
            allstockdict[id]=stockinfo
    return stock_id,allstockdict
stock_id_list,allstocksdict = readallstock(r"../../result/stock_list.csv")
def mynexturl():
    global stock_index
    stock_index = stock_index + 1
    #print (stock_index)
    print("%d of %d is finished."%(stock_index,len(stock_id_list)))    
    nextstockid = stock_id_list[stock_index]
    id = allstocksdict[nextstockid]["id"]
    #print("nextstockid: %s,id: %s"%(nextstockid,id))
    nextstockname=allstocksdict[nextstockid]["name"]
    area=allstocksdict[nextstockid]["area"]
    print(nextstockid +"," + nextstockname+","+area)
    nexturlt="https://www.liaogu.com/zg-detail.html?stockCode=%s"%(nextstockid)
    print(nexturlt)
    return nextstockid,nextstockname,area,nexturlt

class LiaoguSpiderSpider(scrapy.Spider):
    name = 'liaogu_spider'
    allowed_domains = ['www.liaogu.com']
    #start_urls = ['https://www.liaogu.com/zg-detail.html?stockCode=600015']
    start_urls = 'https://www.liaogu.com/zg-detail.html?stockCode=600015'
    def start_requests(self):
        #yield SplashRequest(url=self.start_urls,callback=self.parse,meta={'title':'xxxx'},args={'wait':"3"}
        yield SplashRequest(url=self.start_urls,callback=self.parse, args={'images':0,'wait':3,'timeout': 5})

    def parse(self, response):
        global global_current_stock_id
        global global_current_stock_name
        global global_current_stock_area
        if response.status == 404:
            print("404 error occur")
            global_current_stock_id,global_current_stock_name,global_current_stock_area, newurl=mynexturl()
            yield SplashRequest(url=newurl,callback=self.parse, args={'images':0,'wait':3,'timeout': 5})
            return
        try:
            #print(response.text)
            ret = response.xpath('//p[@class="zhpf"]/b/text()').extract()[0]
            #print("the res that you want is: %s"%ret)
            item = LiaoguItem()
            item = LiaoguItem()
            item["stock_id"]=global_current_stock_id
            item["stock_names"]=global_current_stock_name
            item["TotalScore"]=ret
            yield item
            yield SplashRequest(url=newurl,callback=self.parse, args={'images':0,'wait':3,'timeout': 5})  
        except Exception as e:
            print("error occur")
            print('str(Exception):\t', str(Exception))
            print('str(e):\t\t', str(e))
            print('repr(e):\t', repr(e))

            global_current_stock_id,global_current_stock_name,global_current_stock_area, newurl=mynexturl()
            yield SplashRequest(url=newurl,callback=self.parse, args={'images':0,'wait':3,'timeout': 5})       
        pass
