# coding=utf-8
import datetime
import os
import sys
sys.path.append("../common/")
from rabbit import *
from logger import *

def callback(ch, method, properties, body):
    print("routing_key is: %r body is: %r" % (method.routing_key, body))
    #sb = bytes(s, encoding = "utf8") 
    strbody = str(body, encoding = "utf8")
    print(type(strbody))  
    j = eval(strbody)
    print('system: %s'%j['system'])
    print('subsystem: %s'%j['subsystem'])
    print('level: %s'%j['level'])
    print('message: %s'%j['message'])
    logins=getloger(j['system'],j['subsystem'])
    if j['level']=="debug":
        print('logins.debug')
        logins.debug(j['message'])
    elif j['level']=="info":
        print('logins.info')
        logins.info(j['message'])
    elif j['level']=="warning":
        print('logins.warning')
        logins.warning(j['message'])
    elif j['level']=="error":
        print('logins.error')
        logins.error(j['message'])
    elif j['level']=="critical":
        print('logins.critical')
        logins.critical(j['message'])

loglist={}
def createloger(strsystem,strsubsystem):
    
    key=strsystem+"_"+strsubsystem
    print('createloger for: %s'%key)
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y_%m_%d__%H_%M_%S")
    log_filename=strsystem+'_'+strsubsystem +'_' +otherStyleTime+'.log'
    print('log_filename : %s'%log_filename)
    log = logger(log_filename)
    mylog=log.getlogger()
    loglist[key]=mylog

def getloger(strsystem,strsubsystem):
    key=strsystem+"_"+strsubsystem
    if loglist.get(key):
        print('getloger by key: %s'%key)
        mylog = loglist.get(key)
        return mylog
    else:
        print('the loger not exist, create new for key: %s'%key)
        createloger(strsystem,strsubsystem)
        mylog = loglist.get(key)
        return mylog

if __name__ == '__main__':
    rabbit=Rabbit('guest','guest','192.168.1.8',5672)
    rabbit.declare_exchange('direct_logs', 'direct')
    q = rabbit.declare_queue('',True)
    rabbit.bind_queue('direct_logs',q.method.queue,'log')
    rabbit.consume(q.method.queue,callback)
    print('start to recv')
