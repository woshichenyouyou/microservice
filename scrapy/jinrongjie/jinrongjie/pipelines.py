# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JinrongjiePipeline(object):
    def process_item(self, item, spider):
        print("jinrongjiePipeline")
        print("stock_id: %s"% item['stock_id'])
        print("stock_names: %s"% item['stock_names'])
        print("TotalScore: %s"% item['TotalScore'])
        print("comments: %s"% item['comments'])
        str = item['stock_id']+","+item['stock_names']+","+item['TotalScore']+","+item['comments']+"\n"
        print(str)       
        f=open("..//..//result//jinrongjie.csv","a+")
        f.write(str)
        f.close()
        return item
