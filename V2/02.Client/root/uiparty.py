#Find
	def __ClearShowingButtons(self):
		self.showingButtonList = []
		
#Change
	def __ClearShowingButtons(self):
		if app.ENABLE_PARTY_MATCH:
			for button in self.showingButtonList:
				button.Hide()
		self.showingButtonList = []