import random
from utils.helpers import send_champion_info, get_random_champion, get_random_team_comp


async def random_all_champions(message_channel, champions):
    """Random 1 tướng bất kỳ"""
    champ_key, champ = get_random_champion(champions)
    if champ:
        await send_champion_info(message_channel, champ, prefix="🎲 **Random tướng:** ")
    else:
        await message_channel.send("Không có tướng nào trong data!")


async def random_by_role(message_channel, role, meta_by_role, champions):
    """Random 1 tướng theo role"""
    champs_keys = meta_by_role.get(role, [])
    if not champs_keys:
        await message_channel.send(f"Không có tướng meta cho role **{role}**!")
        return
    
    random_key = random.choice(champs_keys)
    champ = champions[random_key]
    await send_champion_info(message_channel, champ, prefix=f"🎲 **Random {role}:** ")


async def random_team(message_channel, meta_by_role, champions):
    """Random đội hình 5 tướng (1 cho mỗi vị trí)"""
    team = get_random_team_comp(meta_by_role, champions)
    
    # Tạo text hiển thị
    role_names = {
        "top": "🛡️ Top",
        "jg": "🌲 Jungle",
        "mid": "⚔️ Mid",
        "ad": "🏹 ADC",
        "sp": "💚 Support"
    }
    
    team_text = "**🎲 RANDOM ĐỘI HÌNH 5 TƯỚNG**\n\n"
    for role in ["top", "jg", "mid", "ad", "sp"]:
        champ_key, champ = team[role]
        if champ:
            team_text += f"{role_names[role]}: **{champ['name']}**\n"
        else:
            team_text += f"{role_names[role]}: *Không có dữ liệu*\n"
    
    team_text += "\n💡 Tag bot với tên tướng để xem build chi tiết!"
    
    await message_channel.send(team_text)
