# coding=utf-8
import os
import sys
sys.path.append("../common/")
from log_local import *


log = logger("../log/test1.log")
mylog=log.getlogger()
# print('��½�ɹ�')
mylog.debug('debug message') # �Ŵ�
mylog.info('info message') # ������Ϣ
mylog.warning('warning message') # ����
mylog.error('error message') # ����
mylog.critical('critical message') # ����
