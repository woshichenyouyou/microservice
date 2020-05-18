# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import chardet

class EastmoneyPipeline(object):
    def process_item(self, item, spider):
        #print("EastmoneyPipeline")
        #print("stock_id: %s"% item['stock_id'])
        #print("stock_names: %s"% item['stock_names'])
        #print("TotalScore: %s"% item['TotalScore'])
        #print("TotalScoreCHG: %s"% item['TotalScoreCHG'])
        #print("LeadPre: %s"% item['LeadPre'])
        #print("RisePro: %s"% item['RisePro'])
        #print("MsgCount: %s"% item['MsgCount'])
        #print("CapitalScore: %s"% item['CapitalScore'])
        #print("D1: %s"% item['D1'])
        #print("ValueScore: %s"% item['ValueScore'])
        #print("MarketScoreCHG: %s"% item['MarketScoreCHG'])
        #print("Status: %s"% item['Status'])
        #print("Comment: %s"% item['Comment'])
        #print("UpdateTime: %s"% item['UpdateTime'])
        # ss = item['stock_id']
        # adchar = chardet.detect(ss)
        # print("stock_id adchar:%s"%adchar)
        # sss = item['TotalScore']
        # print(type(sss))
        # print(sss)
        # adchar = chardet.detect(sss)
        # print("Comment adchar:%s"%adchar)
        #print(type(item['stock_names']))
        ss = item['stock_names']
        #adchar = chardet.detect(ss)
        #print("stock_names adchar:%s"%adchar)
        #print(ss)
        #print(type(ss))

        str = item['stock_id']+","+ss+","+item['TotalScore']+","+item['TotalScoreCHG']+","+item['LeadPre']+","+item['RisePro']+","+item['MsgCount']+","+item['CapitalScore']+","+item['D1']+","+item['MarketScoreCHG']+","+item['Status']+","+item['Comment']+","+item['UpdateTime']+"\n"
        str = item['stock_id']+","+ss+","+item['TotalScore']+"\n"

        print("encode start")
        print(str)
        
        f=open("..//..//result//eastmoney.csv","a+")
        f.write(str)
        f.close()
        return item
