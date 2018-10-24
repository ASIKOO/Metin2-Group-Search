//Find
	Set(HEADER_CG_ITEM_MOVE, sizeof(TPacketCGItemMove), "ItemMove", true);

///Add
	#ifdef GROUP_MATCH
	Set(HEADER_CG_GROUP_MATCH, sizeof(TPacketCGGrup), "GroupMatch", true);
	#endif