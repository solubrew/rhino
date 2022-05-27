'''
meta:
	DOCid: <^[uuid]^>
	name:
	description: >
	version: 0.0.0.0.0.0
	here: <^[here]^>
	outline:
'''
# -*- coding: utf-8 -*-
#@@@@@@@@@@@@Pheonix.Organelle.Ctrlr.Apctrlr.Veracrypt.Veracrypt@@@@@@@@||
from os.path import abspath, dirname, join
import datetime as dt, subprocess as sbp
#=======================================================================||
from pheonix.elements.comm import comm#							||
from pheonix.elements.config import config#								||
from pheonix.molecules.ctrlr.ossys import linux
#================Common Globals=========================================||
here = join(dirname(__file__),'')#						||
there = abspath(join('../../..'))#						||set path at pheonix level
version = '0.0.0.0.0.0'#												||
#=======================================================================||
class linkage(linux.linkage):
	''' '''
	def __init__(self, volume, loc, word=None):
		''' '''
		pxcfg = '{0}z-data/secsys.yaml'.format(here)
		self.config = config.instruct(pxcfg).load()
		self.volume = volume
		self.mount = loc
		self.word = word
		linux.linkage.__init__(self, self.config)
	def login(self, word=None):
		''' '''
		if word == None:
			word = self.word
		cmd = 'veracrypt -t -v --pim=0 -k="" --protect-hidden=no {0} {1} -p "{2}"'#
		cmd = cmd.format(self.volume, self.mount, word)#
		self.run(cmd)
		return self
	def create(self):
		''' '''
		return self
	def decrypt(self):
		''' '''
		cmd = self.config.dikt['cmds']['decrypt']
		self.run(cmd)
		return self
	def encrypt(self):
		''' '''
		return self
#==========================Source Materials=============================||
#============================:::DNA:::==================================||
'''
---
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
