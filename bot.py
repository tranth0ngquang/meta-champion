import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

# Load environment variables từ file .env
load_dotenv()

# ========== 1. TOKEN BOT ==========
# Token được lấy từ biến môi trường, an toàn hơn hardcode
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    print("❌ CẢNH BÁO: Không tìm thấy DISCORD_TOKEN!")
    print("Hãy tạo file .env hoặc set biến môi trường DISCORD_TOKEN")
    exit(1)


# ========== 2. INTENTS ==========
intents = discord.Intents.default()
intents.message_content = True  # bắt buộc bật để bot đọc được nội dung tin nhắn

bot = commands.Bot(command_prefix="!", intents=intents)


# ========== 3. DATA TƯỚNG / ẢNH / NOTE ==========

# Bạn chỉnh sửa lại data này theo list tướng + ảnh của bạn
# Mỗi tướng có thể có nhiều ảnh (dạng list)
CHAMPIONS = {
    # 1
    "anivia": {
        "name": "Anivia",
        "role": "mid",
        "images": ["images/anivia.webp", "images/anivia-01.webp", "images/anivia-02.webp"],
        "note": "Thứ tự nâng skill winrate cao là: E > W > Q. Combo là R -> W -> Q"
    },
    # 2
    "annie": {
        "name": "Annie",
        "role": "mid",
        "images": ["images/annie.webp"],
        "note": "Annie có combo burst cao, dễ chơi, phù hợp gank với stun."
    },
    # 3
    "ashe": {
        "name": "Ashe",
        "role": "ad",
        "images": ["images/ashe.webp"],
        "note": "Ashe nhớ lấy ngọc giày free và cái vận tốc tiếp cận. Đi chung với milio"
    },
    # 4
    "cassiopeia": {
        "name": "Cassiopeia",
        "role": "top",
        "images": ["images/cassiopeia.webp"],
        "note": "Cassiopeia DPS cao, mạnh ở đấu kéo dài, cần kỹ năng kiting tốt."
    },
    # 5
    "diana": {
        "name": "Diana",
        "role": "jg",
        "images": ["images/diana.webp"],
        "note": "Diana là assassin/fighter mạnh về đột kích và team fight."
    },
    # 6
    "garen": {
        "name": "Garen",
        "role": "top",
        "images": ["images/garen.webp", "images/garen-01.webp"],
        "note": "Garen dễ chơi, tanky, sát thương true damage với ultimate."
    },
    # 7
    "graves": {
        "name": "Graves",
        "role": "jg",
        "images": ["images/graves.webp"],
        "note": "Graves farm nhanh, mạnh đầu giữa game, phù hợp carry."
    },
    # 8
    "gwen": {
        "name": "Gwen",
        "role": "jg",
        "images": ["images/gwen.webp", "images/gwen-01.webp"],
        "note": "Gwen mạnh về true damage và bất tử trong W, cần scale."
    },
    # 9
    "jax": {
        "name": "Jax",
        "role": "top",
        "images": ["images/jax.webp"],
        "note": "Jax scale mạnh late game, cần farm an toàn đầu game."
    },
    # 10
    "jinx": {
        "name": "Jinx",
        "role": "ad",
        "images": ["images/jinx.webp"],
        "note": "Jinx cần team bảo kê, giữ vị trí, chờ reset là tự gánh, đi chung LULU hoặc MILIO"
    },
    # 11
    "kassadin": {
        "name": "Kassadin",
        "role": "mid",
        "images": ["images/kassadin.webp"],
        "note": "Kassadin yếu đầu game, cực mạnh sau level 16, counter mage."
    },
    # 12
    "khazix": {
        "name": "Kha'Zix",
        "role": "jg",
        "images": ["images/khazix.webp"],
        "note": "Kha'Zix assassin mạnh về tách đơn và một chọi một."
    },
    # 13
    "malphite": {
        "name": "Malphite",
        "role": "top",
        "images": ["images/malphite.webp", "images/malphite-01.webp"],
        "note": "Malphite tank, ultimate engage mạnh, counter AD."
    },
    # 14
    "morgana": {
        "name": "Morgana",
        "role": "mid",
        "images": ["images/morgana.webp"],
        "note": "Morgana có Black Shield để bảo vệ đồng đội, CC dài."
    },
    # 15
    "naafiri": {
        "name": "Naafiri",
        "role": "jg",
        "images": ["images/naafiri.webp", "images/naafiri-01.webp"],
        "note": "Naafiri assassin mạnh về roam và gank, đột kích nhanh."
    },
    # 16
    "rammus": {
        "name": "Rammus",
        "role": "jg",
        "images": ["images/rammus.webp", "images/rammus-01.webp"],
        "note": "Rammus tank, gank cực nhanh, counter AD carry, thứ tự nâng skill Q E W"
    },
    # 17
    "sion": {
        "name": "Sion",
        "role": "top",
        "images": ["images/sion.webp"],
        "note": "Sion tank với HP khổng lồ, mạnh về engage và split push."
    },
    # 18
    "syndra": {
        "name": "Syndra",
        "role": "mid",
        "images": ["images/syndra.webp"],
        "note": "Syndra burst damage cao, lane bully, khống chế tốt."
    },
    # 19
    "tryndamere": {
        "name": "Tryndamere",
        "role": "top",
        "images": ["images/tryndamere.webp"],
        "note": "Tryndamere mạnh về split push và 1v1, bất tử 5 giây với R."
    },
    # 20
    "vayne": {
        "name": "Vayne",
        "role": "top",
        "images": ["images/vayne.webp", "images/vayne-01.webp"],
        "note": "Vayne mạnh late game với true damage, yếu đầu game."
    },
    # 21
    "velkoz": {
        "name": "Vel'Koz",
        "role": "mid",
        "images": ["images/velkoz.webp"],
        "note": "Vel'Koz poke damage cao, true damage với passive."
    },
    # 22
    "yasuo": {
        "name": "Yasuo",
        "role": "mid",
        "images": ["images/yasuo.webp", "images/yasuo-01.webp"],
        "note": "Yasuo cần skill cao, mạnh khi có knockup từ team."
    },
    # 23
    "zed": {
        "name": "Zed",
        "role": "mid",
        "images": ["images/zed.webp"],
        "note": "Zed assassin mạnh về một chọi một, cần skill để outplay."
    },
    # 24
    "ziggs": {
        "name": "Ziggs",
        "role": "mid",
        "images": ["images/ziggs.webp"],
        "note": "Ziggs poke và wave clear mạnh, phá turret nhanh."
    },
    # 25
    "volibear": {
        "name": "Volibear",
        "role": "top",
        "images": [],
        "note": "Volibear tam hợp, đoản đao, giáp tâm linh"
    },
    # 26
    "yone": {
        "name": "Yone",
        "role": "top",
        "images": ["images/yone.png"],
        "note": "đi top vì nó mạnh"
    },
    # 27
        "nami": {
        "name": "Nami",
        "role": "sp",
        "images": ["images/nami.png"],
        "note": "Hỗ trợ mạnh với khả năng hồi máu và khống chế."
    },
    # 28
        "milio": {
        "name": "Milio",
        "role": "sp",
        "images": ["images/milio.png"],
        "note": "Hỗ trợ mạnh với khả năng hồi máu và khống chế."
    },
    # thêm tướng khác ở đây...
}

META_BY_ROLE = {
    "top": ["garen", "malphite", "sion", "tryndamere", "volibear", "yone", "vayne", "cassiopeia"],
    "jg": ["diana", "graves", "khazix", "rammus", "gwen", "jax", "naafiri"],
    "mid": ["anivia", "annie", "kassadin", "syndra", "yasuo", "zed", "velkoz","morgana"],
    "ad": ["ashe", "jinx", "ziggs"],
    "sp": ["nami","milio"],
}


# ========== 4. EVENT: BOT ONLINE ==========
@bot.event
async def on_ready():
    print(f"Bot đã đăng nhập: {bot.user} (ID: {bot.user.id})")
    print(f"Bot đang online trong {len(bot.guilds)} server(s)")


# ========== LỆNH PING ĐỂ TEST ==========
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")


# ========== 5. XỬ LÝ MENTION BOT ==========
@bot.event
async def on_message(message: discord.Message):
    # Không xử lý tin nhắn của chính bot
    if message.author == bot.user:
        return

    # Debug: in ra mọi tin nhắn để xem bot có nhận được không
    print(f"[DEBUG] Nhận tin nhắn từ {message.author}: {message.content}")

    # Nếu bot bị mention trong message
    if bot.user in message.mentions:
        print(f"[DEBUG] Bot được mention!")
        # Bỏ phần mention, chỉ lấy phần text phía sau
        content = message.content
        # loại cả 2 dạng mention <@id> và <@!id>
        content = content.replace(f"<@{bot.user.id}>", "")
        content = content.replace(f"<@!{bot.user.id}>", "")
        content = content.strip().lower()
        print(f"[DEBUG] Nội dung sau khi xử lý: '{content}'")

        # ================= CASE -1: @bot help / hướng dẫn =================
        if content == "help" or content == "huongdan" or content == "hướng dẫn" or content == "h":
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

**4️⃣ Xem build tướng cụ thể:**
• `@meta-champion anivia`
• `@meta-champion jinx`
• `@meta-champion yasuo`
(Tên tướng viết thường, không dấu, viết liền)

**5️⃣ Test bot:**
• `!ping`

**6️⃣ Xem hướng dẫn:**
• `@meta-champion help` hoặc `h`
"""
            await message.channel.send(help_text)
            return

        # ================= CASE 0: @bot random all =================
        if content == "random all" or content == "randomall" or content == "rdall":
            # Chọn ngẫu nhiên 1 tướng từ tất cả tướng
            all_champ_keys = list(CHAMPIONS.keys())
            if not all_champ_keys:
                await message.channel.send("Không có tướng nào trong data!")
                return
            
            random_key = random.choice(all_champ_keys)
            champ = CHAMPIONS[random_key]
            
            images = champ["images"]
            note = champ["note"]
            name = champ["name"]
            role = champ["role"]

            # Gửi tất cả ảnh của tướng
            files_to_send = []
            for image_path in images:
                if os.path.exists(image_path):
                    files_to_send.append(discord.File(image_path, filename=os.path.basename(image_path)))

            if files_to_send:
                caption = (
                    f"🎲 **Random tướng:** **{name}** ({role})\n"
                    f"**Ghi chú:** {note}\n"
                    f"**Số lượng ảnh:** {len(files_to_send)}"
                )
                await message.channel.send(content=caption, files=files_to_send)
            else:
                await message.channel.send(f"🎲 Random được **{name}** ({role}) nhưng không tìm thấy ảnh!")
            return

        # ================= CASE 0.5: @bot random <role> =================
        # Hỗ trợ cả lệnh đầy đủ và viết tắt
        random_shortcuts = {
            "rdad": "ad",
            "rdmid": "mid",
            "rdjg": "jg",
            "rdtop": "top",
            "rdsp": "sp"
        }
        
        # Kiểm tra lệnh viết tắt
        role_to_random = None
        if content in random_shortcuts:
            role_to_random = random_shortcuts[content]
        elif content.startswith("random"):
            parts = content.split()
            if len(parts) >= 2:
                role_to_random = parts[1].replace("(", "").replace(")", "")
        
        if role_to_random:
            champs_keys = META_BY_ROLE.get(role_to_random, [])
            if not champs_keys:
                await message.channel.send(f"Không có tướng meta cho role **{role_to_random}**!")
                return
            
            # Random 1 tướng từ role đó
            random_key = random.choice(champs_keys)
            champ = CHAMPIONS[random_key]
            
            images = champ["images"]
            note = champ["note"]
            name = champ["name"]

            # Gửi tất cả ảnh của tướng
            files_to_send = []
            for image_path in images:
                if os.path.exists(image_path):
                    files_to_send.append(discord.File(image_path, filename=os.path.basename(image_path)))

            if files_to_send:
                caption = (
                    f"🎲 **Random {role_to_random}:** **{name}**\n"
                    f"**Ghi chú:** {note}\n"
                    f"**Số lượng ảnh:** {len(files_to_send)}"
                )
                await message.channel.send(content=caption, files=files_to_send)
            else:
                await message.channel.send(f"🎲 Random được **{name}** ({role_to_random}) nhưng không tìm thấy ảnh!")
            return

        # ================= CASE 1: @bot role ad =================
        # Hỗ trợ cả lệnh đầy đủ và viết tắt
        role_shortcuts = {
            "rad": "ad",
            "rmid": "mid",
            "rjg": "jg",
            "rtop": "top",
            "rsp": "sp"
        }
        
        # Kiểm tra lệnh viết tắt
        role_to_show = None
        if content in role_shortcuts:
            role_to_show = role_shortcuts[content]
        elif content.startswith("role"):
            parts = content.split()
            if len(parts) >= 2:
                raw_role = parts[1]
                role_to_show = raw_role.replace("(", "").replace(")", "")
        
        if role_to_show:
            champs_keys = META_BY_ROLE.get(role_to_show, [])
            if not champs_keys:
                await message.channel.send(f"Hiện không có tướng meta cho role **{role_to_show}** (trong data của mình).")
                return

            champ_names = []
            for key in champs_keys:
                champ = CHAMPIONS.get(key)
                if champ:
                    champ_names.append(f"- {champ['name']}")

            reply = (
                f"Tướng meta cho role **{role_to_show}**:\n"
                + "\n".join(champ_names)
                + "\n\nTag mình với tên tướng để xem ảnh build, ví dụ:\n"
                f"`@{bot.user.name} anivia`"
            )
            await message.channel.send(reply)
            return

        # ================= CASE 2: @bot leesin =================
        # coi phần content còn lại là tên tướng
        champ_key = content.replace(" ", "")  # đề phòng gõ "lee sin"
        champ = CHAMPIONS.get(champ_key)

        if champ:
            images = champ["images"]  # Đây là list các ảnh
            note = champ["note"]
            name = champ["name"]
            role = champ["role"]

            # Gửi tất cả ảnh của tướng
            files_to_send = []
            for image_path in images:
                if not os.path.exists(image_path):
                    await message.channel.send(
                        f"⚠️ Không tìm thấy file ảnh tại: `{image_path}`"
                    )
                    continue
                files_to_send.append(discord.File(image_path, filename=os.path.basename(image_path)))

            if files_to_send:
                caption = (
                    f"**{name}** ({role})\n"
                    f"**Ghi chú:** {note}\n"
                    f"**Số lượng ảnh:** {len(files_to_send)}"
                )
                await message.channel.send(content=caption, files=files_to_send)
            else:
                await message.channel.send(
                    f"Không tìm thấy file ảnh nào cho tướng **{name}**. Kiểm tra lại đường dẫn nhé."
                )
        else:
            await message.channel.send(
                "Không tìm thấy tướng trong data. Thử lại với key đơn giản, ví dụ: `anivia`, `jinx`, `yasuo`."
            )

    # Đảm bảo các command khác (nếu sau này bạn thêm) vẫn hoạt động
    await bot.process_commands(message)


# ========== 6. CHẠY BOT ==========
if __name__ == "__main__":
    print("Đang khởi động bot...")
    bot.run(TOKEN)
