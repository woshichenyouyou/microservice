# coding=utf-8
import os
import sys
sys.path.append("../common/")
from logger import *


mylog = mylogger("test1.log")
mylog.remote_init('192.168.1.8',5672,'guest','guest','xray','rtip')
# print('��½�ɹ�')
mylog.debug('debug message',True) # �Ŵ�
mylog.info('info message',True) # ������Ϣ
mylog.warning('warning message',True) # ����
mylog.error('error message',True) # ����
mylog.critical('critical message',True) # ����
