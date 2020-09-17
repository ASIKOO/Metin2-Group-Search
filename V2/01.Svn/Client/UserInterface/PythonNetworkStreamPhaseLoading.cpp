//Find
bool CPythonNetworkStream::IsInsultIn(const char* c_szMsg)
{
	return m_kInsultChecker.IsInsultIn(c_szMsg, strlen(c_szMsg));
}

///Add
#if defined(ENABLE_PARTY_MATCH)
bool CPythonNetworkStream::LoadPartyMatchInfo(const char* FileName)
{
	m_PartyMatch.clear();

	CTextFileLoader* pkTextFileLoader = CTextFileLoader::Cache(FileName);

	if (!pkTextFileLoader)
		return false;

	if (pkTextFileLoader->IsEmpty())
		return false;

	pkTextFileLoader->SetTop();

	for (DWORD i = 0; i < pkTextFileLoader->GetChildNodeCount(); ++i) 
	{
		CTextFileLoader::CGotoChild GotoChild(pkTextFileLoader, i);
		auto p = std::make_shared<PartyMatchInfo>();

		int map;
		if (!pkTextFileLoader->GetTokenInteger("map", &map))
			return false;

		if (!pkTextFileLoader->GetTokenInteger("level", &p->limit_level))
			return false;

		std::vector<std::pair<int, int>> items;
		items.resize(3);

		for (DWORD j = 0; j < pkTextFileLoader->GetChildNodeCount(); ++j) 
		{
			if (pkTextFileLoader->SetChildNode(j))
			{
				CTokenVector* tv;
				for (int k = 0; k < items.size(); k++) 
				{
					if (pkTextFileLoader->GetTokenVector(std::to_string(k + 1), &tv)) 
					{
						if (tv->size() != 2) 
						{
							TraceError("CPythonNetworkStream::LoadPartyMatchInfo : syntax error on item table.");
							return false;
						}

						auto it = tv->begin();
						while (it != tv->end()) {
							auto vnum = std::stoi(*it++);
							auto count = std::stoi(*it++);
							items[k] = std::make_pair(vnum, count);
						}
					}
				}
				pkTextFileLoader->SetParentNode();
			}
		}

		p->items = std::move(items);

		m_PartyMatch.emplace(map, std::move(p));
	}

	return true;
}
#endif