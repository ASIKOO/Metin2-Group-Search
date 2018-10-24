//Find
#include "crc32.h"

///Add
#ifdef GROUP_MATCH
#include "GroupMatchManager.h"
#endif

//Find
	if (GetParty() != NULL)
	{
		GetParty()->UpdateOfflineState(GetPlayerID());
	}
	
///Add
	#ifdef GROUP_MATCH
	CGroupMatchManager::instance().AramayiDurdur(GetPlayerID());
	#endif