# coding=utf-8
import logging.config   # config 配置
import pika
import sys
import datetime
import json
# 定义三种日志输出格式 开始
class logger:
    def __init__(self,logfilename):  
        #logging.root.setLevel(logging.NOTSET)         
        self.standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                      '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
        self.simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        self.id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

        # 定义日志输出格式 结束
        self.logfile_path = logfilename
        
        # 创建一个handler，用于写入日志文件
        self.fh = logging.handlers.RotatingFileHandler(self.logfile_path,maxBytes=10000,backupCount=5) 
        self.fh.setFormatter(logging.Formatter(self.standard_format))
        self.fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        self.ch = logging.StreamHandler()       
        self.ch.setFormatter(logging.Formatter(self.standard_format))    
        self.ch.setLevel(logging.DEBUG) 
        self.logger = logging.getLogger()
        
        self.logger.addHandler(self.fh) #logger对象可以添加多个fh和ch对象
        self.logger.addHandler(self.ch)

    def getlogger(self):       
        return self.logger
        # logger.debug('It works!')  # 记录该文件的运行状态

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

log = logger("test1.log")
mylog=log.getlogger()

def callback(ch, method, properties, body):
    print("routing_key is: %r body is: %r" % (method.routing_key, body))
    #sb = bytes(s, encoding = "utf8") 
    strbody = str(body, encoding = "utf8")  
    j = json.loads(strbody)
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

def setup():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.189.132.41',port=5672,credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')                           
    result = channel.queue_declare(queue='',exclusive=True)
    queue_name = result.method.queue

    routing_key = 'log'
    channel.queue_bind(exchange='direct_logs',
                        queue=queue_name,
                        routing_key=routing_key)
                        
    print(' [*] Waiting for logs. To exit press CTRL+C')
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)                      
    channel.start_consuming()

    

if __name__ == '__main__':
    #createloger('vue','frontend')
    getloger('vue','frontend')
    #setup()
