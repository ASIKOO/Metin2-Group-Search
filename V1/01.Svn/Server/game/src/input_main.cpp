//Find
#include "protocol.h"

///Add
#ifdef GROUP_MATCH
#include "GroupMatchManager.h"
extern const char* EnglishTranslate[];
#endif

//Find
void CInputMain::ItemMove(LPCHARACTER ch, const char * data)
{
	struct command_item_move * pinfo = (struct command_item_move *) data;

	if (ch)
		ch->MoveItem(pinfo->Cell, pinfo->CellTo, pinfo->count);
}

///Add
#ifdef GROUP_MATCH
void CInputMain::GroupMatch(LPCHARACTER ch, const char * data)
{
    grup_paketi * p = (grup_paketi*) data;
	int index = p->index;
	int ayar = p->ayar;
	
	if (ch)
	{
		if (ayar == 1)
		{
			CGroupMatchManager::instance().AddToControl(ch, index);
		}
		else
		{
			CGroupMatchManager::instance().AramayiDurdur(ch->GetPlayerID());
			#ifdef CONVERT_TO_ENGLISH
			ch->ChatPacket(CHAT_TYPE_INFO, EnglishTranslate[4]);
			#else
			ch->ChatPacket(CHAT_TYPE_INFO, "Arama iptal edildi.");
			#endif
			ch->ChatPacket(CHAT_TYPE_COMMAND, "gorup_match_search 0 %d", index);
		}
	}
}
#endif

//Find
		case HEADER_CG_ITEM_MOVE:
			if (!ch->IsObserverMode())
				ItemMove(ch, c_pData);
			break;
			
///Add
		#ifdef GROUP_MATCH
		case HEADER_CG_GROUP_MATCH:
            if (!ch->IsObserverMode())
                GroupMatch(ch, c_pData);
        break;
		#endif