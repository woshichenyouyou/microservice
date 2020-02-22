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
class mq_log_server(messagequeue_receiver):
    def __init__(self):
        self._messagequeueclient = messagequeueclient('192.168.1.8',5672,'guest','guest')
        self._messagequeueclient.register_callback(self,'log')
        self.loglist={}

    def upon_message_received(self,data):
        print('mq_log_server upon_message_received start')
        #sb = bytes(s, encoding = "utf8") 
        j=json.loads(data.decode())
        print('system: %s'%j['system'])
        print('subsystem: %s'%j['subsystem'])
        print('level: %s'%j['level'])
        print('message: %s'%j['message'])
        logins=self.getloger(j['system'],j['subsystem'])
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


    def createloger(self,strsystem,strsubsystem):
        
        key=strsystem+"_"+strsubsystem
        print('createloger for: %s'%key)
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y_%m_%d__%H_%M_%S")
        log_filename=strsystem+'_'+strsubsystem +'_' +otherStyleTime+'.log'
        print('log_filename : %s'%log_filename)
        log = logger(log_filename)
        mylog=log.getlogger()
        self.loglist[key]=mylog

    def getloger(self,strsystem,strsubsystem):
        key=strsystem+"_"+strsubsystem
        if self.loglist.get(key):
            print('getloger by key: %s'%key)
            mylog = self.loglist.get(key)
            return mylog
        else:
            print('the loger not exist, create new for key: %s'%key)
            self.createloger(strsystem,strsubsystem)
            mylog = self.loglist.get(key)
            return mylog

if __name__ == '__main__':
    print('main start')
    mq_log_server = mq_log_server()
#    while True:
#        time.sleep(30)
