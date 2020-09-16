//Find
		bool SendItemMovePacket(TItemPos pos, TItemPos change_pos, BYTE num);

///Add
#if defined(ENABLE_PARTY_MATCH)
		bool PartyMatch(int index, BYTE setting);
		bool RecvPartyMatch();
#endif

//Find
		void __DirectEnterMode_Initialize();
		
///Add
#if defined(ENABLE_PARTY_MATCH)
		struct PartyMatchInfo 
		{
			int limit_level;
			std::vector<std::pair<int, int>> items;
		};
		std::unordered_map<int, std::shared_ptr<PartyMatchInfo>> m_PartyMatch;
#endif

//Find
		DWORD EXPORT_GetBettingGuildWarValue(const char* c_szValueName);
		
///Add
#if defined(ENABLE_PARTY_MATCH)
		bool LoadPartyMatchInfo(const char* FileName);
		const decltype(m_PartyMatch)& GetPartyMatchInfo() const { return m_PartyMatch; };
#endif