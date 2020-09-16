//Find
			case HEADER_GC_EXCHANGE:
				ret = RecvExchangePacket();
				break;
				
///Add
#if defined(ENABLE_PARTY_MATCH)
			case HEADER_GC_PARTY_MATCH:
				ret = RecvPartyMatch();
				break;
#endif

//Find
bool CPythonNetworkStream::SendShootPacket(UINT uSkill)
{
	...
}

///Add
#if defined(ENABLE_PARTY_MATCH)
bool CPythonNetworkStream::PartyMatch(int index, BYTE setting)
{
	if (!__CanActMainInstance())
		return true;

	TPacketCGPartyMatch packet;
	packet.Header = HEADER_CG_PARTY_MATCH;
	packet.index = index;
	packet.SubHeader = setting;
	if (!Send(sizeof(packet), &packet))
	{
		Tracen("Error in CPythonNetworkStream::PartyMatch");
		return false;
	}

	return SendSequence();
}
bool CPythonNetworkStream::RecvPartyMatch()
{
	TPacketGCPartyMatch Packet;
	if (!Recv(sizeof(Packet), &Packet)) {
		Tracen("RecvPartyMatch Error");
		return false;
	}

	switch (Packet.SubHeader)
	{
	case CPythonPlayer::PARTY_MATCH_SEARCH:
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "PartyMatchResult", Py_BuildValue("(ii)", Packet.MSG, Packet.index));
		break;
	case CPythonPlayer::PARTY_MATCH_CANCEL:
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "PartyMatchResult", Py_BuildValue("(i(ii))", Packet.SubHeader, Packet.MSG, Packet.index));
		break;
	}

	return true;
}
#endif