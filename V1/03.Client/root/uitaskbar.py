#Find
	BUTTON_DRAGON_SOUL = 0

#Add if you have BUTTON_PET_GUI = 1 change 1->2
	if app.PARTY_MATCH:
		BUTTON_PARTY = 1
		
#Find
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_PET_GUI].SetParent(self)

#Add
		if app.PARTY_MATCH:
			self.toggleButtonDict[ExpandedTaskBar.BUTTON_PARTY] = self.GetChild("PartyMatchButton")
			self.toggleButtonDict[ExpandedTaskBar.BUTTON_PARTY].SetParent(self)