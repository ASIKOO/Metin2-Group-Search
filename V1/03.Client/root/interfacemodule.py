#Find
import uiParty

#Add
if app.PARTY_MATCH:
	import uipartymatch
	
#Find
		self.wndDragonSoul = None
	
#Add
		if app.PARTY_MATCH:
			self.wndPartyMatch = None

#Find
		self.wndExpandedTaskBar.SetToggleButtonEvent(uiTaskBar.ExpandedTaskBar.BUTTON_DRAGON_SOUL, ui.__mem_func__(self.ToggleDragonSoulWindow))
		
#Add
		self.wndExpandedTaskBar.SetToggleButtonEvent(uiTaskBar.ExpandedTaskBar.BUTTON_PARTY, ui.__mem_func__(self.ToggleParty))
			
#Find
		wndMiniMap = uiMiniMap.MiniMap()
		
#Add
		if app.PARTY_MATCH:
			wndPartyMatch = uipartymatch.PartyMatchWindow()
			
#Find
		self.wndDragonSoul = wndDragonSoul
		
#Add
		if app.PARTY_MATCH:
			self.wndPartyMatch = wndPartyMatch
			
#Find
		if self.wndDragonSoul:
			self.wndDragonSoul.Destroy()
	
#Add
		if app.PARTY_MATCH:
			if self.wndPartyMatch:
				self.wndPartyMatch.Destroy()
				
#Find
		if self.wndDragonSoul:
			del self.wndDragonSoul
			
#Add
		if app.PARTY_MATCH:
			if self.wndPartyMatch:
				del self.wndPartyMatch
				
#Find
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.Hide()
			self.wndDragonSoulRefine.Hide()
			
#Add
		if app.PARTY_MATCH:
			if self.wndPartyMatch:
				self.wndPartyMatch.Hide()
				
#Find
	def ToggleInventoryWindow(self):
		if FALSE == player.IsObserverMode():
			if FALSE == self.wndInventory.IsShow():
				self.wndInventory.Show()
				self.wndInventory.SetTop()
			else:
				self.wndInventory.OverOutItem()
				self.wndInventory.Close()
				
#Add
	if app.PARTY_MATCH:
		def ToggleParty(self):
			if FALSE == player.IsObserverMode():
				if FALSE == self.wndPartyMatch.IsShow():
					self.wndPartyMatch.Open()
				else:
					self.wndPartyMatch.Close()