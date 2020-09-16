#Add End
import app
if app.ENABLE_PARTY_MATCH:
	window["width"] = 37*5
	window["children"][0]["width"] = window["children"][0]["width"] + 37
	window["children"][0]["children"] = window["children"][0]["children"] + (
					{
						"name" : "PartyMatchButton",
						"type" : "button",
						"style" : ("ltr", ),

						"x" : 146,
						"y" : 0,

						"width" : 37,
						"height" : 37,

						"tooltip_text" : uiScriptLocale.KEYCHANGE_PARTY_MATCH_WINDOW,
								
						"default_image" : "icon/item/party_button_01.tga",
						"over_image" : "icon/item/party_button_02.tga",
						"down_image" : "icon/item/party_button_03.tga",
					},)