import discord
from discord.ext import commands

# Import config và data
from config.settings import DISCORD_TOKEN, COMMAND_PREFIX, ROLE_SHORTCUTS, RANDOM_SHORTCUTS
from data.champions import CHAMPIONS, META_BY_ROLE

# Import commands
from commands.help_command import show_help
from commands.random_commands import random_all_champions, random_by_role, random_team
from commands.role_commands import show_role_meta
from commands.champion_commands import show_champion_build


# ========== INTENTS ==========
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)


# ========== EVENT: BOT ONLINE ==========
@bot.event
async def on_ready():
    print(f"Bot đã đăng nhập: {bot.user} (ID: {bot.user.id})")
    print(f"Bot đang online trong {len(bot.guilds)} server(s)")


# ========== LỆNH PING ĐỂ TEST ==========
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")


# ========== XỬ LÝ MENTION BOT ==========
@bot.event
async def on_message(message: discord.Message):
    # Không xử lý tin nhắn của chính bot
    if message.author == bot.user:
        return

    # Debug log
    print(f"[DEBUG] Nhận tin nhắn từ {message.author}: {message.content}")

    # Nếu bot bị mention
    if bot.user in message.mentions:
        print(f"[DEBUG] Bot được mention!")
        
        # Lấy nội dung sau mention
        content = message.content
        content = content.replace(f"<@{bot.user.id}>", "")
        content = content.replace(f"<@!{bot.user.id}>", "")
        content = content.strip().lower()
        print(f"[DEBUG] Nội dung sau khi xử lý: '{content}'")

        # ================= HELP =================
        if content in ["help", "huongdan", "hướng dẫn", "h"]:
            await show_help(message.channel)
            return

        # ================= RANDOM TEAM (5 tướng) =================
        if content in ["random team", "randomteam", "rdteam", "rd5", "team"]:
            await random_team(message.channel, META_BY_ROLE, CHAMPIONS)
            return

        # ================= RANDOM ALL =================
        if content in ["random all", "randomall", "rdall"]:
            await random_all_champions(message.channel, CHAMPIONS)
            return

        # ================= RANDOM BY ROLE (viết tắt) =================
        if content in RANDOM_SHORTCUTS:
            role = RANDOM_SHORTCUTS[content]
            await random_by_role(message.channel, role, META_BY_ROLE, CHAMPIONS)
            return

        # ================= RANDOM BY ROLE (đầy đủ) =================
        if content.startswith("random"):
            parts = content.split()
            if len(parts) >= 2:
                role = parts[1].replace("(", "").replace(")", "")
                await random_by_role(message.channel, role, META_BY_ROLE, CHAMPIONS)
            else:
                await message.channel.send("Bạn dùng kiểu: `@bot random ad` hoặc `@bot rdad` nha.")
            return

        # ================= ROLE META (viết tắt) =================
        if content in ROLE_SHORTCUTS:
            role = ROLE_SHORTCUTS[content]
            await show_role_meta(message.channel, role, META_BY_ROLE, CHAMPIONS, bot.user.name)
            return

        # ================= ROLE META (đầy đủ) =================
        if content.startswith("role"):
            parts = content.split()
            if len(parts) >= 2:
                role = parts[1].replace("(", "").replace(")", "")
                await show_role_meta(message.channel, role, META_BY_ROLE, CHAMPIONS, bot.user.name)
            else:
                await message.channel.send("Bạn dùng kiểu: `@bot role ad` hoặc `@bot rad` nha.")
            return

        # ================= XEM BUILD TƯỚNG =================
        champ_key = content.replace(" ", "")
        await show_champion_build(message.channel, champ_key, CHAMPIONS)

    # Đảm bảo các command khác vẫn hoạt động
    await bot.process_commands(message)


# ========== CHẠY BOT ==========
if __name__ == "__main__":
    print("Đang khởi động bot...")
    bot.run(DISCORD_TOKEN)
