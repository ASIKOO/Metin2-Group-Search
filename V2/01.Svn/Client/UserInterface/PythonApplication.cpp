//Find
	if (!rkItemMgr.LoadItemList(szItemList))
	{
		TraceError("LoadLocaleData - LoadItemList(%s) Error", szItemList);
	}
	
///Add
#if defined(ENABLE_PARTY_MATCH)
	char szPartyMatch[256];
	snprintf(szPartyMatch, sizeof(szPartyMatch), "%s/partymatch_info.txt", localePath);
	rkNetStream.LoadPartyMatchInfo(szPartyMatch);
#endif