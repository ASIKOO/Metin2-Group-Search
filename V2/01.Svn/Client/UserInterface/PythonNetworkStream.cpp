//Find
			Set(HEADER_GC_PING,			CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCPing), STATIC_SIZE_PACKET));
			
///Add
#if defined(ENABLE_PARTY_MATCH)
			Set(HEADER_GC_PARTY_MATCH, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCPartyMatch), STATIC_SIZE_PACKET));
#endif

//Find
	Tracen("PythonNetworkMainStream Clear");
	
///Add
#if defined(ENABLE_PARTY_MATCH)
	m_PartyMatch.clear();
#endif