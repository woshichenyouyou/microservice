# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class LiaoguPipeline(object):
    def process_item(self, item, spider):
        TotalScore=item['TotalScore']
        TotalScore=TotalScore.replace("%","")
        str = item['stock_id']+","+item['stock_names']+","+TotalScore +"\n"
        #print(str)       
        f=open("..//..//result//liaogu.csv","a+")
        f.write(str)
        f.close()
        return item
