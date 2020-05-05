# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DazhihuiXiaozhiPipeline(object):
    def process_item(self, item, spider):
        print("dazhihuipipeline")
        print("stock_id: %s"% item['stock_id'])
        print("stock_names: %s"% item['stock_names'])
        print("TotalScore: %s"% item['TotalScore'])
        print(type(item['TotalScore']))
        TotalScore=item['TotalScore']
        str = item['stock_id']+","+item['stock_names']+","+TotalScore +"\n"
        print(str)       
        f=open("..//..//result//dazhihui.csv","a+")
        f.write(str)
        f.close()
        return item
