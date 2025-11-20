import os
import discord
import random
from typing import List, Dict, Tuple

def get_champion_files(champ: Dict, message_channel) -> Tuple[List[discord.File], int]:
    """
    Lấy danh sách file ảnh của tướng
    
    Returns:
        Tuple[List[discord.File], int]: (danh sách file, số lượng file hợp lệ)
    """
    images = champ["images"]
    files_to_send = []
    
    for image_path in images:
        if os.path.exists(image_path):
            files_to_send.append(discord.File(image_path, filename=os.path.basename(image_path)))
    
    return files_to_send, len(files_to_send)


async def send_champion_info(message_channel, champ: Dict, prefix: str = ""):
    """
    Gửi thông tin và ảnh của tướng
    
    Args:
        message_channel: Discord channel để gửi tin nhắn
        champ: Dictionary chứa thông tin tướng
        prefix: Tiền tố cho caption (ví dụ: "🎲 Random top:")
    """
    images = champ["images"]
    note = champ["note"]
    name = champ["name"]
    role = champ["role"]

    files_to_send = []
    for image_path in images:
        if os.path.exists(image_path):
            files_to_send.append(discord.File(image_path, filename=os.path.basename(image_path)))

    if files_to_send:
        caption = f"{prefix}**{name}** ({role})\n**Ghi chú:** {note}\n**Số lượng ảnh:** {len(files_to_send)}"
        await message_channel.send(content=caption, files=files_to_send)
    else:
        await message_channel.send(f"{prefix}**{name}** ({role}) - Không tìm thấy ảnh!")


def get_random_champion(champions: Dict, role: str = None) -> Tuple[str, Dict]:
    """
    Random một tướng (có thể theo role)
    
    Args:
        champions: Dictionary chứa tất cả tướng
        role: Role cụ thể (None = random tất cả)
    
    Returns:
        Tuple[str, Dict]: (key của tướng, data tướng)
    """
    if role:
        # Filter champions by role
        champs_in_role = {k: v for k, v in champions.items() if v["role"] == role}
        if not champs_in_role:
            return None, None
        champ_key = random.choice(list(champs_in_role.keys()))
        return champ_key, champs_in_role[champ_key]
    else:
        champ_key = random.choice(list(champions.keys()))
        return champ_key, champions[champ_key]


def get_random_team_comp(meta_by_role: Dict, champions: Dict) -> Dict[str, Tuple[str, Dict]]:
    """
    Random đội hình 5 tướng (1 cho mỗi vị trí)
    
    Returns:
        Dict với key là role, value là tuple (champ_key, champ_data)
    """
    team = {}
    roles = ["top", "jg", "mid", "ad", "sp"]
    
    for role in roles:
        champs_keys = meta_by_role.get(role, [])
        if champs_keys:
            random_key = random.choice(champs_keys)
            team[role] = (random_key, champions[random_key])
        else:
            team[role] = (None, None)
    
    return team
