//Find
bool CPythonNetworkStream::SendShootPacket(UINT uSkill)
{
	TPacketCGShoot kPacketShoot;
	kPacketShoot.bHeader=HEADER_CG_SHOOT;
	kPacketShoot.bType=uSkill;

	if (!Send(sizeof(kPacketShoot), &kPacketShoot))
	{
		Tracen("SendShootPacket Error");
		return false;
	}

	return SendSequence();
}

///Add
#ifdef GROUP_MATCH
bool CPythonNetworkStream::GroupMatchh(BYTE index, BYTE ayar)
{
	if (!__CanActMainInstance())
		return true;

	TPacketCGGrup packet;
	packet.header = HEADER_CG_GROUP_MATCH;
	packet.index = index;
	packet.ayar = ayar;
	if (!Send(sizeof(packet), &packet))
	{
		Tracen("Error in CPythonNetworkStream::Group_Match");
		return false;
	}

	return SendSequence();
}
#endif