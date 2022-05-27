'''
---
<(meta)>:
	DOCid: <^[uuid]^>
	name: Molecules Level Distributor Module Syncthing Extension Python Document
	description: >
	version: 0.0.0.0.0.0
	path: <[LEXIvrs]>/panda/LEXI/LEXI.yaml
	outline:
	authority: document|this
	security: seclvl2
	<(wt)>: -32
'''
# -*- coding: utf-8 -*-
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
import os, datetime as dt, shutil as sh
#===============================================================================||
from pheonix.comm import comm#											||
from condor import condor#										||
from pheonix.store.orgnql import fonql
from pheonix.ctrlr.ossys import linux
#===============================================================================||
tdy = dt.datetime.today()
here = os.path.join(os.path.dirname(__file__),'')
#===============================================================================||
class linkage(linux.linkage):
	''' '''
	def __init__(self, cfg=None):
		''' '''
		pxcfg = '{0}z-data_/distsys.yaml'.format(here)
		self.config = config.instruct(pxcfg).load()
#		self.f1l3 = config.xml
		# if sys == 'win':
		# 	self.path = ''' '''
		# elif sys == 'lin':
		# 	self.path = ''' '''
		linux.linkage.__init__(self, self.config)
	def addFolder():
		folder = pheonix.sync.syncthing.config().folder()
		f1l3 = getConfig()
		#find a an entry that is directly asceding adjscent and descending adjsent
		#then insert the new folder between these 2 entries
	def cleanup(self, fpaths):
		'''Move sync conflict files to a pile and compressing the pile'''
		filtrs = ['.sync-conflict', 'conflicted copy', 'Case Conflict']
		for fpath in fpaths.keys():
			tpath = fpaths[fpath]
			fonql.doc(fpath).setFilters(filtrs).move(tpath)
		for fpath in fpaths.keys():
			fonql.compress(fpaths[fpath])
		return self
	def setup(self):
		''' '''
		return self
	def start(self):
		''' '''
		return self
	def stop(self):
		''' '''
		return self
