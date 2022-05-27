#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(META)>:
	DOCid: 6945e62a-d3cd-43fd-bfaf-e4801fdb859b
	name:
	description: >
	expirary: <[expiration]>
	Version: <[Version]>
	path: <[LEXIvrs]>panda/LEXI/
	outline: <[outline]>
	authority: document|this
	security: sec|lvl2
	<(WT)>: -32
'''
# -*- coding: utf-8 -*-
#=======================================================================||
from subprocess import Popen, PIPE#										||
from importlib import import_module#									||
import psutil, datetime as dt, shutil, os, pandas as pd, copy, time#	||
#=======================================================================||
from pheonix.elements.calcgen import text as calct
from pheonix.elements.comm import comm
from pheonix.elements.config import config#								||
from pheonix.elements.thing import thing#								||
from pheonix.molecules.tmapr import tmapr#								||
#=======================================================================||
here = os.path.join(os.path.dirname(__file__),'')#						||
there = os.path.abspath(os.path.join('../../..'))#						||set path at pheonix level
version = '0.0.0.0.0.0'#												||
#=======================================================================||
class engine(object):#
	''
	def __init__(self, name, cfg=None):#
		pxcfg = here+'z-data_/linux.yaml'#								||use default configuration
		self.config = config.instruct(pxcfg).load().override(cfg).dikt#	||load configuration file
	def createCMD(self, cmd):
		''
		app = 'python'
		env = 'GUI'

		process = sbp.Popen( "/bin/bash", shell=False,#					||
							universal_newlines=True, stdin=sbp.PIPE,#	||
									stdout=sbp.PIPE, stderr=sbp.PIPE)#	||
		cmds = ('source activate '+env+' \n '+app+' '+cmd+'\n')#			||verify how to pass arguments with the Popen command
		self.stdout = process.communicate(cmds)
		return self
	def executeCMD(self):
		''
		return self
	def run(self, cmd):
		self.createCMD()
		self.executeCMD()
	def setupCtrlr(self, tipe='python'):
		if tipe == 'python':
			pass
		elif tipe == 'bash':
			pass



class planner:#															||
	'Outline and Manage Events'#										||
	version='0.0.0.0.0.0'#												||
	def __init__(self, name, options=None):#							||
		self.name = name
		if options != None:
			self._parse(options)
		self.rsrcs = None
	def _parse(self, opts):
		self.tbox = tbox.build(opts['start']).genSeq(opts['end'])
		return self
	def scale(self):#
		'blur the scale of event interest....total of 3 levels of timeboxes'
		return self
	def assignResources(self, rsrc='group'):
		'''Add things like build, table, computer, food etc
		Attention is to control the needs of the event...relates to the
		ability of the event run in parallel and the amount of the
		focus resource needed'''
		return self
	def check(self, tmplt=None):
		''
		if tmplt == None:
			tmplt = cfg['tmplt']
		return self
	def period(self, strt, stop, config=None):
		if config == None:
			config = here+'zz_data/config.json'
		self.config = objnql.document(config).read().dikt
		self.strt = strt
		self.stop = stop
		given_period = datediff(stop-strt)
		if given_period > self.config['max']:
			raise('Time Period given violates config size maximum')
		now = dt.datetime.now()
		if self.config['interpertation'] == 'common':
			minute = self.getMin(self.strt)#convert start to number of minutes
			if minute > self.config['increment']:#
				self.zeroMin(self.strt)#
			else:
				self.zeroMin(self.strt, self.config['increment'])
	def getMin(self):
		return self
	def zeroMin(self):
		return self
	def byDate(self, splits, on=None):
		if isinstance(on, dict):
			formats = on
			on = list(on.keys())
		self.ton, non, self.frame = [], [], {}
		if on == None:
			self._findDateCols()
		elif isinstance(on, list):
			pass
		for i in on:
			self._binDate(splits, i)
		for i in self.ton:#set columns for recursive indexing
			non.append(list(self.data.columns).index(i))#append the index of the selected column
		self.recurdexer(non)
		return self
	def _binDate(self, splits, i):
		nframe = calcts.stuff(self.data[i]).bins(splits).frame#			||
		nframe.columns = [i, 'bin'+i, 'binnum'+i]
		self.ton.append('binnum'+i)
		self.data = pd.concat([self.data, nframe], axis=1)
		return self#									||
def GetDiskFreeSpaceEx_errcheck(result, func, args):
	if not result:
		raise ctypes.WinError()
	return args[1].value, args[2].value, args[3].value
def runGDFSE(self):
	GetDiskFreeSpaceEx.errcheck = GetDiskFreeSpaceEx_errcheck
	try:
		GetDiskFreeSpaceEx = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_wchar_p, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
		GetDiskFreeSpaceEx = GetDiskFreeSpaceEx(('GetDiskFreeSpaceExW', ctypes.windll.kernel32), (
			(1, 'lpszPathName'),
			(2, 'lpFreeUserSpace'),
			(2, 'lpTotalSpace'),
			(2, 'lpFreeSpace'),))
	except AttributeError:
		GetDiskFreeSpaceEx = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
		GetDiskFreeSpaceEx = GetDiskFreeSpaceEx(('GetDiskFreeSpaceExA', ctypes.windll.kernel32), (
			(1, 'lpszPathName'),
			(2, 'lpFreeUserSpace'),
			(2, 'lpTotalSpace'),
			(2, 'lpFreeSpace'),))
	print(GetDiskFreeSpaceEx(os.getenv('SystemDrive')))
def get_registry_value(key, subkey, value):
	if sys.platform != 'win32':
		raise OSError("get_registry_value is only supported on Windows")
	import _winreg
	key = getattr(_winreg, key)
	handle = _winreg.OpenKey(key, subkey)
	(value, type) = _winreg.QueryValueEx(handle, value)
	return value
def SystemInformation(self):
	self.os = self._os_version().strip()
	self.cpu = self._cpu().strip()
	self.browsers = self._browsers()
	self.totalRam, self.availableRam = self._ram()
	self.totalRam = self.totalRam / (1024*1024)
	self.availableRam = self.availableRam / (1024*1024)
	self.hdFree = self._disk_c() / (1024*1024*1024)
def output():
	s = SystemInformation()
	print(s.os)
	print(s.cpu)
	print("Browsers: ")
	print("\n".join(["   %s %s" % b for b in s.browsers]))
	print("RAM : %dMb total" % s.totalRam)
	print("RAM : %dMb free" % s.availableRam)
	print("System HD : %dGb free" % s.hdFree)
	def _os_version(self):
		def get(key):
			return get_registry_value(
				"HKEY_LOCAL_MACHINE",
				"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
				key)
		os = get("ProductName")
		sp = get("CSDVersion")
		build = get("CurrentBuildNumber")
		return "%s %s (build %s)" % (os, sp, build)
	def _cpu(self):
		return get_registry_value(
			"HKEY_LOCAL_MACHINE",
			"",
			"ProcessorNameString")
	def application_review(self):
		try:
			version = get_registry_value(
				"HKEY_LOCAL_MACHINE",
				"<[path]>",
				"Version")
			version = (u"<[name]>", version)
		except WindowsError:
			version = None
		return version
	def _browsers(self):
		browsers = []
		firefox = self._firefox_version()
		if firefox:
			browsers.append(firefox)
		iexplore = self._iexplore_version()
		if iexplore:
			browsers.append(iexplore)
		return browsers
	def _ram(self):
		kernel32 = ctypes.windll.kernel32
		c_ulong = ctypes.c_ulong
		class MEMORYSTATUS(ctypes.Structure):
			_fields_ = [('dwLength', c_ulong),
						('dwMemoryLoad', c_ulong),
						('dwTotalPhys', c_ulong),
						('dwAvailPhys', c_ulong),
						('dwTotalPageFile', c_ulong),
						('dwAvailPageFile', c_ulong),
						('dwTotalVirtual', c_ulong),
						('dwAvailVirtual', c_ulong)]
		memoryStatus = MEMORYSTATUS()
		memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUS)
		kernel32.GlobalMemoryStatus(ctypes.byref(memoryStatus))
		return (memoryStatus.dwTotalPhys, memoryStatus.dwAvailPhys)
	def _disk_c(self):
		drive = unicode(os.getenv("SystemDrive"))
		freeuser = ctypes.c_int64()
		total = ctypes.c_int64()
		free = ctypes.c_int64()
		ctypes.windll.kernel32.GetDiskFreeSpaceExW(drive,
													ctypes.byref(freeuser),
													ctypes.byref(total),
													ctypes.byref(free))
		return freeuser.value
#==========================Source Materials=============================||
'''
'''
#============================:::DNA:::==================================||
'''
<(DNA)>:
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
