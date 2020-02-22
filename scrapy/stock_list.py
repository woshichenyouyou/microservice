# coding=utf-8
import datetime
import os
import sys
import time
sys.path.append("../common/")
from rabbit import *
from logger import *
from messagequeue_receiver import messagequeue_receiver
from messagequeueclient import messagequeueclient
import json
import csv
class stock_list(messagequeue_receiver):
    def __init__(self):
        self._messagequeueclient = messagequeueclient('192.168.1.8',5672,'guest','guest')
        self._messagequeueclient.register_callback(self,'stock_list')

    def upon_message_received(self,data):
        print('mq_log_server upon_message_received start')
        print(type(data))
        
        #sb = bytes(data['688369.SH'], encoding = "utf8")
        
        j=json.loads(data.decode())
        print(type(j))
        print(j)
        self.writetocsv(j,'stock_list.csv')
        #sb=str(j['688369.SH'], encoding="utf-8")
        # sb = j['688369.SH']
        # print(sb)
        # print(sb)
    def writetocsv(self, my_dict,filename):
        with open('stock_list.csv', 'w') as f:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in my_dict.items()]
            
    def readtocsv(self,filename):
        with open(filename, 'rb') as csv_file:
            reader = csv.reader(csv_file)
            mydict = dict(reader)
            return mydict

if __name__ == '__main__':
    print('main start')
    stock_list = stock_list()

