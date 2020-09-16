#Find
	def OnEndFrame(self):
		pass
		
#Add
	if app.ENABLE_PARTY_MATCH:
		def ResetFrame(self):
			wndMgr.ResetFrame(self.hWnd)
			
#Find in class Button(Window) / def __init__(self, layer = "UI"):
		self.ToolTipText = None
		
#Add
		if app.ENABLE_PARTY_MATCH:
			self.overFunc = None
			self.overArgs = None
			self.overOutFunc = None
			self.overOutArgs = None
			
#Find in class Button(Window) / def __del__(self):
		self.eventArgs = None
		
#Add
		if app.ENABLE_PARTY_MATCH:
			self.overFunc = None
			self.overArgs = None
			self.overOutFunc = None
			self.overOutArgs = None
			
#Find
	def SetUp(self):
		wndMgr.SetUp(self.hWnd)
		
#Add
	if app.ENABLE_PARTY_MATCH:
		def OnMouseOverIn(self):
			if self.overFunc:
				apply(self.overFunc, self.overArgs )
		def OnMouseOverOut(self):
			if self.overOutFunc:
				apply(self.overOutFunc, self.overOutArgs )
		def SetOverEvent(self, func, *args):
			self.overFunc = func
			self.overArgs = args
		def SetOverOutEvent(self, func, *args):
			self.overOutFunc = func
			self.overOutArgs = args