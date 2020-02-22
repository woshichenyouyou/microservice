#from multiprocessing import Process
from threading import Thread
import sys
import json
sys.path.append("../common/")
from rabbit import *
# TODO message queue client implementation
class messagequeueclient:
    def __init__(self, ip,port,user,password):
        self.rabbit = Rabbit(ip,port,user,password)
        self.rabbit.declare_exchange('direct_logs','direct')
    def send(self, data,key):
        print("messagequeueclient.send start ...")
        bodydata = bytes(str(data), encoding = "utf8")
        self.rabbit.produce('log',bodydata,'direct_logs')
        print("messagequeueclient.send END")

    def _start_receiver(self):
        print('_start_receiver start')
        #p = Process(target=start_receiver, args=(self._read_exchange_name, self._routing_key, self._callback))
        p = Thread(target=start_receiver, args=(self,'direct_logs', 'log', self._callback))
        p.start()

    def register_callback(self, receiver):
        self._receiver = receiver
        self._start_receiver()

    def _callback(self, ch, method, properties, body):
        print(" CLIENT --- Receive [x] %s:%s", method.routing_key, body)
        self._call_receiver(body)

    def _call_receiver(self, body):
        print("messagequeueclient._call_receiver start ...")
        # logger.debug(body)
        #m = json.loads(body.decode())
        # logger.debug(m)
        m=json.loads(body.decode())
        
        self._receiver.upon_message_received(m)
        print("messagequeueclient._call_receiver END")


def start_receiver(messagequeueclient_ins,exchange_name, routing_key, callback_fn):
    # init mq
    print("start_receiver start")
    messagequeueclient_ins.rabbit.declare_exchange('direct_logs', 'direct')
    q = messagequeueclient_ins.rabbit.declare_queue('',True)
    messagequeueclient_ins.rabbit.bind_queue('direct_logs',q.method.queue,'log')
    messagequeueclient_ins.rabbit.consume(q.method.queue,callback_fn)
    print('start to recv')



