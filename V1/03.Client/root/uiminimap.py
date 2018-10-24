#Find
			self.MiniMapShowButton = self.GetChild("MiniMapShowButton")

#Add
			if app.PARTY_MATCH:
				self.group = self.GetChild("PartyMatchButton")
				self.group_effect = self.GetChild("PartyMatchEffect")
				
#Find
		self.serverInfo.SetText(net.GetServerInfo())
		
#Add
		if app.PARTY_MATCH:
			self.group.SetEvent(ui.__mem_func__(self.GroupSettings))
				
#Find
		self.tooltipAtlasOpen.SetTooltipPosition(ButtonPosX, ButtonPosY)
	
#Add
	
		if app.PARTY_MATCH:
			self.group.Hide()
			self.group_effect.Hide()
#Find
	def Destroy(self):
		self.HideMiniMap()

		self.AtlasWindow.Destroy()
		self.AtlasWindow = None

		self.ClearDictionary()

		self.__Initialize()
		
#Add
	if app.PARTY_MATCH:
		def open_party_match(self, ayar, index):
			if ayar == "1":
				self.group.Show()
				self.group_effect.Show()
			else:
				self.group.Hide()
				self.group_effect.Hide()
			self.aasindex = index
			
		def GroupSettings(self):
			import uipartymatch
			self.wndPartyMatch = uipartymatch.PartyMatchWindow()
			self.wndPartyMatch.Open2(self.aasindex)
			