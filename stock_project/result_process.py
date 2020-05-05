import os
import sys
sys.path.append("../common/")
from csvctl import *
head,stock_info = opencsv("../result/stock_list.csv",False)
header,dazhihui_data_list = opencsv("../result/dazhihui.csv",False)
header,eastmoney_data_list = opencsv("../result/eastmoney.csv",False)
header,jinrongjie_data_list = opencsv("../result/jinrongjie.csv",False)
header,jinrongjie_score_data_list = opencsv("../result/jinrongjie_score.csv",False)
header,tonghuashun_data_list = opencsv("../result/scrapystockinfo.csv",False)

stock_all_result=[]
for item in stock_info:
    stock_all_result_item=[]
    print(item[0].split("."))
    stock_id=item[0].split(".")[0]
    stock_area=item[0].split(".")[1]
    stock_name=item[1]
    stock_all_result_item.append(stock_id)#id
    stock_all_result_item.append(stock_name)#name
    stock_all_result_item.append(stock_area)#area
    print(stock_all_result_item)
    #########################################################dazhihui
    res="0.001"
    for dazhihui_item in dazhihui_data_list:
        if dazhihui_item[0] == stock_id:
            res = dazhihui_item[2]
            break
    stock_all_result_item.append(res)
    ##########################################################eastmoney
    res="0.001"
    for eastmoney_item in eastmoney_data_list:
        if eastmoney_item[0] == stock_id:
            res = eastmoney_item[2]
            break
    stock_all_result_item.append(res)
    ##########################################################jinrongjie
    bfind_result=False
    res="0.001"
    for jinrongjie_item in jinrongjie_data_list:
        if jinrongjie_item[0] == stock_id:
            res = jinrongjie_item[2]
            break
    stock_all_result_item.append(res)
    ##########################################################jinrongjie_score
    bfind_result=False
    res="0.001"
    for jinrongjie_score_item in jinrongjie_score_data_list:
        if jinrongjie_score_item[0] == stock_id:
            res = jinrongjie_score_item[2]
            break
    stock_all_result_item.append(res)
    ##########################################################tonghuashun
    bfind_result=False
    res="0.001"
    for tonghuashun_item in tonghuashun_data_list:
        if tonghuashun_item[0] == stock_id:
            res = tonghuashun_item[2]
            break
    stock_all_result_item.append(res)
    stock_all_result.append(stock_all_result_item)
    ##########################################################
writecsv("../result/all_result.csv",stock_all_result,["id","name","area","dazhihui","eastmoney","jinrongjie","jinrongjie_score","tonghuashun"])
