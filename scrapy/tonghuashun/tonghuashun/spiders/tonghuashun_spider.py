# -*- coding: utf-8 -*-
import scrapy
import os
import sys
import chardet
import scrapy
from tonghuashun.items import TonghuashunItem
from pathlib import Path
from scrapy.http import Request
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



class TonghuashunSpiderSpider(scrapy.Spider):
    name = 'tonghuashun_spider'
    allowed_domains = ['http://doctor.10jqka.com.cn/']
    start_urls = ['http://http://doctor.10jqka.com.cn//']

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
            global_current_stock_id,global_current_stock_name,global_current_stock_area, newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
        except:
            print("error occur")
            global_current_stock_id,global_current_stock_name,global_current_stock_area, newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)

        pass
