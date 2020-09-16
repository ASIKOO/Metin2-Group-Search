#Find
import uiParty

#Add
import app
if app.ENABLE_PARTY_MATCH:
	import uiPartyMatch
	
#Find
		self.wndDragonSoul = None
	
#Add
		if app.ENABLE_PARTY_MATCH:
			self.wndPartyMatchWindow = None

#Find
			self.wndExpandedTaskBar.SetToggleButtonEvent(uiTaskBar.ExpandedTaskBar.BUTTON_DRAGON_SOUL, ui.__mem_func__(self.ToggleDragonSoulWindow))
	
#Add
			if app.ENABLE_PARTY_MATCH:
				self.wndExpandedTaskBar.SetToggleButtonEvent(uiTaskBar.ExpandedTaskBar.BUTTON_PARTY_MATCH_WINDOW, ui.__mem_func__(self.TogglePartyMatchWindow))	
#Find
		wndMiniMap = uiMiniMap.MiniMap()
		
#Add
		if app.ENABLE_PARTY_MATCH:
			self.wndPartyMatchWindow = uiPartyMatch.PartyMatch()
			
#Find
		self.DRAGON_SOUL_IS_QUALIFIED = False
		
#Add
		if app.ENABLE_PARTY_MATCH:
			self.wndPartyMatchWindow.SetItemToolTip(self.tooltipItem)
			self.wndPartyMatchWindow.BindMiniMap(self.wndMiniMap)
			if self.wndMiniMap:
				self.wndMiniMap.BindPartyMatchEvent( self.TogglePartyMatchWindow )
				
#Find
		if self.wndItemSelect:
			self.wndItemSelect.Destroy()
			
#Add
		if app.ENABLE_PARTY_MATCH:
			if self.wndPartyMatchWindow:
				self.wndPartyMatchWindow.Destroy()
				del self.wndPartyMatchWindow
				
#Find
		if self.wndExpandedTaskBar:
			self.wndExpandedTaskBar.Hide()
			
#Add
		if app.ENABLE_PARTY_MATCH:
			if self.wndPartyMatchWindow:
				self.wndPartyMatchWindow.Hide()
				
#Find
		if self.wndExpandedTaskBar:
			hideWindows += self.wndExpandedTaskBar,
			
#Add
		if app.ENABLE_PARTY_MATCH:
			if self.wndPartyMatchWindow:
				hideWindows += self.wndPartyMatchWindow,
				
#Find
	def EmptyFunction(self):
		pass
		
#Add
	if app.ENABLE_PARTY_MATCH:
		def PartyMatchResult(self, type, data):
			if self.wndPartyMatchWindow:
				self.wndPartyMatchWindow.PartyMatchResult(type, data)
				
		def TogglePartyMatchWindow(self):
			if False == player.IsObserverMode() and self.wndPartyMatchWindow:
				if not self.wndPartyMatchWindow.IsShow():
					self.wndPartyMatchWindow.Show()
				else:
					self.wndPartyMatchWindow.Close()