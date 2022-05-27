#@@@@@@@@@@@@@@@@@@@@Pheonix.Molecules.Communicator.Rabbit@@@@@@@@@@@@@@||
'''
---
<(META)>:
	DOCid: b2d7b141-af47-4d48-9c9a-211decb4d316
	name: Molecules Level Communicator Module Rabbit Extension Py Doc #	||
	description: >
	version: 0.0.0.0.0.0
	path: <[LEXIvrs]>pheonix/molecules/communicator/rabbit.py
	outline:
	authority: document|this
	security: sec|lvl2
	<(WT)>: -32
'''
# -*- coding: utf-8 -*-
#=======================================================================||
import os, datetime as dt, logging#								||
#===========================3rd Party Modules===========================||
try:
	import pika
except:
	pass
#=======================================================================||
from pheonix.comm import comm#									||
from condor import condor#								||
from pheonix.thing import thing#								||
#=======================================================================||
here = os.path.join(os.path.dirname(__file__),'')#						||
#=======================================================================||
class client:#															||
	''#						||
	version='0.0.0.0.0.0'#												||
	def __init__(self, cfg=None):#										||
		pxcfg = here+'z-data_/comsys.yaml'#						||use default configuration
		self.config = config.instruct(pxcfg).select('rabbitmq'
												).override(cfg).dikt#	||load configuration file
	def assignQs(self, q=None):#										||
		''#														||
		self.con = self._create_connection()#							||
		chan = self.con.channel()#										||
		self._create_queue(chan, q)#									||
		return chan#													||
	def callback(self, body):#											||
		''#																||
		comm.see([' [x] Received %r' % body,])#							||
		return body#													||
	def recieve(self, que='time', cback=None):#							||
		'Start Recieving Messages & Executing Callback Methods'#		||
		chan = self.assignQs(que)
		if cback == None:
			cback = self.callback
		self.message_received_callback = cback
		chan.basic_consume('time', self._consume_message)
		chan.start_consuming()
	def transmit(self, message=None, que='time'):
		''
		if message == None:
			message = next(thing.when().gen())
		chan = self.assignQs(que)
		chan.basic_publish(exchange='', routing_key='time', body=message)
		self.con.close()
	def _consume_message(self, channel, method, properties, body):
		result = self.message_received_callback(body)
		if result != False:
			channel.basic_ack(delivery_tag=method.delivery_tag)
		return body
	def _create_exchange(self, chan):
		''
		pass
#		exchange_options = self.config['exchangeOptions']
#		chan.exchange_declare(exchange=self.config['exchangeName'],
#								 exchange_type=self.config['exchangeType'],
#								 passive=exchange_options['passive'],
#								 durable=exchange_options['durable'],
#								 auto_delete=exchange_options['autoDelete'],
#								 internal=exchange_options['internal'])
	def _create_connection(self):
		params = self.config['connection']
		credentials = pika.PlainCredentials('guest', 'guest')
		parameters = pika.ConnectionParameters('localhost', credentials=credentials)

#		credentials = pika.PlainCredentials(self.config['userName'], self.config['password'])
#		parameters = pika.ConnectionParameters(self.config['host'], self.config['port'],
#											   self.config['virtualHost'], credentials, ssl=True)
		return pika.BlockingConnection(parameters)
	def _create_queue(self, chan, que):
		''
		chan.queue_declare(queue=que)
#		queue_options = self.config['queueOptions']
#		channel.queue_declare(queue=self.config['queueName'],
#							  passive=queue_options['passive'],
#							  durable=queue_options['durable'],
#							  exclusive=queue_options['exclusive'],
#							  auto_delete=queue_options['autoDelete'])
	def _create_vhost(self, vhost):
		''
		cmd = 'rabbitmqctl add_vhost <[vhost]>'
		ctrlr.engine().run(cmd)
		return self
	def _delete_channel(self, chan):
		''
		return self
	def _delete_exchange(self, exchange):
		''
		return self
	def _delete_vhost(self, vhost):
		''
		return self
	def _get_channels(self):
		''
		return self
	def _get_exchanges(self):
		''
		return self
	def _get_vhosts(self):
		''
		return self
#	def __enter__(self):
#		self.connection = self._create_connection()
#		return self
	def __exit__(self, *args):
		self.connection.close()
def connect():
	credentials = pika.PlainCredentials('guest','guest')
	parameters = pika.ConnectionParameters('192.168.1.106', '5672', '/',
											credentials, connection_attempts=5,
											retry_delay=1)
	conx = pika.BlockingConnection(parameters)
	return conx
def setupSystem():
	''
	conx = connect()
	channel = conx.channel()
	for exchange in exchanges:
		channel.exchange_declare(exchange=exch['name'],
									exchange_type=exch['type'])
	for queue in queues:
		channel.queue_declare(queue=queue['name'],
										routing_key=queue['key'])#		||
#==========================Source Materials=============================||
'''
https://pika.readthedocs.io/en/stable/modules/parameters.html
https://www.rabbitmq.com/vhosts.html
http://www.rabbitmq.com/devtools.html#devops-tools
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
'''
#============================:::DNA:::==================================||
'''
<(DNA)>:
	<@[datetime]@>:
		<[class]>:
			version: <[active:.version]>
			test:
			description: >
				<[description]>
			work:
				- <@[work_datetime]@>
	<[datetime]>:
		here:
			version: <[active:.version]>
			test:
			description: >
				<[description]>
			work:
				- <@[work_datetime]@>
'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
