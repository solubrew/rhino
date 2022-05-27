#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(META)>:
	DOCid: <^[uuid]^>
	name:
	description: >
		World bridger anipulates and controls e and accounts outside
		Mid level interaction with Linux and Windows
		as well as control of VMs, HVCs, VPSs, PBs,
		via distribution of skrps and direct connection
		using fabric, syncthing, ssh,
		A vein is a data deposit that can be mined
		initiate trade with bot
		select card and retrieve pricing
		store new observation
		analyze updated pricing
		set new values in catalog
		evalute inventory
		retrieve screen data through opencv and text
		recognition software

	expirary: <[expiration]>
	version: <[version]>
	path: <[LEXIvrs]>
	authority: document|this
	security: sec|lvl2
	<(WT)>: -32
'''
# -*- coding: utf-8 -*-
#===============================================================================||
from os.path import abspath, dirname, exists, join
from os import chdir, getcwd
import subprocess as sbp, os, socket
#===============================================================================||
import pprint as pp
#===============================================================================||
from condor import condor, thing
from excalc import text as calct
from fxsquirl.orgnql import fonql
#===============================================================================||
here = join(dirname(__file__),'')#						||
there = abspath(join('../../..'))#						||set path at pheonix level
version = '0.0.0.0.0.0'#												||
log = True
#===============================================================================||
pxcfg = join(abspath(here), '_data_/ossys.yaml')
class linkage(object):
	def __init__(self, cfg=None):
		self.config = condor.instruct(pxcfg).select('linux').override(cfg)
		self.config.dikt = self.config.dikt['ubuntu']
		#self.ip = thing.where().ip
		self.working_dir = here
		self.python_env_path = None

	def addPkgs(self):
		return self

	def alll(self):
		sb.subprocess('apt-get upgrade')
		sb.subprocess('pip upgrade --all && y')

	def bashr(self, cmd, hold=True, toSECs=10000):
		''' '''
		print('CMD', cmd)
		cwd = self.working_dir
		self.outs = None
		if self.python_env_path != None:
			cmd = f'source {self.python_env_path}; {cmd}'
		process = sbp.Popen( "/bin/bash", shell=False, universal_newlines=True,#||
									cwd=cwd, stdin=sbp.PIPE, stdout=sbp.PIPE,#	||
									stderr=sbp.PIPE)#							||
		if hold == True:
			self.outs = process.communicate(cmd, timeout=toSECs)
		pp.pprint(['OUTs', self.outs])
		self.lastprocess = process
		return self

	def cd(self, path):
		''' '''
		return self.set_working_directory(path)

	def clean(self, prcs):
		'kill all processes created by the given cmd'
		cmd = f'killall {prcs}'
		return self.bashr(cmd)

	def clientr(self):
		''
		return self

	def channels(self):
		return self

	def check(self):
		self.text = sb.subprocess('apt-get update').output
		self.text.append('\n'+30*'@')
		self.text.append(sb.subprocess('pip upgrade --all'))
		store.stuff('update.log').write(self.text).text

	def checkPort(self, ip, port):
		'''https://www.adamsmith.haus/python/answers/how-to-check-if-a-network-port-is-open-in-python'''
		ip = '127.0.0.1'
		port = 8545
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.connect((ip, int(port)))
			s.shutdown(2)
			if log: print(True)
			return True
		except Exception as e:
			if log: print(False, e)
			return False

	def connect(self, ip, port=22):
		if ip == self.ip:
			self.ip = '127.0.0.1'
		self.conx = Connection(host=ip, user=self.user, port=port)
		return self

	def cpDir(self, path, to):
		''' '''
		cmd = subtrix.instruct(self.config.dikt['create_machine'],
																data).run()[0]
		self.bashr(cmd)
		return self

	def creDir(self, path):
		''' '''
		cmd = f'mkdir {path}'
		return self.bashr(cmd)

	def creFile(self, path):
		''
		cmd = f'touch {path}'
		return self.bashr(cmd)

	def delDir(self, path):
		cmd = f'rm -R {path}'
		return self.bashr(cmd)

	def delFile(self, path):
		cmd = f'rm {path}'
		return self.bashr(cmd)

	def getStatus(self):
		pass
		#read all EDNs
		#ping all Devices
		#check all syncthing connections last updates

	def inspect(self):
		return self

	def monitr(self):
		''
		listen = True
		while listen == True:
			self.getNext()

	def mvDir(self, path, to):
		cmd = f'mv {path} {to}'
		return self.bashr(cmd)

	def mvFile(self, path):
		cmd = f'mv {path} {to}'
		return self.bashr(cmd)

	def ping(self, ip):
		cmd = ["/bin/ping", "-c", "1", ip]
		resp = str(sbp.Popen(cmd, stdout=sbp.PIPE).stdout.read())
		s, e = '+1 errors, ', ' packet loss,'
		if s in resp:
			print('Errors found')
			loss = calct.stuff(resp).findPattern(s, e).pattern
		else:
			s = '1 received, '
			loss = calct.stuff(resp).findPattern(s, e).pattern
		if loss == '0%':
			return True
		elif loss == '100%':
			return False
		else:
			return None

	def pythr(self, cmd, name='delta'):
		'''Run python command in the given virtual environment '''
		print('CMD', cmd)
		self.set_python_environment(name)
		outs = self.bashr(f'python {cmd}')
		return outs

	def reboot(self, ip):
		print('Not sure how best to handle a reboot over LAN')

	def rmvPkgs(self):
		''
		return self

	def scanr(self):
		''
		for worker, skills in self.workerls.items():
			self.rprts = self.skills['rprts']
			self.group = self.ctrlservr['group']
			p4th = self.group['path']
		return self

	def set_working_directory(self, path):
		'''Set working directory'''
		if not exists(path):
			fonql.touch(f'{path}/')
		self.working_dir = path
		chdir(self.working_dir)
		return self

	def set_python_environment(self, name):
		'''Set python execution environment'''
		print('Config', self.config.dikt)
		envs = self.config.dikt['python']['environments']['path']
		self.python_env = name
		self.python_env_path = f'{envs}/{name}/bin/activate'
		return self

	def sshr(self):
		#try to integrate fabric for this
		#decide between remote distribution and remote interaction
		#decentralization decisions
		return self

	def stopr(self, name=None):
		''
		if name == None:
			return self
		pidskrp = 'pids=$(pgrep '+name#					||
		pids = sbp.subprocess(pidskrp)#					||
		killskrp = 'kill -9 $pids'#						||
		sb.subprocess(skrp)#							||
		return self

	def sudor(self, cmd, endoffile, pword=None, prompt="Enter Password"):#
		''
		if pword == None:#												||
			import getpass#												||
			pword = getpass.getpass(prompt)#							||
		child = pexpect.spawn(cmd)#										||
		child.expect([endoffile, pexpect.EOF])#							||
		child.sendline(pword)#											||
		child.expect(pexpect.EOF)#										||
		child.close()#													||


def sync(frm, to):
	''' '''
	linkage().bashr(f'rsync -avz {frm} {to}')


#==============================Source Materials=================================||
'''

'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
