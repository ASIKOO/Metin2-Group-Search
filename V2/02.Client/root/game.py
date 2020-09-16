#Find
	def AskSafeboxPassword(self):
		self.interface.AskSafeboxPassword()
		
#Add
	if app.ENABLE_PARTY_MATCH:
		def PartyMatchResult(self, type, data):
			self.interface.PartyMatchResult(type, data)