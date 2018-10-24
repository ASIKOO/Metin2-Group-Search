//Find
	HEADER_CG_QUEST_CONFIRM			= 31,

///Add
	#ifdef GROUP_MATCH
	HEADER_CG_GROUP_MATCH			= 32,
	#endif
	
//Find
typedef struct command_item_move
{
	BYTE 	header;
	TItemPos	Cell;
	TItemPos	CellTo;
	BYTE	count;
} TPacketCGItemMove;

///Add
#ifdef GROUP_MATCH
typedef struct grup_paketi
{
	BYTE		header;
	BYTE		index;
	BYTE		ayar;
} TPacketCGGrup;
#endif