import os
from dotenv import load_dotenv

# Load environment variables từ file .env
load_dotenv()

# ========== BOT SETTINGS ==========
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = "!"

# Kiểm tra token
if not DISCORD_TOKEN:
    print("❌ CẢNH BÁO: Không tìm thấy DISCORD_TOKEN!")
    print("Hãy tạo file .env hoặc set biến môi trường DISCORD_TOKEN")
    exit(1)

# ========== COMMAND SHORTCUTS ==========
ROLE_SHORTCUTS = {
    "rad": "ad",
    "rmid": "mid",
    "rjg": "jg",
    "rtop": "top",
    "rsp": "sp"
}

RANDOM_SHORTCUTS = {
    "rdad": "ad",
    "rdmid": "mid",
    "rdjg": "jg",
    "rdtop": "top",
    "rdsp": "sp"
}
