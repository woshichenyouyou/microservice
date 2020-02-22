# coding=utf-8
import os
import sys
sys.path.append("../common/")
from logger import *


mylog = mylogger("test1.log")
mylog.remote_init('192.168.1.8',5672,'guest','guest','xray','rtip')
# print('登陆成功')
mylog.debug('debug message',True) # 排错
mylog.info('info message',True) # 正常信息
mylog.warning('warning message',True) # 警告
mylog.error('error message',True) # 错误
mylog.critical('critical message',True) # 崩溃
