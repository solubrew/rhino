#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TIGR Metrics@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''  #																	||
---  #																	||
<(META)>:  #															||
	DOCid:   #						||
	name:  #					||
	description: >  #													||
		  #	||
	expirary: <[expiration]>  #											||
	version: <[version]>  #												||
	path: <[LEXIvrs]>  #												||
	outline: <[outline]>  #												||
	authority: document|this  #											||
	security: sec|lvl2  #												||
	<(WT)>: -32  #														||
''' #																	||
# -*- coding: utf-8 -*-#												||
#===========================Core Modules================================||
from os.path import abspath, dirname, join
import os, simplejson as json, yaml
#===========================3rd Party Modules===========================||
import PyPDF2 as pdf
#============================Pheonix Modules============================||
from pheonix.calcgen import text as calct
from pheonix.calcgen import tree as calctr
from condor import condor#								||
from pheonix.comm import log#									||
from pheonix.rule import rule#									||
from pheonix.thing import thing#								||
from pheonix.store.objnql import imgonql#						||
from pheonix.store.orgnql import yonql#						||
#=======================================================================||
here = join(dirname(__file__),'')#						||
there = abspath(join('../../..'))#						||set path at pheonix level
version = '0.0.0.0.0.0'#												||
#=======================================================================||
class book(object):#														||
	def __init__(self, path):#											||
		''' '''#							||
		if self.tipe == 'pdfdoc':#										||
			self.pdfOBJ = open(path, 'rb')#								||
	def create(self, params):#							||
		''' '''
		return self
	def read(self)#							||
		''
		cfgNB = self.config.select(tipe).dikt#							||load configuration file
		if tipe == 'pdfdoc':#											||
			tmplt = json.loads(cfgNB['notebook']['tmplt'])#				||
			self.text = self.pdfOBJ#							||
		elif tipe == 'richtextdoc':#									||
			tmplt = yaml.load(cfgNB['notebook']['tmplt'])#				||
		elif tipe == 'simpmletextdoc':#							||
			tmplt = {}#							||
		self.text = self.pdfOBJ.extractText()#							||
		return self
	def combine(self):
		''' '''
		return self
#==========================Source Materials=============================||
'''
https://automatetheboringstuff.com/chapter13/
'''
#============================:::DNA:::==================================||
#<(DNA)>:
#	administer:
#		version: <[active:.version]>
#		test:
#		description: >
#			Administrate Tests of the Tmplt Classes
#		work:
#	here:
#		version: <[active:.version]>
#		test:
#		description: >
#			Test Each Tmplt Class
#		work:
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
