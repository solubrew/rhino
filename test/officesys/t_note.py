#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(meta)>:
	docid: ''
	name:
	description: >
	expirary: <[expiration]>
	version: <[version]>
	authority: document|this
	security: seclvl2
	<(wt)>: -32
'''
# -*- coding: utf-8 -*-
#===============================================================================||
#===============================================================================||
from os.path import abspath, dirname, join
from sys import argv
import datetime as dt, time#					||
#===============================================================================||
import crow
#===============================================================================||
from condor import condor, thing#										||
from fxsquirl import collector
#===============================================================================||
from rhino.officesys import note
#===============================================================================||
here = join(dirname(__file__),'')#												||
log = True
#===============================================================================||

def run(args):
	''' '''
	t_cherryNBWriter()

def t_cherryNBWriter():
	''' '''
	name = 'node-javascript-ecommerce-master'
	path = ''
	opath = ''
	nb = note.cherryNBWriter(name, path, opath)

if __name__ == '__main__':
	''' '''
	run(argv)


#===========================Code Source Examples================================||
'''
'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
