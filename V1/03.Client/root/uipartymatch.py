#created by blackdragonx61 - 08.07.2017

import ui, player, grp, uiToolTip, net, localeInfo, uiScriptLocale, constInfo, mouseModule, app, net, uiCommon, exception, item, chat, interfaceModule, snd, dbg

class PartyMatchWindow(ui.ScriptWindow):
	isLoad = False
	isLoad2 = False
	
	ZINDANS = {
		0: localeInfo.MAP_SKIPIA_DUNGEON_BOSS,
		1: localeInfo.MAP_N_FLAME_DUNGEON_01,
		2: localeInfo.MAP_N_SNOW_DUNGEON_01,
		3: localeInfo.MAP_DAWNMIST_DUNGEON_01,
		4: localeInfo.MAP_MT_TH_DUNGEON_01,
		5: localeInfo.MAP_N_FLAME_DRAGON,
	}
	ITEMS = {
		0: 30190,#0
		1: 30179,#0
		2: 71095,#1
		3: 30613,#3
		4: 71095,#5
	}
	NEED_LEVELS = {
		0: 75,
		1: 100,
		2: 100,
		3: 95,
		4: 95,
		5: 75,
	}
	
	def __init__(self):
		self.Zindanlar = [[localeInfo.MAP_SKIPIA_DUNGEON_BOSS, 0], [localeInfo.MAP_N_FLAME_DUNGEON_01, 1], [localeInfo.MAP_N_SNOW_DUNGEON_01, 2], [localeInfo.MAP_DAWNMIST_DUNGEON_01, 3], [localeInfo.MAP_MT_TH_DUNGEON_01, 4], [localeInfo.MAP_N_FLAME_DRAGON, 5]]
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/partymatchwindow.py")
		except:
			import exception
			exception.Abort("PartyMatchWindow.__LoadWindow.LoadObject")

		try:
			self.GetChild("board").SetCloseEvent(ui.__mem_func__(self.Close))
			self.GetChild("CloseButton").SetEvent(self.OnCloseEvent)
			self.needitemslot = self.GetChild("required_items_slot")
			self.needitemslot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
			self.needitemslot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
			self.dungeon_select_button = self.GetChild("dungeon_select_button")
			self.dungeon_select_text = self.GetChild("dungeon_select_text")
			self.dungeon_level_text = self.GetChild("entree_level_text")
			self.MatchingButton = self.GetChild("MatchingButton")
			self.HideMyButton = self.GetChild("HideButtonn")
			self.HideMyButton.SetEvent(ui.__mem_func__(self.HideButtonn))
			self.HideMyButton.Hide()
			self.MatchingButton.SetEvent(ui.__mem_func__(self.SendToGame))
			self.dungeon_select_button.SetEvent(ui.__mem_func__(self.open_W))		
			self.selectBonus = self.GetChild("dungeon_select_window")
			self.selectBonus.SetParent(self)
			self.LoginManager_Board = self.ThinBoard(self, 1, 109, 61, 129, 100)
			self.NewListBox2(self.LoginManager_Board, localeInfo.SEC, 20, 0, 90, 15)
			self.tl = uiToolTip.ItemToolTip()
			self.tl.Hide()
			self.tooltipItem = self.tl
			
		except:
			import exception
			exception.Abort("PartyMatchWindow.__LoadWindow.BindObject")
			
	def __OnOverInItem(self, slotIndex):
		self.tooltipItem.ClearToolTip()
		if constInfo.DIGER_NAME == self.ZINDANS[0]:
			if slotIndex == 0:
				self.tooltipItem.AddItemData(self.ITEMS[0], 0, 0)
			elif slotIndex == 1:
				self.tooltipItem.AddItemData(self.ITEMS[1], 0, 0)
		elif constInfo.DIGER_NAME == self.ZINDANS[1]:
			if slotIndex == 0:
				self.tooltipItem.AddItemData(self.ITEMS[2], 0, 0)
		elif constInfo.DIGER_NAME == self.ZINDANS[3]:
			if slotIndex == 0:
				self.tooltipItem.AddItemData(self.ITEMS[3], 0, 0)
		elif constInfo.DIGER_NAME == self.ZINDANS[5]:
			if slotIndex == 0:
				self.tooltipItem.AddItemData(self.ITEMS[4], 0, 0)
				
	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
			
	def NewListBox2(self, parent, name, x, y, width, heigh):
		self.ListBox = ui.ListBox()
		if parent:
			self.ListBox.SetParent(parent)
		self.ListBox.SetSize(width, heigh)
		self.ListBox.SetPosition(x, y)
		self.ListBox.SetEvent(ui.__mem_func__(self.OnSelectItem))
		self.ListBox.SetPickAlways()
		self.InsertList(self.Zindanlar)
		self.ListBox.Show()
		
	def open_W(self):
		if constInfo.KILITLE != 61:
			if self.isLoad2 == False:
				self.LoginManager_Board.Show()
				self.isLoad2 = True
			else:
				self.LoginManager_Board.Hide()
				self.isLoad2 = False
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PARTY_MATCH_TEXT_1)
			
	def bilgi_ver(self, index):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PARTY_MATCH_TEXT_2 + self.ZINDANS[int(index)] + "]!")
	
	def ThinBoard(self, parent, moveable, x, y, width, heigh):
		tmpThinboard = ui.Bar3D()

		if parent:
			tmpThinboard.SetParent(parent)

		if moveable:
			tmpThinboard.AddFlag('movable')
			tmpThinboard.AddFlag('float')

		tmpThinboard.SetSize(width, heigh)
		tmpThinboard.SetPosition(x, y)

		return tmpThinboard
	
	def OnSelectItem(self, index, name):
		self.dungeon_select_text.SetText(name)
		constInfo.DIGER_NAME = name
		self.LoginManager_Board.Hide()
		self.isLoad2 = False
		self.event = index
		self.UpdateBL(index)
	
	def UpdateBL(self, index):
		self.gerekli_level = self.NEED_LEVELS[index]
		if index == 0:
			self.needitemslot.SetItemSlot(0, self.ITEMS[0], 1)
			self.needitemslot.SetItemSlot(1, self.ITEMS[1], 3)
			self.needitemslot.SetItemSlot(2, 0, 0)
		elif index == 1:
			self.needitemslot.SetItemSlot(0, self.ITEMS[2], 1)
			self.needitemslot.SetItemSlot(1, 0, 0)
			self.needitemslot.SetItemSlot(2, 0, 0)
		elif index == 2:
			self.needitemslot.SetItemSlot(0, 0, 0)
			self.needitemslot.SetItemSlot(1, 0, 0)
			self.needitemslot.SetItemSlot(2, 0, 0)
		elif index == 3:
			self.needitemslot.SetItemSlot(0, self.ITEMS[3], 1)
			self.needitemslot.SetItemSlot(1, 0, 0)
			self.needitemslot.SetItemSlot(2, 0, 0)
		elif index == 4:
			self.needitemslot.SetItemSlot(0, 0, 0)
			self.needitemslot.SetItemSlot(1, 0, 0)
			self.needitemslot.SetItemSlot(2, 0, 0)
		elif index == 5:
			self.needitemslot.SetItemSlot(0, self.ITEMS[4], 1)
			self.needitemslot.SetItemSlot(1, 0, 0)
			self.needitemslot.SetItemSlot(2, 0, 0)
		self.dungeon_level_text.SetText(localeInfo.PARTY_MATCH_TEXT_4 + " " + str(self.gerekli_level))
		
	def InsertList(self, list):
		for name, index in list:
			self.ListBox.InsertItem(index, name)
		self.ListBox.ArrangeItem()
		self.lenList = len(list)
	
	def SendToGame(self):
		if self.event == 61 or self.gerekli_level == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PARTY_MATCH_TEXT_5)
			self.sifir()
			return
		# alternative block level
		# if player.GetStatus(player.LEVEL) < self.gerekli_level:
			# chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PARTY_MATCH_TEXT_6)
			# self.sifir()
			# return
		self.Close()	
		net.SendGroupMatch(int(self.event), 1)

	def sifir(self):
		self.isLoad = True
		self.isLoad2 = False
		self.__LoadWindow()
		self.SetTop()
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		self.tooltipItem = None
		self.SetCenterPosition()
	
	def Show(self):
		ui.ScriptWindow.Show(self)
	
	def OnPressEscapeKey(self):
		self.Close()

	def Open(self):
		if constInfo.KILITLE != 61:
			if not self.isLoad:
				self.isLoad = True
				self.__LoadWindow()
				self.event = 61
				self.gerekli_level = 0
				self.needitemslot.SetItemSlot(0, 0, 0)
				self.needitemslot.SetItemSlot(1, 0, 0)
				self.needitemslot.SetItemSlot(2, 0, 0)
				self.SetTop()
				self.SetCenterPosition()
				self.Show()
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PARTY_MATCH_TEXT_3)
			
	def Open2(self, index):
		if not self.isLoad:
			self.isLoad = True
			self.__LoadWindow()

			self.SetTop()
			self.SetCenterPosition()
			self.UpdateBL(int(index))
			self.dungeon_select_text.SetText(constInfo.DIGER_NAME)
			self.digerindexx = index
			self.HideMyButton.Show()
			self.Show()
			
	def HideButtonn(self):
		net.SendGroupMatch(int(self.digerindexx), 0)
		constInfo.KILITLE = 0
		self.Close()
		
	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		self.isLoad = False
		self.isLoad2 = False
		self.LoginManager_Board.Hide()
		self.Hide()

	def OnCloseEvent(self):
		self.Close()

	def __OnClosePopupDialog(self):
		pass