#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Nchantrs@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''  #																			||
---  #																			||
<(META)>:  #																	||
	docid:   #																	||
	name: Python Excecution Document  #				||
	description: >  #															||

	expirary: <[expiration]>  #													||
	version: <[version]>  #														||
	path: <[LEXIvrs]>  #														||
	outline: <[outline]>  #														||
	authority: document|this  #													||
	security: sec|lvl2  #														||
	<(WT)>: -32  #																||
''' #																			||
# -*- coding: utf-8 -*-#														||
#================================Core Modules===================================||
import time
from os.path import abspath, dirname, exists, join, expanduser
from sys import argv, exit
#===============================================================================||
import signing
from base64 import b64encode, b64decode
#===============================================================================||
from condor import condor
#===============================================================================||
here = join(dirname(__file__),'')#												||
there = abspath(join('../../..'))#												||set path at pheonix level
version = '0.0.0.0.0.0'#														||
log = True
#===============================================================================||
pxcfg = join(abspath(here), '_data_/crypt.yaml')

def encrypt(msg, public):
	''' '''
	encrypted = b64encode(rsa.encrypt(msg, public))

def exportKeys(public, pkey):
	''' '''
	print(pkey.exportKey('PEM'))
	print(public.exportKey('PEM'))

def decrypt(emsg, pkey):
	''' '''
	msg = rsa.decrypt(b64decode(emsg), pkey)
	return msg

def makeKeys(keysize=4096):
	''' '''
	(public, pkey) = rsa.newkeys(keysize)
	return public, pkey

def sign(msg, pkey):
	''' '''
	signature = b64encode(rsa.sign(msg, pkey, "SHA-512"))

def verify(msg, signature, public):
	''' '''
	verify = rsa.verify(msg, b64decode(signature), public)
