#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''  #																			||
---  #																			||
<(META)>:  #																	||
	docid:   #						||
	name:  #					||
	description: >  #															||
		  #	||
	expirary: <[expiration]>  #													||
	version: <[version]>  #														||
	authority: document|this  #													||
	security: sec|lvl2  #														||
	<(WT)>: -32  #																||
''' #																			||
# -*- coding: utf-8 -*-#														||
#================================Core Modules===================================||
from os import walk#															||
from os.path import abspath, dirname, exists, join#								||
import yaml#																	||
try:#																			||
	import simplejson as json#													||
except:#																		||
	import json#																||
#================================Pheonix Modules================================||
from condor import condor, thing#										||
from excalc import text as calct, tree as calctr#							||
from squirl.objnql import imgonql#								||
from squirl.orgnql import monql, yonql#								||
from subtrix import subtrix#									||
#===============================================================================||
here = join(dirname(__file__),'')#												||
log = True
#===============================================================================||
pxcfg = join(abspath(here), '_data_', 'note.yaml')

class book(object):#															||s
	'''Office notebook creates a generic structure by which various
		popular notebook files can be created, edited and manipulated.
		below is an example:


		node0	#row0.column0.rod0										0.0.0
			node1	#row0.column1.rod0									0.1.0
				||	#
					0	#row0.column1.rod1								0.1.1
					1	#row0.column1.rod2								0.1.2
				node3	#row0.column2.rod0								0.2.0
						||
						0	#row0.column2.rod1							0.2.1
						1	#row1.column2.rod2							1.2.2
					node4	#row0.column3.rod0							0.3.0
						||
							0
					node7   #row1.column3.rod0							1.3.0
				node5  #row1.column2.rod0								1.2.0
					||
					node6	#row0.column3.rod0							0.3.0
						||
							0											0.3.1
							1											0.3.2
							2
			node2	#row1.column1.rod0									1.1.0
				||
					0  #sheet number									1.1.1
					1													1.1.2
					2													1.1.3
						full path - 0.0.0|1.1.0|1.1.3
					3
	'''#																		||
	def __init__(self, path, cfg=None):#										||
		pxcfg = f'{here}_data_/notebook.yaml'#						||
		if cfg == None:#														||
			tipe = 'pheonixNB'#													||
		elif 'type' in cfg.keys():#												||
			tipe = cfg['type']#													||
		self.tipe = tipe#														||
		self.config = config.instruct(pxcfg).override(cfg)#	||load configuration file
		self.doc = {'path': path}
	def collapse(self):#														||
		'''Recursively write data from the addressed row, col, rod, cell
				structure to a text structure for the given notebook type'''#	||
		for row, rowd in self.doc['addressed'].items():
			for col, cold in rowd.items():
				for rod, rodd in cold.items():
					for cell, celld in rodd.items():
						pass
		return self#															||
	def convert(self):
		'Convert file to pheonixNB or pheonix to various notebook files'

		return self
	def create(self, params):#			||
		''
		self.doc['UUID'] = thing.what().uuid().ruuid
		tipe = self.tipe
		self.doc['text'] = self.config.dikt[tipe]['TMPLT']['notebook']['tmplt']#	||
		self.createRod(params, self.doc)
		return self#													||
	def createCell(self, d, gTMPLT, tipe=None, uuid=None):#								||
		'Create a notebook cell of a core office notebook type'
		if tipe == None:
			tipe = self.tipe
		if tipe == 'cherrytreeNB':
			if uuid == None:#													||
				uuid = thing.what().uuid#										||
				lock = 1#														||
#need to allow for various types of cells
		ctipe = 'rich_text'
		cellTMPLT = self.config.dikt[tipe]['TMPLT']['cell'][ctipe]['tmplt']#	||
		dargs = self.config.dikt[tipe]['TMPLT']['cell'][ctipe]['dargs']
		args = calctr.stuff(dargs).merge(d).it
		return subtrix.mechanism(cellTMPLT, args).run()[0]
	def createCol(self, d, gTMPLT, tipe=None, uuid=None):
		''' Create notebook column if notebook format uses a column structure'''
		if tipe == None:
			tipe = self.tipe
		if tipe == 'cherrytreeNB':
			if uuid == None:#													||
				uuid = thing.what().uuid#										||
				lock = 1#														||
		colTMPLT = self.config.dikt[tipe]['TMPLT']['col']['tmplt']#			||
		dargs = self.config.dikt[tipe]['TMPLT']['col']['dargs']#			||Load template defaults
		if colTMPLT == None:
			self.doc['text'] = self.createCell(d, gTMPLT)
			return self
		if dargs != None:
			args = calctr.stuff(dargs).merge(d).it#								||Merge instance configurations
		colTMPLT = subtrix.mechanism(colTMPLT, args).run()[0]#still broken?
		for cell in x:
			self.doc['text'] = self.createCell(d, colTMPLT)
		return self
	def createRod(self, d, gTMPLT, tipe=None, uuid=None):
		'''Creating a rod adds an additional sheet to the notebook'''
		if tipe == None:
			tipe = self.tipe
		if uuid == None:#													||
			uuid = {'uuid': thing.what().uuid}#									||
		rodTMPLT = self.config.dikt[self.tipe]['TMPLT']['rod']['tmplt']#			||
		t = {'rod': rodTMPLT}
		dargs = self.config.dikt[tipe]['TMPLT']['rod']['dargs']
		args = calctr.stuff(dargs).merge(d).merge(t).it
		if rodTMPLT == None:
			self.doc['text'] = self.createRow(d, gTMPLT)
			return self
		rodTMPLT = subtrix.mechanism(rodTMPLT, args).run()[0]
		for rod in x:
			self.doc['text'] = self.createRow(args, rodTMPLT)
		return self
	def createRow(self, d, gTMPLT, tipe=None, uuid=None):
		'''Creating a row adds an additional row to a sheet'''
		if tipe == None:
			tipe = self.tipe
		if tipe == 'cherrytreeNB':
			if uuid == None:#													||
				uuid = thing.what().uuid#										||
				lock = 1#														||
		rowTMPLT = self.config.dikt[tipe]['TMPLT']['row']['tmplt']#				||
		dargs = self.config.dikt[tipe]['TMPLT']['row']['dargs']
		args = calctr.stuff(dargs).merge(d).it
		for row in x:
			self.doc['text'] = self.createCol(d, rowTMPLT)
		return self
	def edit(self, d):#													||
		'''Edit given notebook with given data, data structure should contain
			a dictionary with {'notebook': {'rod': {'row': {'col': {
															'cell': {}}}}}'''#	||
		self.read()
		self.doc['dikt'] = calctr.stuff(self.doc['dikt']).merge(d).it
		return self#													||
	def read(self, nbTYPE='PheonixNB'):
		''
		if nbTYPE == 'CherrytreeNB':
			self.readCherrytreeNB()
		elif nbTYPE == 'JupyterNB':
			self.readJupyterNB()
		elif nbTYPE == 'PheonixNB':
			self.readPheonixNB()
		return self
	def readCherrytreeNB(self):
		'Read Cherrytree Notebook file'
		kind = {'orgnql': {'code': 'XML'}}
		self.doc['obj'] = next(monql.doc(path, kind).read())
		self.doc['text'] = self.doc['obj'].text
		self.doc['dikt'] = self.doc['obj'].dikt
		return self
	def readJupyterNB(self):
		'Read Jupyter Notebook file'
		kind = {'orgnql': {'code': 'JSON'}}
		self.doc['obj'] = next(yonql.doc(path, kind).read())
		self.doc['text'] = self.doc['obj'].text
		self.doc['dikt'] = self.doc['obj'].dikt
		return self
	def readPheonixNB(self):
		'Read Pheonix Notebook file'
		kind = {'orgnql': {'code': 'YAML'}}
		self.doc['obj'] = next(yonql.doc(path, kind).read())
		self.doc['text'] = self.doc['obj'].text
		self.doc['dikt'] = self.doc['obj'].dikt
		return self
	def sanitize(self, content):#												||
		if self.config['sanitizie'] == None:
			return content
		for k,v in self.config.dikt[self.tipe]['sanitize'].items():
			content = content.replace(k,v)
		return content#															||
	def write(self, d, nb='pheonixNB'):
		'Write Notebook to given file type'
		if exists(self.doc['path']):
			self.edit(d)
		else:
			self.create(d)

		#need to run a conversion from the internal notebook datastructure to the selected output
		#not all structures are compatible
		#a jupyter notebook converts to cherrytree ish...not sure about totallity of outputs
		#a cherrytree notebook converts to jupyternotebook....requires very detailed conversions for tables, images and such
		#a pheonix notebook can store the data from either but rendering is a different store
		#internally the system is going to use PheonixNB
		#
		monql.doc(self.doc['path']).write(self.doc['text'])


class cherryNBWriter(object):
	''' '''

	def __init__(self, name, path, opath, cfg=None):
		''' '''
		self.config = condor.instruct(pxcfg).select('cherrytreeNB')
		self.config.override(cfg)
		self.imagelist = self.config.dikt['imageLIST']
		self.textlist = self.config.dikt['textLIST']
		self.depth_lock = 0
		self.lang = calctr.stuff(self.textlist).insideOut().it
		self.img = calctr.stuff(self.imagelist).insideOut().it
		DOC = self.builder(path, name)
		self.writeFile(name, opath, DOC)

	def disposition(self, f1l3, action):
		''' '''
		if action == 'Kill':#Kill will move the file to a grave and let the life maintenace system take over the handling of the file
			grave = f'{mps}/History/{tdy}'
#			if not os.path.exists(grave):
#				os.makedirs(grave)
#			shutil.move(f1l3,grave)
#			return
		elif action == 'Desenegrate':#desenegrate removes the file and all copies of it from the system
			shutil.remove(f1l3)
			return
		elif action == 'Hold':#holds the file in its current position
			return
		elif action == 'Relocate':#move the file to a new sturctured home
			shutil.copyfile2(f1l3,action['home'])
			return



	def top_node(self, node, name, content):#
		''' '''
		tabs = ''#
		for i in range(node['depth']+2):#
			f'{tabs}\t'#
		name = sanitize(name)
		DOC = f'{tabs}<node name="{name}" '#									||
		DOC += 'prog_lang="{0}" readonly="False" '.format(node['lang'])#		||this formatting required
		DOC += 'tags="" unique_id="{0}">\n'.format(str(node['nid']))#			||
		DOC = f'{DOC}{tabs}\t<rich_text>\n{content}\n{tabs}\t</rich_text>\n'#	||
		return DOC

	def end_node(self, node, name):
		''' '''
		tabs = ''
		for i in range(node['depth']+2):
			f'{tabs}\t'
		return (f'{tabs}</node>\n')

	def builder(self, path, name):
		''' '''
		f1l3_5ub5y5t3m = walk(path,topdown=True,
									onerror=None,followlinks=False)#	||
		DOC = '<?xml version="1.0" ?>\n\t<cherrytree>\n'
		depth, ncnt, oldp4th = 0, 0, {}
		oldp4th[0] = ''
		for p4th, d1r5, f1l35 in f1l3_5ub5y5t3m:
			if ncnt >= self.depth_lock and self.depth_lock != 0:
				break
			ncnt += 1
			curd1r = p4th[len(p4th[:p4th.rfind('/')])+1:]
			if oldp4th[depth] in p4th:
				options = {'lang': self.lang['.txt'],'nid':ncnt,'depth':depth}
				content = ''
				DOC += self.top_node(options,curd1r,content)
			else:
				lock = 1
				while lock == 1:
					depth += -1
					options = {'depth':depth}
					DOC += self.end_node(options,curd1r)
					if oldp4th[depth] in p4th:
						lock = 0
				options = {'lang': self.lang['.txt'],'nid':ncnt,'depth':depth}
				content = ''
				DOC += self.top_node(options,curd1r,content)
			depth += 1
			oldp4th[depth] = p4th
			for f1l3 in f1l35:
				ext = f1l3[len(p4th[:f1l3.rfind('.')]):]
				if self.config.dikt['content'] == True:
					content = ''
					if ext.lower() in self.img:
						try:
							content = encodeImage(p4th, f1l3, content, ext)
						except Exception as e:
							content = f'{path}/{f1l3}'
					elif ext.lower() in self.lang.keys():
						content = encodeText(p4th, f1l3)
						if not content:
							content, ext = '', '.txt'
							self.disposition(f'{p4th}/{f1l3}','Hold')
					else:
						ext = '.txt'
					ncnt += 1
				options = {'lang': self.lang[ext.lower()], 'nid': ncnt,
																'depth': depth}
				DOC += self.top_node(options, f1l3, content)
				content, options = '', {'depth':depth}
				DOC += self.end_node(options,f1l3)
		if log: print('Close Doc')
		while depth > 0:
			depth += -1
			DOC += self.end_node({'depth':depth}, '')
		return f'{DOC}\t</cherrytree>\n'

	def writeFile(self, name, opath, DOC):
		opath += f'/{name}.ctd'
		with open(opath,'w') as tr33:
			tr33.write(DOC)
		tr33.closed

def encodeText(path, phile):
	''' '''
	content = ''
	try:
		with open(f'{path}/{phile}','r') as doc:
			content = sanitize(doc.read())+'\n'
		doc.closed
	except Exception as e:
		print('Open Content Failed', e)
		return False
	return content

def encodeImage(path, phile, content, ext):
	''' '''
	b64 = imgonql.doc(f'{p4th}/{f1l3}')
	if ext != '.png':
		b64.convert(ext)
	img = str(b64.encode().resize(800).it.decode('utf-8'))
	content = '\t</rich_text>\n<encoded_png char_offset="0">'
	return f'{content}{img}</encoded_png>\t<rich_text>\n'

def sanitize(content):#
	''' '''
	content = calct.stuff(content).removeBlankLines().it
	content = content.replace('&','&amp;')#
	content = content.replace('<','&lt;')#
	content = content.replace('>','&gt;')#
	content = content.replace('"','&quot;')#
	return content#

#==============================Source Materials=================================||
'''

'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
