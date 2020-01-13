# coding=utf-8
import pika
class Rabbit(object):
    def __init__(self,username,password,host,port=5672):
        self.host = str(host)
        self.port = int(port)
        self.crt = pika.PlainCredentials(username,password)
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host=self.host,
            port=self.port,credentials=self.crt))
        self.channel = self.conn.channel()
 
    def declare_queue(self,queue_name,is_durable):
        que = self.channel.queue_declare(queue=queue_name,exclusive=True)
        return que

    def declare_exchange(self,exchange, exchange_type):
        self.channel.exchange_declare(exchange=exchange, exchange_type=exchange_type) 

    def bind_queue(self,exchange,queue,routing_key):
        self.channel.queue_bind(exchange=exchange,queue=queue,routing_key=routing_key)

    def produce(self,r_key,msg,ex=''):
        self.channel.basic_publish(exchange=ex,
		routing_key=r_key,
		body=msg,
		properties=pika.BasicProperties(
			delivery_mode=2 # make message persistent
			))

    def set_qos(self):
        self.channel.basic_qos(prefetch_count=1)

    def consume(self,queue_name,callback=None,no_ack=False):
        if callback==None:
            self.channel.basic_consume(queue=queue_name, on_message_callback=callback2, auto_ack=True)             
        else:
            self.channel.basic_consume(on_message_callback=callback,queue=queue_name,auto_ack=True)
        self.channel.start_consuming()
 
    def msg_count(self,queue_name,is_durable=True):
        queue = self.channel.queue_declare(queue=queue_name,durable=is_durable)
        count = queue.method.message_count
        return count
 
    def close(self):
        self.conn.close()