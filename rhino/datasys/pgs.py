#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(meta)>:
	DOCid: <^[uuid]^>
	Name:
	description: >
	expirary: <[expiration]>
	Version: <[Version]>
	path: <[LEXIvrs]>panda/LEXI/
	outline: <[outline]>
	authority: document|this
	security: seclvl2
	<(wt)>: -32
'''
# -*- coding: utf-8 -*-
#===============================================================================||
from os.path import abspath, dirname, join
#===============================================================================||

#===============================================================================||
from pheonix.comm import comm#											||
from condor import condor#										||
from pheonix.ctrlr.ossys import linux
#===============================================================================||
here = join(dirname(__file__),'')#												||
there = abspath(join('../../..'))#												||set path at pheonix level
version = '0.0.0.0.0.0'#														||
#===============================================================================||

os_cmd = 'docker exec -i <[hvc]>'
connect_cmd = 'psql -U <[user]> <[db]>'
drop_cmd = 'echo "DROP TABLE <[scheme]>.<[table]> CASCADE" | <[os]> <[connect]>'

#===============================Source Materials================================||
'''
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
