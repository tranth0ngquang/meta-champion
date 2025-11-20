async def show_help(message_channel):
    """Hiển thị hướng dẫn sử dụng bot"""
    help_text = """
**📚 HƯỚNG DẪN SỬ DỤNG BOT**

**1️⃣ Xem tướng meta theo role:**
• `@meta-champion role ad` hoặc `rad`
• `@meta-champion role mid` hoặc `rmid`
• `@meta-champion role jg` hoặc `rjg`
• `@meta-champion role top` hoặc `rtop`
• `@meta-champion role sp` hoặc `rsp`

**2️⃣ Random tướng theo role:**
• `@meta-champion random ad` hoặc `rdad`
• `@meta-champion random mid` hoặc `rdmid`
• `@meta-champion random jg` hoặc `rdjg`
• `@meta-champion random top` hoặc `rdtop`
• `@meta-champion random sp` hoặc `rdsp`

**3️⃣ Random tướng bất kỳ:**
• `@meta-champion random all` hoặc `rdall`

**4️⃣ Random đội hình 5 tướng:**
• `@meta-champion random team` hoặc `rdteam` hoặc `rd5`

**5️⃣ Xem build tướng cụ thể:**
• `@meta-champion anivia`
• `@meta-champion jinx`
• `@meta-champion yasuo`
(Tên tướng viết thường, không dấu, viết liền)

**6️⃣ Test bot:**
• `!ping`

**7️⃣ Xem hướng dẫn:**
• `@meta-champion help` hoặc `h`
"""
    await message_channel.send(help_text)
