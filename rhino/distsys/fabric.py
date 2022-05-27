#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(META)>:
	DOCid: <^[uuid]^>
	name:
	description: >
	expirary: <[expiration]>
	version: <[version]>
	path: <[LEXIvrs]>
	outline: <[outline]>
	authority: document|this
	security: sec|lvl2
	<(WT)>: -32
'''
# -*- coding: utf-8 -*-
#===============================================================================||

import os, pandas as pd, datetime as dt, logging as log
#from fabric import Connection
#from fabric.api import local, run, sudo, env, prompt, settings, cd, parallel, execute
#from fabric.contrib.files import exists
#from fabric.decorators import hosts, roles, runs_once
import json

import logging
import pheonix
#=======================================================================||
import pheonix
#=======================================================================||
here = os.path.join(os.path.dirname(__file__),'')#						||
version = '0.0.0.0.0.0'#												||
#use rules to load devices for control
# log.getLogger('').setLevel(log.INFO)
# logger = log.getLogger(__name__)
# here = os.path.join(os.path.dirname(__file__),'')

#=======================================================================||
#
# env.forward_agent = True
#
# env.user = 'username'
#
# role_list = (
# 	'aptmirror',
# 	'flask',
#  	'drupal',
# 	'cache',
# 	'db',
# 	'celery',
# 	'syncthing',
# 	'rabbitmq',
# )
#
# host_dict = {
# 	'192.168.1.131': ('aptmirror', 'syncthing',),
# 	#'100.100.100.101': ('db', 'celery',),
# }
#
# env.hosts = host_dict.keys()
#
# for r in role_list:
# 	env.roledefs[r] = []
#
# for k_host, v_roles in host_dict.items():
# 	for v_role in v_roles:
# 		env.roledefs[v_role].append(k_host)

# log.getLogger('').setLevel(log.INFO)
# logger = log.getLogger(__name__)
# here = os.path.join(os.path.dirname(__file__),'')
#
# conx = Connection(host='192.168.1.106', user='solubrew', port=22)
#
# conx.run('ls /home/solubrew')
#
# conx.run('sudo docker ps', pty=True)
# import getpass
# from fabric import Connection, Config
# sudo_pass = getpass.getpass("What's your user password?\n")
# config = Config(overrides={'user': '<host-user>', 'connect_kwargs': {'password': sudo_pass}})
# c = Connection('<host-ip>', config=config)
# c.run('uname -s')
#
# env.forward_agent = True
# env.user = 'username'
# role_list = ('aptmirror', 'flask', 'drupal', 'cache', 'db', 'celery',
# 				'syncthing', 'rabbitmq',)
# host_dict = {'100.100.100.100': ('web', 'cache',),
# 				'100.100.100.101': ('db', 'celery',),
# 				'192.168.1.131': ('aptmirror', 'syncthing',),
# 				'100.100.100.101': ('db', 'celery',),}
# env.hosts = host_dict.keys()
# for r in role_list:
# 	env.roledefs[r] = []
# for k_host, v_roles in host_dict.items():
# 	for v_role in v_roles:
# 		env.roledefs[v_role].append(k_host)
# env.password = ""
# class mainst:
# 	def __init__(self):
# 		self.host = '192.168.1.131'
# 		self.user = "joe"
# class maindt:
# 	def __init__(self):
# 		self.host = '127.0.0.1'
# 		self.user = "solubrew"
# env.forward_agent = True
# env.user = 'username'
# env.hosts = host_dict.keys()
# @task
# def update(device):
# 	env.hosts = device.host
# 	env.user = device.user
# 	sudo("apt get update")
# 	sudo("apt get upgrade")
# 	sudo("apt get update")
# 	sudo("apt get dist-update")
# 	sudo("apt get update")
# 	sudo("apt autoremove")
# @task
# def install(app):
# 	sudo("apt get update")
# 	cmd = "apt get install <[app]>".replace(app, '<[app]>')
# 	sudo(cmd)
# @task
# def uptime():
# 	local('uptime')
# 	run('uptime')
# @task
# def mirror():
# #	env.hosts = mainst().host
# 	env.hosts = ['192.168.1.131',]
# 	env.user = mainst().user
# 	sudo('rm /media/ware/Packagables/UbuntuPkgs/AptMirror/var/apt-mirror.lock')
# 	run('apt-mirror')
# def backup():
# 	pass
# 	#create a task to backup file scripts

# """
# logging.getLogger('').setLevel(logging.INFO)
# logger = logging.getLogger(__name__)
#
# env.forward_agent = True
# env.user = 'username'
# role_list = (
# 	'aptmirror',
# 	'flask',
#  	'drupal',
# 	'cache',
# 	'db',
# 	'celery',
# 	'syncthing',
# 	'rabbitmq',
# )
# host_dict = {
# 	'100.100.100.100': ('web', 'cache',),
# 	'100.100.100.101': ('db', 'celery',),
# 	'192.168.1.131': ('aptmirror', 'syncthing',),
# 	#'100.100.100.101': ('db', 'celery',),
# #}
# env.hosts = host_dict.keys()
# for r in role_list:
# 	env.roledefs[r] = []
# for k_host, v_roles in host_dict.items():
# 	for v_role in v_roles:
# 		env.roledefs[v_role].append(k_host)
# #env.password = ""
# """
# class mainst:
# 	def __init__(self):
# 		self.host = '192.168.1.131'
# 		self.user = "joe"
#
# class maindt:
# 	def __init__(self):
# 		self.host = '127.0.0.1'
# 		self.user = "solubrew"
#
#
#
#
#
#
#
#
# class mainst:
# 	def __init__(self):
# 		self.host = '192.168.1.131'
# 		self.user = "joe"
#
# class maindt:
# 	def __init__(self):
# 		self.host = '127.0.0.1'
# 		self.user = "solubrew"
#
# @task
# def update(device):
# 	env.hosts = device.host
# 	env.user = device.user
# 	sudo("apt get update")
# 	sudo("apt get upgrade")
# 	sudo("apt get update")
# 	sudo("apt get dist-update")
# 	sudo("apt get update")
# 	sudo("apt autoremove")
#
# @task
# def install(app):
# 	sudo("apt get update")
# 	cmd = "apt get install <[app]>".replace(app, '<[app]>')
# 	sudo(cmd)
#
# @task
# def uptime():
# 	local('uptime')
# 	run('uptime')
#
#
# @task
# def mirror():
# #	env.hosts = mainst().host
# 	env.hosts = ['192.168.1.131',]
# 	env.user = mainst().user
# 	sudo('rm /media/ware/Packagables/UbuntuPkgs/AptMirror/var/apt-mirror.lock')
# 	run('apt-mirror')
#
#
#
# def backup():
# 	pass
# 	#create a task to backup file scripts
