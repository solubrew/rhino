#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Pheonix@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''  #																	||
---  #																	||
<(META)>:  #															||
	DOCid:   #						||
	name:  #					||
	description: >  #													||
		Custom browsing tools for embeding in nchantrs and focused web
		interaction#	||
	expirary: <[expiration]>  #											||
	version: <[version]>  #												||
	path: <[LEXIvrs]>  #												||
	outline: <[outline]>  #												||
	authority: document|this  #											||
	security: sec|lvl2  #												||
	<(WT)>: -32  #														||
''' #																	||
# -*- coding: utf-8 -*-#												||
#================================Core Modules===================================||
import sys, datetime as dt, os
#===============================3rd Party Modules===============================||
try:
	import win32com
	import win32com.client
	import pythoncom
except:
	print('No Win32Com')
#===============================================================================||
here = join(dirname(__file__),'')#												||
there = abspath(join('../../..'))#												||set path at pheonix level
version = '0.0.0.0.0.0'#														||
#===============================================================================||
class bppk(object):
	def __init__(self):
		''' '''

'''
#message.To
#message.CC
#message.BCC
#message.CreationTime
#message.Sender.GetContact
#message.Sender.Details
#message.SenderEmailAddress
#message.SenderName
#message.Subject
#message.ConversationID
#message.ConversationIndex
#message.Parent.Store.IsConversationEnabled
def outlook():
	outlook = win.Dispatch("Outlook.Application").GetNamespace("MAPI")
	inbox = outlook.GetDefaultFolder(6)#6 is inbox
	sent = outlook.GetDefaultFolder(5)#18 is a shared folder 20 server Failures
	calendar = outlook.GetDefaultFolder(9)
	#Contacts = 10
	#unknown = 12,13,15
	#Journal = 11
	#public_folders = 18
	#conflicts = 20
	#deleted = 3
	#outbox = 4
	folders = outlook.GetDefaultFolder(6).items
	print(folders)
	#print(folders.GetLast())
	#for folder in folders:
	#	print(folder)
	#archive = outlook.
	#print(archive)
	#messages = CurArc.Items
	#message = messages.GetLast()
	#body_content = message.body
	#print (body_content)
	def sendEmail():
		s = win.client.Dispatch("Mapi.Session")
		o = win.client.Dispatch("Outlook.Application")
		s.Logon("Outlook2003")
		Msg = o.CreateItem(0)
		Msg.To = "recipient@domain.com"
		Msg.CC = "more email addresses here"
		Msg.BCC = "more email addresses here"
		Msg.Subject = "The subject of you mail"
		Msg.Body = "The main body text of you mail"
		attachment1 = "Path to attachment no. 1"
		attachment2 = "Path to attachment no. 2"
		Msg.Attachments.Add(attachment1)
		Msg.Attachments.Add(attachment2)
		Msg.Send()
	targets = [
		['Joe.Brewer@samtec.com', 'Archives', '2016_Q34']
		, ['Joe.Brewer@samtec.com', 'Archives', '2016_Q12']
		, ['Joe.Brewer@samtec.com', 'Archives', '2015_Q34']
	#	, ['Joe.Brewer@samtec.com', 'Archives', '2015_Q12']
		, ['Joe.Brewer@samtec.com', 'Sent Items']
	]
def monitor():
	outlook = win32com.client.DispatchWithEvents("Outlook.Application", Handler_Class)
	pythoncom.PumpMessages()
def scan():#pickup any messages that have come through while the pump was down
	pass
def sanitize_subject(subject):
	codes = ['RE :','Re: ','FW: ','fw: ','Fwd: ','fwd: ']
	text = subject
	subject = pheonix.trans.text.sanitize(text, codes)
	return subject
class Handler_Class(object):
	def OnNewMailEx(self, receivedItemsIDs):
		outlook = win32com.client.Dispatch("Outlook.Application")
		messages = []
		for ID in receivedItemsIDs.split(","):
#			print(ID)
#			print(outlook)
			# Microsoft.Office.Interop.Outlook _MailItem properties: https://msdn.microsoft.com/en-us/library/microsoft.office.interop.outlook._mailitem_properties.aspx
			#https://blog.matthewurch.ca/?p=236
			mailItem = outlook.Session.GetItemFromID(ID)
			print("Subj: ", str(mailItem.Subject.encode('ascii','ignore').decode('utf-8')))
			print("Body: ", str(mailItem.Body.encode('ascii','ignore').decode('utf-8')))
			print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			messages.append(mailItem)
		return messages
def getMessagesFromFolders(Folders, targets):
	box = []#
	for target in targets:#
		folder = find_folder(Folders, targets)#
		box.append(folder)#
	return box
#outlook = win32com.client.DispatchWithEvents("Outlook.Application", Handler_Class)
#pythoncom.PumpMessages()
class outlook(object):
	def __init__(self):
		self.Outlook = win32com.client.Dispatch("Outlook.Application")
		self.mapi = self.Outlook.GetNamespace("MAPI")
class mailbox(object):
	def __init__(self, outlook):
		self.inbox = outlook.mapi.GetDefaultFolder(6)
		self.sent = outlook.mapi.GetDefaultFolder(5)
		self.cal = outlook.mapi.GetDefaultFolder(9)
		self.Journal = outlook.mapi.GetDefaultFolder(11)
		self.public_folders = outlook.mapi.GetDefaultFolder(18)
		self.conflicts = outlook.mapi.GetDefaultFolder(20)
		self.deleted = outlook.mapi.GetDefaultFolder(3)
		self.outbox = outlook.mapi.GetDefaultFolder(4)
		self.folders = outlook.mapi.GetDefaultFolder(6)
def find_folder(folders, search_path, level=0):
	for folder in folders:
		name = folder.Name
		if name.lower() == search_path[level].lower():
			if level < len(search_path)-1:
#				print(dir(folder))
				folder = find_folder(folder.Folders, search_path, level+1)# search sub folder
			return folder
	return None
def send():
	s = win32com.client.Dispatch("Mapi.Session")
	o = win32com.client.Dispatch("Outlook.Application")
	s.Logon("Outlook2003")
	Msg = o.CreateItem(0)
	Msg.To = "recipient@domain.com"
	Msg.CC = "more email addresses here"
	Msg.BCC = "more email addresses here"
	Msg.Subject = "The subject of you mail"
	Msg.Body = "The main body text of you mail"
	attachment1 = "Path to attachment no. 1"
	attachment2 = "Path to attachment no. 2"
	Msg.Attachments.Add(attachment1)
	Msg.Attachments.Add(attachment2)
	Msg.Send()
#need to create an object by which i can loop through the rule and call attributes like " in rule.categories "
#for each message get the conversation ID then check to see if that conversation has any tags and apply accordingly
class mailbox:
	def __init__(self):
		self.Outlook = win32com.client.Dispatch("Outlook.Application")
		self.mapi = self.Outlook.GetNamespace("MAPI")
		self.targets = [['Joe.Brewer@samtec.com', 'Archives', '2017_Q12'],
					['Joe.Brewer@samtec.com', 'Archives', '2016_Q34'],
					['Joe.Brewer@samtec.com', 'Archives', '2016_Q12'],
					['Joe.Brewer@samtec.com', 'Archives', '2015_Q34'],
					['Joe.Brewer@samtec.com', 'Sent Items']]
	def find_folder(self, search_path, level=0):
		for folder in self.mapi.Folders:
			name = folder.Name
			if name.lower() == search_path[level].lower():
				if level < len(search_path)-1:
#					print(dir(folder))
					folder = find_folder(folder.Folders, search_path, level+1)# search sub folder
				return folder
		return None
	def NX(self):
 		self.todo = []
		for target in targets:
			folder = self.find_folder(target)
			todo_folders.append(folder)
		for folder in todo_folders:
			items = folder.Items
			for message in items:
				clean_subject = sam.work.email.sanitize().subject(message.Subject)
				if 'NX' in message.Categories and 'Notes' in message.Categories:
					if clean_subject not in note_todo:
						note_todo.append(clean_subject)
						print(str(cnt0)+': Tablet_Note - '+clean_subject)
						cnt0 += 1
				elif 'NX' in message.Categories:
class sanitize:
	def __init__(self,message=None):
		self.message = message
		if message:
			self.subject = message.Subject
			self.body = message.Body
	def subject(self, subject=None):
		pairs = {'RE:':'', 'Re:':'','re:':'','FWD:':'','Fwd:':'','fwd:':'','fw:':''}
		if subject:
			self.subject = subject
		self.subject = pheonix.trans.text.text.exchange(subject, pairs)
		self.subject = str(self.subject.encode('ascii','ignore')).lower()
		return self.subject
f1l3 = home+'/1_NX/SAM_TODOs'
cnt = 0
outlook_todo = []
note_todo = []
project_todo = {}
projects = ['SPC','BTO','Off Cuts','Gold','ACS']
for cat in projects:
	project_todo[cat] = []
project_todo['other'] = []
write_todo = []
cnt0 = 0
cnt1 = 0
write_todo = ''
for l1st in todo:
	items = l1st.Items
	for message in items:
		clean_subject = sam.work.email.sanitize().subject(message.Subject)
		if 'NX' in message.Categories and 'Notes' in message.Categories:
			if clean_subject not in note_todo:
				note_todo.append(clean_subject)
				print(str(cnt0)+': Tablet_Note - '+clean_subject)
				cnt0 += 1
		elif 'NX' in message.Categories:
			if clean_subject not in outlook_todo:
				outlook_todo.append(clean_subject)
				categories = ''
				categories = categories[:-2]
				task = str(cnt1)+': SAM_eMail - '+clean_subject+' => ['+str(message.Categories)+']\n'
				project_task = 0
				for cat in projects:
					if cat in message.Categories:
						project_task = 1
						if task not in project_todo[cat]:
							project_todo[cat].append(task)
				if project_task == 0:
					project_todo['other'].append(task)
				write_todo += (task)
				print(task)
				cnt1 += 1
with open(f1l3+'.txt','w') as doc:
	doc.write(write_todo)
doc.closed
new_project = ''
with open(f1l3+'_byProject.txt','w') as doc:
	for k, vs in project_todo.items():
		doc.write(k+'\n')
		for v in vs:
			doc.write('\t'+v)
doc.closed
def MessageSorter(listMessages):
	rules = MessageRules()
	for message in listMessages:
		applyCategories(message.Conversation)
		clean_subject = cleanSubject(message.Subject)
		categories = message.Categories
def arkMessage(outlook,message):
	ark = outlook.mapi.Folders.Item('Joe.Brewer@samtec.com').Folders.Item('Archives').Folders.Item('2016_Q12')
	message.Move(ark)
def exportMessage(message, trigger):
	export = pheonix.transform.docs('pdf', message)
	wolf.lone.files.sort(export, trigger)
class sanitize:
	def __init__(self,message=None):
		self.message = message
		if message:
			self.subject = message.Subject
			self.body = message.Body
	def subject(self, subject=None):
		pairs = {'RE:':'', 'Re:':'','re:':'','FWD:':'','Fwd:':'','fwd:':'','fw:':''}
		if subject:
			self.subject = subject
		self.subject = lexi.panda.trans.text.text.exchange(subject, pairs)
		self.subject = str(self.subject.encode('ascii','ignore')).lower()
		return self.subject
class sanitize:
	def __init__(self,message=None):
		self.message = message
		if message:
			self.subject = message.Subject
			self.body = message.Body
	def subject(self, subject=None):
		pairs = {'RE:':'', 'Re:':'','re:':'','FWD:':'','Fwd:':'','fwd:':'','fw:':''}
		if subject:
			self.subject = subject
		self.subject = pheonix.trans.text.text.exchange(subject, pairs)
		self.subject = str(self.subject.encode('ascii','ignore')).lower()
		return self.subject
class Sender(object):#	||Sender -> dispatches messages to interested callables
	def __init__(self):
		self.listeners = {}
#		self.logger = logger.getLogger()
	def register(self,listener,events=None):# register a listener function Parameters -----------listener : external listener function events  : tuple or list of relevant events (default=None)
		if events is not None and type(events) not in (tuple,list):
			events = (events,)
			self.listeners[listener] = events
	def dispatch(self,event=None, msg=None):# notify listeners
		for listener,events in self.listeners.items():
			if events is None or event is None or event in events:
				try:
					listener(self,event,msg)
				except (Exception,):
					self.unregister(listener)
#					errmsg = "Exception in message dispatch: Handler '{0}' unregistered for event '{1}'  ".format(listener.func_name,event)
#					self.logger.exception(errmsg)
	def unregister(self,listener):#	|| unregister listener function
		del self.listeners[listener]
def sort(message):
	if message.GetConversation().GetTable().GetRowCount() > 1:
		message = rules(message)
	if message.Categories == None:
		#assign the x categorie
		message.Categories = ('X',)
		#create a task to disposition email
		pheonix.todo.todo.new(message)
	#move message to archive folder
	if tdy in Q1 or tdy in Q2:
		message.folder = 'joe.brewer@samtec.com/Archives/'+yr+'_Q12'
	else:
		message.folder = 'Joe.Brewer@samtec.com/Archives/'+yr+'_Q34'
	message.save()
def getCatsforConvo(message):
	convo = message.GetConversation()
	if convo:
		table = convo.GetTable()
		rows = table.GetRowCount()
		convo_cats = ''
		messages = convo.GetMessages()
		for message in messages:
			if convo_cats == '':
				convo_cats = message.Categories
			else:
				cats = message.Categories
				for cat in cats:
					if cat not in convo_cats:
						convo_cats += ','+cat
		return convo_cats
	else:
		return None
def find_folder(folders, search_path, level=0):
	for folder in folders:
		name = folder.Name
		if name.lower() == search_path[level].lower():
			if level < len(search_path)-1:
#				print(dir(folder))
				folder = find_folder(folder.Folders, search_path, level+1)# search sub folder
			return folder
	return None
	def process(messages):
		tag(messages)
		distribute(messages)
	def tag(messages):
		for message in messages:
			convo_cats = getCatsforConvo(message)
			cats = message.Categories
			cat_fam = breedcats(cats, convo_cats)
			if cat_fam:
				if 'NX' not in cat_fam:
					message.Categories = cat_fam+',NX'
					convo.Categories = convo_cats
					convo.Save
			for VIP in VIPs:
				if VIP in message.from0:
					message.Categories = convo_cats+',HIGH,X'
				elif 'Open' in message.Categories:
					#add Mobile
					pass
			projects = pheonix.multiorganism.projects.project.getProjects('SAM')
			for proj in projects:
				profile = pheonix.multiorganism.project.project.profile(proj)['email']['profile']
				rules = profile['rules']
				for rule in rules:
					if rule['Type'] == 'Contact':
						if contact in message.to:
							pass
						elif contact in message.ffrom:
							pass
						elif contact in message.cc:
							pass
						elif contact in message.bcc:
							pass
					elif rule['Type'] == 'Content':
						pass
			else:
				message.Categories = 'NX,ToRead'
			message.Save
#==========================Source Materials=============================||
'''
'''

Monitor Outlook Inbox
	https://blog.matthewurch.ca/?p=236


Message Items

MailItem Object:
	https://msdn.microsoft.com/en-us/library/office/ff861332.aspx
	Category Assigment
		https://msdn.microsoft.com/en-us/library/office/ff424469.aspx
		SetAlwaysAssignCategories Method
			https://msdn.microsoft.com/en-us/library/office/ff868084.aspx
		Create and Manipulate Categories:
			https://msdn.microsoft.com/en-us/library/office/ff424467.aspx
	GetConversation Method
		https://msdn.microsoft.com/en-us/library/office/ff869870.aspx

Message Links
	http://stackoverflow.com/questions/8667827/creating-link-to-outlook-messages

MAPIFolder Object


	MailItem Attachments:
		https://msdn.microsoft.com/en-us/library/office/hh290849.aspx


	Items Memebers
		https://msdn.microsoft.com/en-us/library/office/ff868813.aspx



Contacts
http://stackoverflow.com/questions/405724/modifying-microsoft-outlook-contacts-from-python




Office Outlook 2007
	Known problems - https://support.microsoft.com/en-us/kb/929590




Message Parsing:
https://github.com/zapier/email-reply-parser




'''
#============================:::DNA:::==================================||
'''
<(DNA)>:
	administer:
		version: <[active:.version]>
		test:
		description: >
			Administrate Tests of the Tmplt Classes
		work:
	here:
		version: <[active:.version]>
		test:
		description: >
			Test Each Tmplt Class
		work:
'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
