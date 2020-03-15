from flask import Flask
from flask import request
from flask import jsonify
import datetime

import utils
import hit

import csv
import sys
import json

startTime = datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")
def opencsv(filepath,isheadexist):
    filename = filepath
    data_list=[]
    # 打开文件
    with open(filename) as f:
        # 创建cvs文件读取器
        reader = csv.reader(f)
        if isheadexist:            
            # 读取第一行，这行是表头数据。
            header_row = next(reader)
        else:
            header_row = None
        # 读取第二行，这行是真正的数据。
        for row in reader:
            data_list.append(row)           
            #print("id:%s en:%s cn:%s mat:%s"%(id,en,cn,mat))    
    return header_row,data_list
def opencsv_to_json(filepath,isheadexist,header):
    with open(filepath) as wf:
        reader = csv.DictReader(wf,fieldnames=header)
        print(type(reader))
        total_dict = {}
        for row in reader:
            id = row["stock_id"]
            r={id:row}
            total_dict=dict(total_dict,**r)
        j = json.dumps(total_dict)
        print(j)
        return j
app = Flask(__name__)

@app.route("/")
def show_details() :
    global startTime
    return "<html>" + \
           "<head><title>Docker + Flask Demo</title></head>" + \
           "<body>" + \
           "<table>" + \
           "<tr><td> Start Time </td> <td>" +  startTime + "</td> </tr>" \
           "<tr><td> Hostname </td> <td>" + utils.gethostname() + "</td> </tr>" \
           "<tr><td> Local Address </td> <td>" + utils.getlocaladdress() + "</td> </tr>" \
           "<tr><td> Remote Address </td> <td>" + request.remote_addr + "</td> </tr>" \
           "<tr><td> Server Hit </td> <td>" + str(hit.getServerHitCount()) + "</td> </tr>" \
           "</table>" + \
           "</body>" + \
           "</html>"

@app.route("/json")
def send_json() :
    global startTime
    return jsonify( {'StartTime' : startTime,
                     'Hostname': utils.gethostname(),
                     'LocalAddress': utils.getlocaladdress(),
                     'RemoteAddress':  request.remote_addr,
                     'Server Hit': str(hit.getServerHitCount())} )
@app.route("/stocktopn")
def stocktopn():
    srcfile = r"../result/eastmoney_10.csv"
    headerfile = r"../result/eastmoney_header.csv"
    header,data=opencsv(headerfile,True)
    json_data=opencsv_to_json(srcfile,False,header)
    return json_data
if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
