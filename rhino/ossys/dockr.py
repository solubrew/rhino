#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(META)>:
	docid: <^[uuid]^>
	Name:
	description: >
	expirary: <[expiration]>
	Version: <[Version]>
	authority: document|this
	security: seclvl2
	<(WT)>: -32
'''
# -*- coding: utf-8 -*-
#===============================================================================||
from __future__ import print_function
import psutil
from os.path import abspath, dirname, join
from os import chdir
from io import BytesIO
#===============================================================================||
import docker
#===============================================================================||
from condor import condor#								||
from subtrix import subtrix
from rhino.ossys import linux
#===============================================================================||
here = join(dirname(__file__),'')#						||
there = abspath(join('../../..'))#												||set path at pheonix level
wolfpack = f'{there}wolf/pack/bash'
log = True
#===============================================================================||
pxcfg = join(abspath(here), '_data_/ossys.yaml')#								||use default configuration
class linkage(linux.linkage, docker.DockerClient):
	'''Control Docker System Instances'''
	def __init__(self, cfg=None):
		self.config = condor.instruct(pxcfg).override(cfg).select('dockr')#		||load configuration file
		docker.DockerClient.__init__(self)
		linux.linkage.__init__(self, cfg)

	def load_commands(self):
		''' '''
		params = self.config.dikt['dockr']['cmds']#, wolfpack
		self.dockrCMDs = subtrix.mechanism(params).run()[0]
		return self

	def backup(self, service, active=False, service_name=None):
		'''Backup docker service and/or HVC EDN '''
		if active == True:
			if service_name == None:
				return False
			path = '<[DATAvrs]>/EDNs/HVCs/{0}'.format(service_name)
			fonql.backup(path)
		try:
			cmd = self.config.dikt['services'][service]['cmds']['dump']
			data = {}
			cmd = subtrix.mechanism(cmd, data).run()[0]
			status = self.run(cmd)#												||
		except Exception as e:
			cmd = self.config.dikt['services'][service]['cmds']['backup']
			data = {}
			cmd = subtrix.mechanism(cmd, data).run()[0]
			status = self.run(cmd)#												||
		return status

	def build(self, text):#														||
		'''Build a docker image from Dockerfile text Build docker image from
			dockerfile select build command from docker file '''
		cmd = calct.stuff(text).between('<{CLI:=>', '}>').it
		if 'docker build' == cmd[:len('docker build')]:
			status = self.bashr(cmd)#					||
			print('Status', status)
		return self

	def buildTree(self, path):
		''' '''
		rdr = fonql.doc(path).read()
		while True:
			fsTREE = next(rdr, None)
			if fsTREE == None:
				break
			paths = fsTREE.filtr('Dockerfile')
			for path in paths.paths:
				if 'Dockerfile' in path:
					print('Path', path)
					dir = calct.stuff(path).trimPast('/', 'exclude','end').it
					print('Dir', dir)
					chdir(dir)
					dockrFile = next(txtonql.doc(path).read()).text
					self.build(dockrFile)
		return

	def clean(self, what='all'):
		'''Remove unused or selected assets from the docer system including
		 	images, containers and volumes'''
		#self.info()
		# if what == 'images' or what == 'all':
		# 	self._cleanImages()
		# elif what == 'containers' or what == 'all':
		# 	self._cleanContainers()
		# elif what == 'volumes' or what == 'all':
		# 	self._cleanVolumes()
		# return self
		out = self.containers.prune()
		print('Containers', out)
		out = self.images.prune()
		print('Images', out)

	def delContainer(client, name):
		''' '''
		client.remove_container(name)

	def delImage(client, name):
		''' '''
		client.remove_image(name)

	def execute(self, machine, cmd):
		''' '''
		dcmd = self.config.dikt['dockr']['cmds']['execute']
		data = {'machine': machine, 'cmd': cmd}
		dcmd = subtrix.mechanism(dcmd, data).run()[0]
		self.linux.execute(dcmd)
		out = p.stdout.read()
		if p.wait() == -9:	# Happens on timeout
			# We have to kill the container since it still runs
			# detached from Popen and we need to remove it after because
			# --rm is not working on killed containers
			kill_and_remove(ctr_name)
		return out

	def getContainers(self, how=''):
		''' '''
		self.dcontainers = {'live': self.containers.list(all=False),
								'all': self.containers.list(all=True)}#	||
		return self

	def getImages(self):
		''' '''
		self.dimages = self.images.list()
		return self

	def hold_containers(self):
		''' '''
		self.hold = {'containers': []}
		self.hold['containers'].append([self.config['hold']['containers']])#	||
		if profile != None:
			self.hold['containers'].append([profile['hold']['containers']])#	||
		return self

	def hold_images(self):
		''' '''
		self.hold['images'] = []
		self.hold['images'].append([self.config['hold']['images']])#			||
		if profile != None:
			self.hold['images'].append([profile['hold']['images']])#			||
		return self

	def info(self):
		''' '''
		self.containers = self.client.containers.list()
		self.images = self.client.images.list()
		self.containers, self.images = {},{}
		results = {'containers': {'live': {'cmd': 'sudo docker ps', 'out': '',
					}, 'all': {'cmd': 'sudo docker ps -a', 'out': '',
					}, 'images': {'cmd': 'sudo docker images', 'out': '',}}}
		report = dvc.bashr(cmds)
		return self

	def kill(self):
		''' '''
		cmd = 'sudo docker rmi <[name]>:<[tag]>'
		cmd = tmplt.thing().run()
		linux.linkage().bashr(cmd)

	def kill_and_remove(self, ctr_name):
		''' '''
		for action in ('kill', 'rm'):
			p = Popen('docker %s %s' % (action, ctr_name), shell=False,
													stdout=PIPE, stderr=PIPE)#	||
			if p.wait() != 0: raise RuntimeError(p.stderr.read())

	def loadDOCKs(self, concern='all'):
		'''Load docker machines from kwown concerns'''
		if concern != 'all':
			self.session = ''

	def postgres(self, cmdn):
		''' '''
		app = self.config.dikt['services']['postgres']
		self.execute(app['cmds'][cmdn])
		return self

	def prune(self):
		client.containers.prune()
		client.images.prune()

	def run(self, image=None, name=None, depth=None):
		if name == None:
			name = namer.engine('random').it
		if depth == 'full':
			self.images(name, tag, path)
			cmd = 'docker run --rmi --name <[name]> <[image]>'
			link = linux.linkage().run(cmd)
			self.container['start']['out'] = link.stdout.read()
			self.container['start']['errors'] = link.stderr.read()
			self.container['status']['inspect'] = self.inspect()
		if p.wait() == -9:	# on timeout kill the container since it still runs
			# detached from Popen and we need to remove it after because --rm is not working on killed containers
			kill_and_remove(ctr_name)
		return out

	def savContainer():
		''' '''
		return

	def saveImage(self, image, tag, name=None, path=None):
		''' '''
		if path == None:
			path = self.config.dikt['images']['store']
		cmd = 'docker save <[image]>:<[tag]> --output <[path]>/<[name]>.tar'
		data = {'image': image, 'tag': tag, 'path': path, 'name': name}
		cmd = subtrix.mechanism(cmd, data).run()[0]
		return

	def saveImages(self, images=None):
		''' '''
		if images == None:
			images = self.client.images.list()
		for image in images:
			print('Image', image)
			self.saveImage(image, tag, name)

	def _cleanContainers(self):
		for container in self.containers['live']:
			if container not in self.hold['containers']:
				self.stop(container)
		for container in self.containers['all']:
			if container not in self.hold['containers']:
				delContainer(client, container)

	def _cleanImages(self):
		if log: print('Images', self.images.__dir__())
		for image in self.images['all']:
			if image not in self.hold['images']:
				delImage(client, image)

def backup_pgs_docker(rte):
	when = next(thing.when().gen())#					||
	dbn = rte['backup_pgs_docker']
	for db in povsesh.ppov['stores']['DBvrs'].keys():
		if dbn != None and dbn != db:
			continue
		path = '/home/solubrew/EDN/Documents/{0}/{1}.sql.gz'.format(when, db)
		status = fonql.touch(path)
		#need to build out usage of bear to control these variables and
		#compact this function into ossys.dockr/appsys.pgs
		#
		user = 'solubrew'
		hvc = 'postgres_lexi'
		if status != False:
			cmd = 'docker exec {0} pg_dump -U {1} {2} | gzip > {3}'.format(hvc, user, db, path)
			print('Backup', db)
			out = linux.linkage().run(cmd)
			print('Status', out)

def restore_pgs_docker(rte):
	when = rte['restore_pgs_docker']
	for db in povsesh.ppov['stores']['DBvrs'].keys():
#			out = dockr.linkage().run(('postgres','backup'))
		path = '/home/solubrew/EDN/Documents/{0}/{1}.sql.gz'.format(when, db)
		user = 'solubrew'
		hvc = 'postgres_lexi'
		print('unzip path',path)
#			path = path[:-3]
#			cmd = 'docker exec {0} gunzip -c {1} | psql dbname -U {2}'.format(hvc, path, user)
		cmd = 'docker exec {0} createdb -h localhost -p 5432 -U {1} {2}'.format(hvc, user, db)
		out = linux.linkage().run(cmd)
		print('Zip Status', out)
		cmd = 'gunzip -c {0} | docker exec -i {1} psql -U {2} {3}'.format(path, hvc, user, db)
		print('Restore', db)
		out = linux.linkage().run(cmd)
		print('Status', out)


#===============================Source Materials================================||
'''


import docker, sys
def build(image):
    if image == 'all':
        #load image files
        ''
    else:
        ''
        #need a way to lookup build file by image output name
        #scan folder and load a database
        #
def clean():
    client = docker.from_env()
    out = client.containers.prune()
    print('Containers', out)
    out = client.images.prune()
    print('Images', out)
def list():
    client = docker.from_env()
    containers = client.containers.list('all')
    print('Containers',containers)
    images = client.images.list()
    print('Images', images)
def scanFiles():
    ''
if __name__ == '__main__':
    if sys.argv[1] == 'clean':
        clean()
    elif sys.argv[1] == 'list':
        list()
    elif sys.argv[1] == 'build':
        build(sys.argv[2])



'''
#=================================:::DNA:::=====================================||
'''
<(DNA)>:
	administer:
		version: <[active:.version]>
		test:
		description: >
			<[description]>
		work:
	here:
		version: <[active:.version]>
		test:
		description: >
			<[description]>
		work:
'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
