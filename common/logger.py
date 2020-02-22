# coding=utf-8
import logging.config   # config 配置

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

from messagequeueclient import messagequeueclient
import json
class mylogger(logger):
    def __init__(self,logfilename):
        self.log = logger(logfilename)
        self.logins = self.log.getlogger()
        self.system_name=''
        self.subsystem_name=''
        self._messagequeueclient=None
    def remote_init(self,ip,port,user,password,system_name,subsystem_name):
        self._messagequeueclient = messagequeueclient(ip,port,user,password)
        self.system_name = system_name
        self.subsystem_name = subsystem_name

    def debug(self,msg,bremote=False):
        if bremote:
            data={"system":self.system_name,
                "subsystem":self.subsystem_name,
                "level":"debug",
                "message":msg}
            bodydata = json.dumps(data)
            self._messagequeueclient.send(bodydata,'log')
        else:            
            self.logins.debug('debug message') # 排错

    def info(self,msg,bremote=False):  
        if bremote:
            data={"system":self.system_name,
                "subsystem":self.subsystem_name,
                "level":"info",
                "message":msg}
            bodydata = json.dumps(data)
            self._messagequeueclient.send(bodydata,'log')
        else:   
            self.logins.info('debug message') # 正常信息

    def warning(self,msg,bremote=False):
        print("warning")   
        if bremote:
            print("warning1")
            data={"system":self.system_name,
                "subsystem":self.subsystem_name,
                "level":"warning",
                "message":msg}
            bodydata = json.dumps(data)
            self._messagequeueclient.send(bodydata,'log')
        else:  
            print("warning2")
            self.logins.warning('debug message') # 警告

    def error(self,msg,bremote=False):  
        if bremote:
            data={"system":self.system_name,
                "subsystem":self.subsystem_name,
                "level":"error",
                "message":msg}
            bodydata = json.dumps(data)
            self._messagequeueclient.send(bodydata,'log')
        else:   
            self.logins.error('debug message') # 错误

    def critical(self,msg,bremote=False):
        if bremote:
            data={"system":self.system_name,
                "subsystem":self.subsystem_name,
                "level":"critical",
                "message":msg}
            bodydata = json.dumps(data)
            self._messagequeueclient.send(bodydata,'log')
        else:     
            self.logins.critical('debug message') # 崩溃
