# -*- coding: utf-8 -*-
import os
import re
import json
import sys
import chardet
import scrapy
from eastmoney.items import EastmoneyItem
from scrapy.http import Request
#from scrapy import optional_features
from commondlib import stockctl

#optional_features.remove('boto')

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
    nexturlt="http://gwapi.eastmoney.com/agent/1258/stockcomment/api/so/%s.json?appid=1466&tk=28228DE7FA07D013677756DD94686DEA&cb=jQuery112405065479470006455_1560957752762&_=1560957752774"%nextstockno
    print(nexturlt)
    return nexturlt
class EastmoneyscoreSpider(scrapy.Spider):
    handle_httpstatus_list = [404, 500]
    name = "eastmoneyscore"
    allowed_domains = ["eastmoney.com"]
    start_urls = (
        'http://gwapi.eastmoney.com/agent/1258/stockcomment/api/so/600015.json?appid=1466&tk=28228DE7FA07D013677756DD94686DEA&cb=jQuery112405065479470006455_1560957752762&_=1560957752774',
    )

    def parse(self, response):
        if response.status == 404:
            print("404 error occur")
            newurl=mynexturl()
            yield Request(newurl,callback=self.parse,dont_filter=True)
            return
        try:
            print("response from url success")
            #print("response type is:")
            #print(type(response))
            #print("response content is:")
            #print(response)
            res = response.body.decode(response.encoding)
            #print("After decode response, type is:")
            #print(type(res))
            #print(res)
            p1 = re.compile(r'[(](.*?)[)]', re.S)
            finalres = re.findall(p1, res)
            #print("finalres is:")
            #print(finalres)
            json_finalres = json.loads("".join(finalres))
            #print("json load success")
            Scode = json_finalres['Scode']
            ApiResults = json_finalres['ApiResults']
            HasError = json_finalres['HasError']
            #print("ApiResults is:")
            #print(ApiResults)
            #print("ApiResults type is:")
            #print(type(ApiResults))
            Overall=ApiResults['zj']['Overall'][0]
            #print(type(Overall))
            TotalScore = Overall['TotalScore']
            TotalScoreCHG = Overall['TotalScoreCHG']
            LeadPre = Overall['LeadPre']
            RisePro = Overall['RisePro']
            MsgCount = Overall['MsgCount']
            CapitalScore = Overall['CapitalScore']
            D1 = Overall['D1']
            ValueScore = Overall['ValueScore']
            MarketScoreCHG = Overall['MarketScoreCHG']
            Status = Overall['Status']
            Comment = Overall['Comment']
            UpdateTime=Overall['UpdateTime']
            #print("Overall is:")
            #print(Overall)
            item = EastmoneyItem()
            item['stock_names'] = g_stock_name
            item['stock_id'] = g_stock_id
            item['TotalScore'] = TotalScore
            item['TotalScoreCHG'] = TotalScoreCHG
            item['LeadPre'] = LeadPre
            item['RisePro'] = RisePro
            item['MsgCount'] = MsgCount
            item['CapitalScore'] = CapitalScore
            item['D1'] = D1
            item['ValueScore'] = ValueScore
            item['MarketScoreCHG'] = MarketScoreCHG
            item['Status'] = Status
            item['Comment'] = Comment
            item['UpdateTime'] = UpdateTime    
            #print("json success")
            
            # item['total_score']=response.xpath('//div[@class="pingfen"]/span/text()')
            # for i in item['total_score']:
                # print(i)
            # item['today_score']=response.xpath('//div[@class="biaoxian"]/span/text()').extract()
            # item['win_score']=response.xpath('//div[@class="dabai"]/span/text()').extract()
            # item['tomorrow_score']=response.xpath('//div[@class="shangzhang"]/span/text()').extract()
            # print("start:")
            # print(item['total_score'])
            # print(item['today_score'])
            # print(item['win_score'])
            # print(item['tomorrow_score'])
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
