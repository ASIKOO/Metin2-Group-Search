///Add
#if defined(ENABLE_PARTY_MATCH)
#include "GroupMatchManager.h"
#endif

//Find
	marriage::CManager::instance().Logout(this);
	
///Add
#if defined(ENABLE_PARTY_MATCH)
	CGroupMatchManager::instance().StopSearching(this, CGroupMatchManager::eMSG::PARTY_MATCH_FAIL, 0);
#endif