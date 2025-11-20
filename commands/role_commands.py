async def show_role_meta(message_channel, role, meta_by_role, champions, bot_user_name):
    """Hiển thị danh sách tướng meta theo role"""
    champs_keys = meta_by_role.get(role, [])
    if not champs_keys:
        await message_channel.send(f"Hiện không có tướng meta cho role **{role}**!")
        return

    champ_names = []
    for key in champs_keys:
        champ = champions.get(key)
        if champ:
            champ_names.append(f"- {champ['name']}")

    reply = (
        f"Tướng meta cho role **{role}**:\n"
        + "\n".join(champ_names)
        + "\n\nTag mình với tên tướng để xem ảnh build, ví dụ:\n"
        f"`@{bot_user_name} anivia`"
    )
    await message_channel.send(reply)
