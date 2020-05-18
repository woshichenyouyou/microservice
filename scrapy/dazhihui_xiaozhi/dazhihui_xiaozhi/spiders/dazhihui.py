# -*- coding: utf-8 -*-
import os
import sys
import chardet
import scrapy
from dazhihui_xiaozhi.items import DazhihuiXiaozhiItem
from scrapy.http import Request
from pathlib import Path
from bs4 import BeautifulSoup
from lxml import etree
import js2xml
#from scrapy import optional_features
#optional_features.remove('boto')
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
    nexturlt="http://aia.gw.com.cn/index.php?c=robot&DZHSPECIAL=36&a=index&stock=%s%s"%(area,nextstockid)
    print(nexturlt)
    return nextstockid,nextstockname,area,nexturlt
   

class DazhihuiSpider(scrapy.Spider):
    name = 'dazhihui'
    allowed_domains = ['http://aia.gw.com.cn']
    start_urls = ['http://aia.gw.com.cn/index.php?c=robot&DZHSPECIAL=36&a=index&stock=SH600015']
    #start_urls = list(mynexturl())
    def parse(self, response):
        global global_current_stock_id
        global global_current_stock_name
        global global_current_stock_area
        if response.status == 404:
            print("404 error occur")
            global_current_stock_id,global_current_stock_name,global_current_stock_area, newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
            return
        try:
            print("response from url success")
            #print("response type is:")
            #print(type(response))
            #print("response content is:")
            #print(response)
            resp = response.text
            soup = BeautifulSoup(resp,'lxml')
            res = response.body.decode(response.encoding)

            scripts = soup.find_all('script')
            for script in scripts:
                if type(script.string) is type(None):
                    continue
                elif script.string.find("timeTenOver") > 0:
                    #print(script)
                    src=script
                    break  
            src_text = js2xml.parse(src.string, encoding='utf-8',debug=False) 
            src_tree = js2xml.pretty_print(src_text)    
            #print(src_tree)

            selector = etree.HTML(src_tree)    
            timeTenOver = selector.xpath('//program/var[@name="timeTenOver"]/number/@value')
            secondOver = selector.xpath('//program/var[@name="secondOver"]/number/@value')
            strtimeTenOver=''.join(timeTenOver)
            strsecondOver=''.join(secondOver)
            #print("timeTenOver is: %s secondOver is: %s"%(strtimeTenOver,strsecondOver))
            score="%s.%s"%(strtimeTenOver,strsecondOver)
            print("score is: %s"%score)
            item = DazhihuiXiaozhiItem()
            item["stock_id"]=global_current_stock_id
            item["stock_names"]=global_current_stock_name
            item["TotalScore"]=score
            yield item
            global_current_stock_id,global_current_stock_name,global_current_stock_area, newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
        except Exception as e:
            print("error occur")
            print('str(Exception):\t', str(Exception))
            print('str(e):\t\t', str(e))
            print('repr(e):\t', repr(e))

            global_current_stock_id,global_current_stock_name,global_current_stock_area, newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
        pass