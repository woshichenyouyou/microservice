import tushare as ts
import pysnooper
ts.set_token('8ad36a275e9ca6a4bccded5db104f46ecdb260341f53c27abca2ed69')
print(ts.__version__)

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
    print(res)
    print(res.columns)
    length=len(res)
    for i in range(length):
        print('code: %s,name: %s)'%(res.iloc[i]['ts_code'],res.iloc[i]['name']))
if __name__=="__main__":
    getstockinfonew()
    
