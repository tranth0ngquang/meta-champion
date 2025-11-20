import os
import discord
from utils.helpers import send_champion_info


async def show_champion_build(message_channel, champ_key, champions):
    """Hiển thị build của tướng cụ thể"""
    champ = champions.get(champ_key)
    
    if not champ:
        await message_channel.send(
            "Không tìm thấy tướng trong data. Thử lại với key đơn giản, ví dụ: `anivia`, `jinx`, `yasuo`."
        )
        return
    
    await send_champion_info(message_channel, champ)
