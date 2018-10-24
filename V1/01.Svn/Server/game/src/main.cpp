//Find

#ifdef __AUCTION__
#include "auction_manager.h"
#endif

///Add

#ifdef GROUP_MATCH
#include "GroupMatchManager.h"
#endif

//Find
	// LOCALE_SERVICE
	config_init(st_localeServiceName);
	// END_OF_LOCALE_SERVICE
	
///Add
	#ifdef GROUP_MATCH
	CGroupMatchManager::instance().group_search_config_init();
	#endif

//Find
	DESC_MANAGER	desc_manager;
	
///Add	
	#ifdef GROUP_MATCH
	CGroupMatchManager groupmatch_manager;
	#endif
	
//Find
	Cube_init();
	
///Add
	#ifdef GROUP_MATCH
	groupmatch_manager.Initialize();
	#endif
	
//Find
	OXEvent_manager.Destroy();
	
///Add
	#ifdef GROUP_MATCH
	sys_log(0, "<shutdown> Destroying CGroupMatchManager...");
	groupmatch_manager.Destroy();
	#endif