-- Created by Blackdragonx618
quest group_search begin
	state start begin
		when letter with pc.is_gm() begin
			send_letter(gameforge.group_search._001_npcChat)
		end
		when info or button with pc.is_gm() begin
			say_title(gameforge.group_search.hiii_say..pc.get_name()..":")
			local secenekler = select(gameforge.group_search._050_say,gameforge.group_search._060_say,gameforge.group_search._061_say,gameforge.group_search._070_say)
			if secenekler == 4 then
				send_letter(gameforge.group_search._001_npcChat)
				return
			else if secenekler == 3 then
				local durum2 = game.get_event_flag("group_notice")
				if group_match.is_send_shout() == 0 then
					say(gameforge.group_search._099_say)
				else
					if durum2 == 0 then
						say(gameforge.group_search._092_say)
						say("")
						local ac = select(locale.yes,locale.no)
						if ac == 1 then
							chat(gameforge.group_search._096_say)
							game.set_event_flag("group_notice",1)
						end
						send_letter(gameforge.group_search._001_npcChat)
					else
						say(gameforge.group_search._093_say)
						say("")
						local ac2 = select(locale.yes,locale.no)
						if ac2 == 1 then
							chat(gameforge.group_search._097_say)
							game.set_event_flag("group_notice",0)
						end
						send_letter(gameforge.group_search._001_npcChat)
					end
				end
			else if secenekler == 2 then
				local durum = game.get_event_flag("group_match_giris")
				if durum == 0 then
					say(gameforge.group_search._080_say)
					say("")
					local ac = select(locale.yes,locale.no)
					if ac == 1 then
						chat(gameforge.group_search._094_say)
						game.set_event_flag("group_match_giris",1)
					end
					send_letter(gameforge.group_search._001_npcChat)
				else
					say(gameforge.group_search._090_say)
					say("")
					local ac2 = select(locale.yes,locale.no)
					if ac2 == 1 then
						chat(gameforge.group_search._095_say)
						game.set_event_flag("group_match_giris",0)
					end
					send_letter(gameforge.group_search._001_npcChat)
				end
			else if secenekler == 1 then
				local secenekler2 = select(group_match.dungeon_name(0),group_match.dungeon_name(1),group_match.dungeon_name(2),group_match.dungeon_name(3),group_match.dungeon_name(4),group_match.dungeon_name(5),gameforge.group_search._070_say)
				if secenekler2 == 7 then
					return
				else if secenekler2 == 3 or secenekler2 == 5 then
					say(string.format(gameforge.group_search._010_say, group_match.giris_levelleri(secenekler2 - 1)))
					if group_match.is_new_need_items() == 1 then
						say(string.format(gameforge.group_search._020_say,group_match.ayarlar_itemler_count(secenekler2 - 1), item_name(group_match.ayarlar_itemler(secenekler2 - 1))))
					end
					say(string.format(gameforge.group_search._030_say, group_match.ayarlar_giris(secenekler2 - 1)))
					say(string.format(gameforge.group_search._035_say, group_match.ayarlar_kayitlar(secenekler2 - 1)))
				else if secenekler2 == 1 then 
					say(string.format(gameforge.group_search._010_say, group_match.giris_levelleri(secenekler2 - 1)))
					say(string.format(gameforge.group_search._020_say, group_match.ayarlar_itemler_count(secenekler2 - 1), item_name(group_match.ayarlar_itemler(secenekler2 - 1))))
					say(string.format(gameforge.group_search._040_say, group_match.ayarlar_itemler_count(6), item_name(group_match.ayarlar_itemler(6))))
					say(string.format(gameforge.group_search._030_say, group_match.ayarlar_giris(secenekler2 - 1)))
					say(string.format(gameforge.group_search._035_say, group_match.ayarlar_kayitlar(secenekler2 - 1)))
				else
					say(string.format(gameforge.group_search._010_say, group_match.giris_levelleri(secenekler2 - 1)))
					say(string.format(gameforge.group_search._020_say, group_match.ayarlar_itemler_count(secenekler2 - 1), item_name(group_match.ayarlar_itemler(secenekler2 - 1))))
					say(string.format(gameforge.group_search._030_say, group_match.ayarlar_giris(secenekler2 - 1)))
					say(string.format(gameforge.group_search._035_say, group_match.ayarlar_kayitlar(secenekler2 - 1)))
				end
		end end end end end end end
	end
end