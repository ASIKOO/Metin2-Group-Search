//Find
#include "DragonSoul.h"

///Add
#ifdef GROUP_MATCH
#include "GroupMatchManager.h"
extern const char* EnglishTranslate[];
#endif

//Find in ACMD(do_event_flag)
str_to_number(value, arg2);

///Add
	#ifdef GROUP_MATCH
	if (!strcmp(arg1, "group_match_giris"))
	{
		if (value != 0)
		{
			#ifdef CONVERT_TO_ENGLISH
			ch->ChatPacket(CHAT_TYPE_INFO, EnglishTranslate[11]);
			#else
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("group girisleri acildi"));
			#endif
		}
		else
		{
			#ifdef CONVERT_TO_ENGLISH
			ch->ChatPacket(CHAT_TYPE_INFO, EnglishTranslate[10]);
			#else
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("group girisleri kapatildi"));
			#endif
		}
	}
	#ifdef ENABLE_SEND_SHOUT
	else if (!strcmp(arg1, "group_notice"))
	{
		if (value != 0)
		{
			#ifdef CONVERT_TO_ENGLISH
			ch->ChatPacket(CHAT_TYPE_INFO, EnglishTranslate[12]);
			#else
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("<Gurup Aramas1"));
			#endif
		}
		else
		{
			#ifdef CONVERT_TO_ENGLISH
			ch->ChatPacket(CHAT_TYPE_INFO, EnglishTranslate[13]);
			#else
			ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("<Gurup Aramas2"));
			#endif
		}
	}
	#endif
	#endif