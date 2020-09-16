//Find
PyObject * playerGetTargetVID(PyObject* poSelf, PyObject* poArgs)
{
	return Py_BuildValue("i", CPythonPlayer::Instance().GetTargetVID());
}

///Add
#if defined(ENABLE_PARTY_MATCH)
PyObject* playerGetPartyMatchInfoMap(PyObject* poSelf, PyObject* poArgs)
{
	const auto& PartyMatchInfo = CPythonNetworkStream::Instance().GetPartyMatchInfo();

	PyObject *items, *dict = PyDict_New();

	for (const auto& i : PartyMatchInfo)  {
		const auto& ItemVector = i.second->items;
		items = PyTuple_New(ItemVector.size());

		for (size_t j = 0; j < ItemVector.size(); j++)
			PyTuple_SetItem(items, j, Py_BuildValue("ii", ItemVector.at(j).first, ItemVector.at(j).second));

		PyDict_SetItem(dict, PyInt_FromLong(i.first), Py_BuildValue("iiO", i.first, i.second->limit_level, items));
	}

	return dict;
}
PyObject* playerIsPartyMatchLoaded(PyObject* poSelf, PyObject* poArgs)
{
	const auto& PartyMatchInfo = CPythonNetworkStream::Instance().GetPartyMatchInfo();
	return Py_BuildValue("i", !PartyMatchInfo.empty());
}
#endif

//Find
		{ "GetItemLink",				playerGetItemLink,					METH_VARARGS },
		
///Add
#if defined(ENABLE_PARTY_MATCH)
		{ "GetPartyMatchInfoMap",		playerGetPartyMatchInfoMap,			METH_VARARGS },
		{ "IsPartyMatchLoaded",			playerIsPartyMatchLoaded,			METH_VARARGS },
#endif

//Find
	PyModule_AddIntConstant(poModule, "MBF_SKILL",	CPythonPlayer::MBF_SKILL);
	
///Add
#if defined(ENABLE_PARTY_MATCH)
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_REQUIRED_ITEM_MAX", CPythonPlayer::PARTY_MATCH_REQUIRED_ITEM_MAX);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_INFO", CPythonPlayer::PARTY_MATCH_INFO);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_CANCEL", CPythonPlayer::PARTY_MATCH_CANCEL);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_FAIL", CPythonPlayer::PARTY_MATCH_FAIL);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_SUCCESS", CPythonPlayer::PARTY_MATCH_SUCCESS);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_START", CPythonPlayer::PARTY_MATCH_START);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_CANCEL_SUCCESS", CPythonPlayer::PARTY_MATCH_CANCEL_SUCCESS);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_FAIL_NO_ITEM", CPythonPlayer::PARTY_MATCH_FAIL_NO_ITEM);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_FAIL_LEVEL", CPythonPlayer::PARTY_MATCH_FAIL_LEVEL);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_FAIL_NOT_LEADER", CPythonPlayer::PARTY_MATCH_FAIL_NOT_LEADER);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_FAIL_MEMBER_NOT_CONDITION", CPythonPlayer::PARTY_MATCH_FAIL_MEMBER_NOT_CONDITION);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_FAIL_NONE_MAP_INDEX", CPythonPlayer::PARTY_MATCH_FAIL_NONE_MAP_INDEX);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_FAIL_IMPOSSIBLE_MAP", CPythonPlayer::PARTY_MATCH_FAIL_IMPOSSIBLE_MAP);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_HOLD", CPythonPlayer::PARTY_MATCH_HOLD);
	PyModule_AddIntConstant(poModule, "PARTY_MATCH_FAIL_FULL_MEMBER", CPythonPlayer::PARTY_MATCH_FAIL_FULL_MEMBER);
#endif