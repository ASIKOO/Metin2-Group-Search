//Find
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

///Add
#ifdef GROUP_MATCH
	PyModule_AddIntConstant(poModule, "PARTY_MATCH",	1);
#else
	PyModule_AddIntConstant(poModule, "PARTY_MATCH",	0);
#endif