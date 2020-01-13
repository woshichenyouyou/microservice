# -*- coding:utf-8 -*-
import os
import sys
sys.path.append("../common/")
import time
from rabbit import *
if __name__ == '__main__':
    rabbit=Rabbit('guest','guest','192.168.1.8',5672)
    rabbit.declare_exchange('direct_logs', 'direct')   
    data={}
    data['system']='sysdata'
    data['subsystem']='subsysdata2'
    data['level']='error'
    data['message']='this is the message content!'
    bodydata = bytes(str(data), encoding = "utf8")
    rabbit.produce('log',bodydata,'direct_logs')
    rabbit.close()