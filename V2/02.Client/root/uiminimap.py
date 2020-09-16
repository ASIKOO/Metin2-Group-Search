#Find
		self.isLoaded = 0
		
#Add
		if app.ENABLE_PARTY_MATCH:
			self.party_match_event	= None
			self.tooltipPartyMatch = MapTextToolTip()
			self.tooltipPartyMatch.SetText(localeInfo.PARTY_MATCH_SEARCHING)
			self.tooltipPartyMatch.Show()
			
#Find
		self.serverInfo = None
		
#Add
		if app.ENABLE_PARTY_MATCH:
			self.party_match_event	= None
			self.tooltipPartyMatch	= 0
			self.PartyMatchButton	= 0
			self.PartyMatchEffect	= 0
			
#Find
			self.serverInfo = self.GetChild("ServerInfo")
			
#Add
			if app.ENABLE_PARTY_MATCH:
				self.PartyMatchButton = self.GetChild("PartyMatchButton")
				if self.party_match_event:
					self.PartyMatchButton.SetEvent( self.party_match_event )
				self.PartyMatchButton.Hide()
				self.PartyMatchEffect = self.GetChild("PartyMatchEffect")
				self.PartyMatchEffect.Hide()
				
#Find
		self.tooltipAtlasOpen.SetTooltipPosition(ButtonPosX, ButtonPosY)
		
#Add
		if app.ENABLE_PARTY_MATCH:
			(ButtonPosX, ButtonPosY) = self.PartyMatchButton.GetGlobalPosition()
			self.tooltipPartyMatch.SetTooltipPosition(ButtonPosX, ButtonPosY)
			
#Find
		if True == self.AtlasShowButton.IsIn():
			self.tooltipAtlasOpen.Show()
		else:
			self.tooltipAtlasOpen.Hide()
			
#Add
		if app.ENABLE_PARTY_MATCH:
			if True == self.PartyMatchButton.IsIn():
				self.tooltipPartyMatch.Show()
			else:
				self.tooltipPartyMatch.Hide()
				
#Find
	def ScaleDown(self):
		miniMap.ScaleDown()
		
#Add
	if app.ENABLE_PARTY_MATCH:
		def ShowPartyMatchButton(self):
			if self.PartyMatchButton:
				self.PartyMatchButton.Show()
			if self.PartyMatchEffect:
				self.PartyMatchEffect.Show()
				self.PartyMatchEffect.ResetFrame()
		def HidePartyMatchButton(self):
			if self.PartyMatchButton:
				self.PartyMatchButton.Hide()
			if self.PartyMatchEffect:
				self.PartyMatchEffect.Hide()
		def BindPartyMatchEvent(self, event):
			if self.PartyMatchButton:
				self.PartyMatchButton.SetEvent( ui.__mem_func__(event) )
			else:
				self.party_match_event = ui.__mem_func__(event)