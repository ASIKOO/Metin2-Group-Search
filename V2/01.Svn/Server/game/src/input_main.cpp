///Add
#if defined(ENABLE_PARTY_MATCH)
#include "GroupMatchManager.h"
void CInputMain::PartyMatch(LPCHARACTER ch, const char* data)
{
	if (!ch)
		return;

	const auto pinfo = reinterpret_cast<const TPacketCGPartyMatch*>(data);

	if (pinfo->SubHeader == CGroupMatchManager::eHeader::PARTY_MATCH_SEARCH)
		CGroupMatchManager::instance().AddSearcher(ch, pinfo->index);
	else
		CGroupMatchManager::instance().StopSearching(ch, CGroupMatchManager::eMSG::PARTY_MATCH_CANCEL_SUCCESS, pinfo->index);
}
#endif

//Find
		case HEADER_CG_ITEM_MOVE:
			if (!ch->IsObserverMode())
				ItemMove(ch, c_pData);
			break;
			
///Add
#if defined(ENABLE_PARTY_MATCH)
		case HEADER_CG_PARTY_MATCH:
			if (!ch->IsObserverMode())
				PartyMatch(ch, c_pData);
			break;
#endif