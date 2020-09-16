//Find
	Set(HEADER_CG_ITEM_MOVE, sizeof(TPacketCGItemMove), "ItemMove", true);
	
///Add
#if defined(ENABLE_PARTY_MATCH)
	Set(HEADER_CG_PARTY_MATCH, sizeof(TPacketCGPartyMatch), "PartyMatch", true);
#endif