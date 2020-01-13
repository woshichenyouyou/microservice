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