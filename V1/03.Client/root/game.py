#Find
		net.SendEnterGamePacket()
		
#Add
		if app.PARTY_MATCH:
			constInfo.KILITLE = 0
#Find
	"ConsoleEnable"			: self.__Console_Enable,

#Add
	"gorup_match_search"   : self.open_group,
	
#Find
	def __Console_Enable(self):
		constInfo.CONSOLE_ENABLE = TRUE
		self.consoleEnable = TRUE
		app.EnableSpecialCameraMode()
		ui.EnablePaste(TRUE)
		
#Add
	if app.PARTY_MATCH:
		def open_group(self, ayar, index):
			import uipartymatch
			self.wndPartyMatch = uipartymatch.PartyMatchWindow()
			if ayar == "61":
				# self.wndPartyMatch.sifir()
				constInfo.KILITLE = 0
			else:
				if self.interface:
					self.interface.wndMiniMap.open_party_match(ayar, index)
					if ayar == "1":
						self.wndPartyMatch.bilgi_ver(index)
						constInfo.KILITLE = 61
					else:
						constInfo.KILITLE = 0