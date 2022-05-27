'''
---
<(META)>:
	docid: <^[uuid]^>
	name:
	description: >
		Virtual machine linkage for controlling virtual box machines

		Run updates and cleanup on OS then make copies of settings
		send commands to the bash inside the VM? ssh?
		need to decide on best command logic for sending ssh commands several options found

		Save environmental settings for each vm with primary work scenarios for each environment
		Maintenance Level 0 will traverse all the user machines
		@MainST/ware/User_Drives and create corresponding dirs at MainST/data/VMIM and VMIM Substructure
		verify how to pass arguments with the Popen command

	version: 0.0.0.0.0.0
	expire: <^[expire]^>
	here: <[path]>
	outline:
	<(WT)>:
'''
# -*- coding: utf-8 -*-
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
from os.path import abspath, dirname, join
#===============================================================================||
from pheonix.elements.comm import comm#							||
from pheonix.elements.config import config#								||
from pheonix.elements.subtrix import subtrix
from pheonix.molecules.ctrlr.ossys import linux
#===============================================================================||
here = join(dirname(__file__),'')#												||
there = abspath(join('../../..'))#												||set path at pheonix level
version = '0.0.0.0.0.0'#														||
#===============================================================================||
class linkage(linux.linkage):
	'''Virtualbox Linkage creates connections to the virtualbox host and the
	 	guest operating systems in order to pe
		rform functions to and within
		a virtual machine and virtual harddisk'''
	def __init__(self, cfg=None, platform='linux', flavor='ubuntu'):
		'''Initialize linkage to virtualbox host'''
		pxcfg = '{0}z-data_/ossys.yaml'.format(here)
		self.platform, self.flavor = platform, flavor
		self.config = config.instruct(pxcfg).override(cfg)
#		print('Config', self.config.dikt)
		self.vmcfg = self.config.dikt['vbvm']['vbvm']
		self.cfg = self.config.dikt[platform][flavor]

		self.session = self.config.session
		self.ware_vrs = self.session.ppov['stores']['WAREvrs']
		linux.linkage.__init__(self, cfg)
	def backup(self):
		''' '''
		data = {}
		cmd = subtrix.mechanism(self.cfg['backup'], data).run()[0]
		self.run(cmd)
		return self
	def change_uuid(self, data):
		''' '''
		data = {'device_image': data}
		cmd = subtrix.mechanism(self.vmcfg['cmds']['change_uuid'], data).run()[0]
		outs = self.run(cmd)
		return outs
	def clone(self, frm, to):
		''' '''
		base = '<[WAREvrs]>/Bootables/Base_Drives/<[from_image]>.vdi'
		data = {'WAREvrs': self.ware_vrs, 'from_image': frm}
		base = subtrix.mechanism(base, data).run()[0]

		data = {'WAREvrs': self.ware_vrs, 'to_image': to}
		user = '<[WAREvrs]>/Bootables/Base_Drives/<[to_image]>.vdi'
		shutil.copyfile2(base,user)#											||
		cmd = self.config.dikt['cmds']['change_uuid']
		self.status = self.run(subtrix.mechanism(cmd, data).run()[0])

		return self
	def cremach(self, name):
		'''Create Virtual Box Virtual Machine Machine'''
		data = {}
		cmd = subtrix.mechanism(self.cfg['create_machine'], data).run()[0]
		self.run(cmd)
		return self
	def crehd(self):
		'''Create Virtual Box Virtual Machine Harddisk'''
		data = {}
		cmd = subtrix.mechanism(self.cfg['create_harddisk'], data).run()[0]
		self.run(cmd)
		return self
	def delete(self):
		'''Delete Virtual Box Virtual Machine Harddisk'''
		cmd = subtrix.mechanism(self.cfg['delete_harddisk'], data).run()[0]
		self.run(cmd)
		return self
	def install(self):
		'''Run commands to install programs on a virtual device'''
		cmd = subtrix.mechanism(self.cfg['install_apps'], data).run()[0]
		self.run(cmd)
		return self
	def list(self, path):
		'''List Virtual Machines Located at ware/UserDrives/_z/'''
		rdr = fonql.doc(path).filtr('.vdi').read()
		while True:
			self.drives = next(rdr, None)
			if self.drives == None:
				break
			yield self
		yield self
	def modify(self, data):
		''' '''
		cmd = subtrix.mechanism(self.cfg['modify'], data).run()[0]
		self.run(cmd)
		return self
	def monitor(self):
		''' '''
		pass
		#subprocess.Popen(['dpkg-query '+mp+'/VMIM/'+vm+'/Log/installed'+d4t3+'.log', -l)#				||verify how to pass arguments with the Popen command
		#VMs = mp+'/data/LOG/VDI.log'#
		#new_vm = 'VBOXManage clonevm STAN --name WORK'
		#subprocess.Popen(['bash',new_vm])#															||
		#subprocess.Popen(['bash','VBOXManage storageattach '])#
		#send commands to the bash inside the VM? ssh?
		#need to decide on best command logic for sending ssh commands several options found
	def sethd(self):
		cmd = subtrix.mechanism(self.cfg['register_harddisk'], data).run()[0]#||
		self.run(cmd)
		return self
	def start(self):
		''' '''
		cmd = subtrix.mechanism(self.cfg['start'], data).run()[0]#			||
		self.run(cmd)
		return self
	def update(self):
		''' '''
		cmd = subtrix.mechanism(self.cfg['update'], data).run()[0]#			||
		self.run(cmd)
		return self
