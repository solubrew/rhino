#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(META)>:
	docid: 'a401bdfc-d03b-4f8b-a72c-84f9c8e6f643'
	name:
	description: >
	expirary: <[expiration]>
	version: <[version]>
	authority: document|this
	security: sec|lvl2
	<(WT)>: -32
'''
# -*- coding: utf-8 -*-
#=======================================================================||
from os.path import abspath, dirname, join
import subprocess as sbp, os
#=======================================================================||
#from fabric import Connection
#=======================================================================||
from condor import condor, thing
from excalc import text as calct
from rhino.ossys import linux
#=======================================================================||
here = join(dirname(__file__),'')#						||
there = abspath(join('../../..'))#						||set path at pheonix level
version = '0.0.0.0.0.0'#												||
log = True
#=======================================================================||
pxcfg = join(abspath(here), '_data_/git.yaml')
class linkage(object):
	def __init__(self, cfg=None):
		if log: print('Git Config', cfg)
		self.config = condor.instruct(pxcfg).override(cfg)
		if log: print('Git Linkage Config',self.config.dikt)
		self.os = linux.linkage()

	def clone(self, path, to):
		''' '''
		self.os.set_working_directory(to)
		out = self.os.bashr(f'git clone {path}')
		return out

	def commit(self, msg):
		'''add changes and commit to current branch'''
		out = self.os.bashr('git add --all')
		#need to verify cmd worked
		out = self.os.bashr(f'git commit -m {msg}')
		return out

	def pull(self, path, to):
		''' '''
		self.os.set_working_directory(to)
		if log: print('To', to)
		out = self.os.bashr(f'git pull {path}')
		return out

	def push(self):
		''' '''
		out = self.os.bashr('git push origin main')
		out = self.os.bashr(username)
		out = self.os.bashr(pword)
		return out

	def roll(self):
		'''Move each branch foward 1 version'''
		i = 0
		for branch in self.config.dikt['branches']:
			if i == 0:
				i += 1
				pbranch = branch
				continue
			out = self.os.bashr(f'git checkout {branch}')
			out = self.os.bashr(f'git merge {pbranch}')
			pbranch = branch

	def setup(self):
		''' '''
		out = self.os.bashr('git init')
		out = self.os.bashr('git add --all')
		out = self.os.bashr('git commit')
		print('Config', self.config.dikt)
		for branch in self.config.dikt['branches']:
			out = self.os.bashr('git branch {branch}')

	def tag(self):
		''' '''
		msg = '"{CompanyRepoSystem} revision {RevisionNum}" {OptionalCodeVersion} {CommitNum}'
		out = self.os.bashr(f'git tag -m {msg}')
		return out

def gitDiff():
	'''Difference the dirs and files within 2 directories in different git
		states ignoring the git folders and overwriting changes from a to b
		also need to remove files and dirs from b that are not in a
		then run git commands to update the local git this creates increased
		overhead but begins to reconcile the use of Syncthing with Git and
		github while maintaining the internal release process being built'''
#==========================Source Materials=============================||
'''



https://pygithub.readthedocs.io/en/latest/introduction.html
https://python-gitlab.readthedocs.io/en/stable/api-usage.html

git push --set-upstream https://github.com/solubrew/pyqt5pandas.git master

git push https://github.com/solubrew/pyqt5pandas.git

git commit -am "message"


git clone https://github.com/solubrew/subtrix.git

git remote add origin subtrix
git remote -v
git push origin master
git add --all
git commit
git add --all
git commit
git push origin master
git add --all
git commit
git push origin master

mkdir -p /path/xxx.git
cd /path/xxx.git
git init --bare #git init tells the system to put a reposiotry here

git remote add origin /path/xxx.get #get remote add origin connects the repository to the master

git add .
git commit -m "cloning existing repo" #git commit -m to commit locally
git push origin master

git add .
git commit -m "syncing to {CompanyRepoSystem} revision {RevisionNum}"
git push origin master

git tag -m "{CompanyRepoSystem} revision {RevisionNum}" {OptionalCodeVersion} {CommitNum}
git tag -l -n
git push --tags

git pull #to pull changes from a repository



GUIs
http://www.git-scm.com/downloads/guis
Git and Other Systems - Git and Subversion
http://git-scm.com/book/en/v1/Git-and-Other-Systems-Git-and-Subversion
Mercurial
	http://mercurial.selenic.com/
BitBucket
Git
	GitHub
	need to work on creating a workflow for connecting to get hub for various projects
	http://git-scm.com/docs/user-manual.html
	https://www.digitalocean.com/community/tutorials/how-to-use-git-effectively
	http://git-scm.com/docs/gittutorial
	http://lifehacker.com/5983680/how-the-heck-do-i-use-github
Gitolite
	http://gitolite.com/gitolite/
GitLab
Gitosis is depreciated
Git cola
Git DAG
Git g
	{sudo apt-get install git-cola --install-suggests}
git-DAG
Gitolite
http://gitolite.com/gitolite/
https://gitlab.com/explore
http://git-scm.com/book/ch4-8.html
http://trac.edgewall.org/wiki/TracGit
https://pypi.python.org/pypi/Trac/1.0.8




GUIs
http://www.git-scm.com/downloads/guis
Git and Other Systems - Git and Subversion
http://git-scm.com/book/en/v1/Git-and-Other-Systems-Git-and-Subversion
Mercurial
	http://mercurial.selenic.com/
BitBucket
Git
	GitHub
	need to work on creating a workflow for connecting to get hub for various projects
	http://git-scm.com/docs/user-manual.html
	https://www.digitalocean.com/community/tutorials/how-to-use-git-effectively
	http://git-scm.com/docs/gittutorial
	http://lifehacker.com/5983680/how-the-heck-do-i-use-github
Gitolite
	http://gitolite.com/gitolite/
GitLab
Gitosis is depreciated
Git cola
Git DAG
Git g
	{sudo apt-get install git-cola --install-suggests}
git-DAG
Gitolite
http://gitolite.com/gitolite/
https://gitlab.com/explore
http://git-scm.com/book/ch4-8.html
http://trac.edgewall.org/wiki/TracGit
https://pypi.python.org/pypi/Trac/1.0.8
'''
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
