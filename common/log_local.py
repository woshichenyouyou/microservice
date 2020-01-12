# coding=utf-8
import logging.config   # config 配置

# 定义三种日志输出格式 开始
class logger:

    def __init__(self,logfilename):           
        self.standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                      '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
        self.simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        self.id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

        # 定义日志输出格式 结束
        self.logfile_path_staff = logfilename

        # log配置字典
        # LOGGING_DIC第一层的所有的键不能改变
        self.LOGGING_DIC = {
            'version': 1,  # 版本号
            'disable_existing_loggers': False,  #　固定写法
            'formatters': {
                'standard': {
                    'format': self.standard_format
                },
                'simple': {
                    'format': self.simple_format
                },
            },
            'filters': {},
            'handlers': {
                #打印到终端的日志
                'sh': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',  # 打印到屏幕
                    'formatter': 'simple'
                },
                #打印到文件的日志,收集info及以上的日志
                'fh': {
                    'level': 'INFO',
                    'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
                    'formatter': 'standard',
                    'filename': self.logfile_path_staff,  # 日志文件
                    'maxBytes': 100000,  # 日志大小 300字节
                    'backupCount': 5,  # 轮转文件的个数
                    'encoding': 'utf-8',  # 日志文件的编码
                },
            },
            'loggers': {
                #logging.getLogger(__name__)拿到的logger配置
                '': {
                    'handlers': ['sh', 'fh'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
                    'level': 'DEBUG',
                    'propagate': True,  # 向上（更高level的logger）传递
                },
            },
        }
    def getlogger(self):
        logging.config.dictConfig(self.LOGGING_DIC)  # 导入上面定义的logging配置 通过字典方式去配置这个日志
        logger = logging.getLogger()  # 生成一个log实例  这里可以有参数 传给task_id
        return logger
        # logger.debug('It works!')  # 记录该文件的运行状态

if __name__ =="__main__":
    log = logger("../log/test1.log")
    mylog=log.getlogger()
    # print('登陆成功')
    mylog.debug('debug message') # 排错
    mylog.info('info message') # 正常信息
    mylog.warning('warning message') # 警告
    mylog.error('error message') # 错误
    mylog.critical('critical message') # 崩溃
