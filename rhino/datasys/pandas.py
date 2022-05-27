






	def pandas(self, serv='yahoo', how='datareader'):#					||
		''
		go = True
		while go == True:
			go = False
			terms = next(sonql.doc(name).read(None,{},cmd))
			go = terms.go
			for t in terms.dikt['given']['records']:
				try:
					d = pdr.DataReader(t[0], serv,#				||
												self.start, self.end)#	||
				except Exception as e:
					m = ['Grab Failed for ',t[0],'on service',serv,#	||
														'due to',e]#	||
					comm.see(m)
					log.WORKLOG(e,m,t[0],serv)
					d = None
					continue
				try:
					d.reset_index(level=0, inplace=True)
				except Exception as e:
					m = ['Grab Failed for ',t[0],'on service',serv,#	||
														'due to',e]#	||
					comm.see(['Failed Cmd and Data Stored to ',m])#		||
					log.WORKLOG(e,m, d, serv)
					continue
				try:#													||
					fx = lambda x: dt.datetime.strftime(x,
													'%Y%m%d%H%M%S')#	||
					d.Date = d.Date.apply(fx)
				except Exception as e:
					log.WORKLOG(e,m,d,serv)
					continue
				d = d.assign(TickerID=lambda x: t[0])
				data = {table: {'columns': ['Date', 'High','Low',
											'Open','Close','Volume',
											'Adj Close','TickerID'],
								'records': d}}
				comm.see(['Data Return Type',type(d),type(d)])
				sonql.doc(self.store['db']).write(data)
			return self