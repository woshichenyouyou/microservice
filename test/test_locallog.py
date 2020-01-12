# coding=utf-8
import os
import sys
sys.path.append("../common/")
from log_local import *


log = logger("../log/test1.log")
mylog=log.getlogger()
# print('登陆成功')
mylog.debug('debug message') # 排错
mylog.info('info message') # 正常信息
mylog.warning('warning message') # 警告
mylog.error('error message') # 错误
mylog.critical('critical message') # 崩溃
