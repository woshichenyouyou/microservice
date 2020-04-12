import tushare as ts
import pysnooper
ts.set_token('9dbd435e2a93b6cb5a82fd48053bdcb3a7b27aafa0daee5c9b4fadb2')
print(ts.__version__)


# coding=utf-8
import os
import sys
sys.path.append("../common/")
from messagequeueclient import messagequeueclient
import json

#@pysnooper.snoop()
def getstockinfoold():
    res=ts.get_stock_basics()
    print(res)
    print(res.columns)
    length=len(res)
    for i in range(length):
        print('code: %s,name: %s)'%(res.iloc[i].name,res.iloc[i]['name']))

#@pysnooper.snoop()
def getstockinfonew():
    pro = ts.pro_api()
    res = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    #print(res)
    #print(res.columns)
    length=len(res)
    data={}
    for i in range(length):
        #print('code: %s,name: %s)'%(res.iloc[i]['ts_code'],res.iloc[i]['name']))
        data[res.iloc[i]["ts_code"]]=res.iloc[i]["name"]
        #print(type(data[res.iloc[i]["ts_code"]]))
        #print(type(res.iloc[i]["name"]))
    print(data)
    writetocsv(data,'../result/stock_list.csv')
    dataj = json.dumps(data)
    return dataj

def writetocsv(my_dict,filename):
    with open(filename, 'w') as f:
        [f.write('{0},{1}\n'.format(key, value)) for key, value in my_dict.items()]  

if __name__=="__main__":
    data=getstockinfonew()
#    messagequeueclient = messagequeueclient('192.168.1.8',5672,'guest','guest')
#    messagequeueclient.send(data,'stock_list')
