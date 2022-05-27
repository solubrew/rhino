#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(META)>:
	DOCid: <^(UUID)^>
	name:
	description: >
	expirary: <^[expiration]^>
	version: <^[version]^>
	path:
	outline: <[outline]>
	authority: document|this
	security: sec|lvl2
	<(WT)>: -32
'''
# -*- coding: utf-8 -*-
#===============================================================================||
import os, datetime as dt, multiprocessing as mp, sys, hashlib#					||
#================================3rd Party Modules==============================||
import wormhole as wm
#===============================================================================||

#===============================================================================||
here = os.path.join(os.path.dirname(__file__),'')#								||
there = os.path.abspath(os.path.join('../../..'))#								||set path at pheonix level
#===============================================================================||
