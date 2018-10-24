///For bug fix 31.07.2017
//Find
#include "XTrapManager.h"

///Add
#ifdef GROUP_MATCH
#include "GroupMatchManager.h"
#endif

//Find
ch->ReviveInvisible(5);

///Add
#ifdef GROUP_MATCH
	CGroupMatchManager::instance().AramayiDurdur(ch->GetPlayerID());
#endif