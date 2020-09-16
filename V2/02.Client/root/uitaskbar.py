#Find
	BUTTON_DRAGON_SOUL = 0
	
#Add
	if app.ENABLE_PARTY_MATCH:
		BUTTON_PARTY_MATCH_WINDOW = 1
		
#Find
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_DRAGON_SOUL].SetParent(self)
		
#Add
		if app.ENABLE_PARTY_MATCH:
			self.toggleButtonDict[ExpandedTaskBar.BUTTON_PARTY_MATCH_WINDOW] = self.GetChild("PartyMatchButton")
			self.toggleButtonDict[ExpandedTaskBar.BUTTON_PARTY_MATCH_WINDOW].SetParent(self)