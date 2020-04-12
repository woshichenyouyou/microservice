# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class StockscrapyPipeline(object):
    def process_item(self, item, spider):
#        print(item['stock_names'])
#        print(item['score_h'][0])
#        print(item['score_l'][0])
#        print(type(item['score_h']))
#        print("stockname is: %s"% item['stock_names'][0])
        totalscore=item['score_h'][0]+item['score_l'][0]
        print("score is: "+totalscore)
        
        print("score_tech: %s"% "".join(item['score_tech'])[0:3])
        print("score_money: %s"% "".join(item['score_money'])[0:3])
        print("score_news: %s"% "".join(item['score_news'])[0:3])
        print("score_industry: %s"% "".join(item['score_industry'])[0:3])
        print("score_basic: %s"% "".join(item['score_basic'])[0:3])
        stock_name = item['stock_names'][0][0:len(item['stock_names'][0])-8]
        stock_id = item['stock_names'][0][len(item['stock_names'][0])-7:len(item['stock_names'][0])-1]
        #print ("stockname:%s"%stock_name)
        
        print(stock_id)
        str = stock_name+','+stock_id+','+totalscore+','+ "".join(item['score_tech'])[0:3]   +','+  "".join(item['score_money'])[0:3]  +','+ "".join(item['score_news'])[0:3]  +','+ "".join(item['score_industry'])[0:3]  +','+  "".join(item['score_basic'])[0:3]+"\n"
        #str = unicode(str).encode("utf-8")
        print(str)
        output_filename = "scrapystockinfo.csv"
        print("output filename:%s"%output_filename)
        f=open(output_filename,"a+")
        f.write(str)
        f.close()
        return item
