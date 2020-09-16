//Find
	HEADER_CG_QUEST_CONFIRM			= 31,
	
///Add
#if defined(ENABLE_PARTY_MATCH)
	HEADER_CG_PARTY_MATCH = 32,
#endif

//Find
	HEADER_GC_HYBRIDCRYPT_KEYS		= 152,
	
///Add
#if defined(ENABLE_PARTY_MATCH)
	HEADER_GC_PARTY_MATCH = 147,
#endif

//Find
typedef struct command_item_move
{
	...
} TPacketCGItemMove;

///Add
#if defined(ENABLE_PARTY_MATCH)
typedef struct partymatchCG
{
	BYTE		Header;
	BYTE		SubHeader;
	int			index;
} TPacketCGPartyMatch;
typedef struct partymatchGC
{
	BYTE		Header;
	BYTE		SubHeader;
	BYTE		MSG;
	DWORD		index;
} TPacketGCPartyMatch;
#endif