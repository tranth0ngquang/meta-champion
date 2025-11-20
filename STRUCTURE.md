# 📁 CẤU TRÚC CODE & HƯỚNG DẪN BẢO TRÌ

## Tổng quan cấu trúc

Project được chia thành các module riêng biệt để dễ quản lý và mở rộng:

```
lol-discord-bot/
├── bot.py                    # File chính - khởi chạy bot
├── config/                   # Cấu hình
│   └── settings.py          # Token, prefix, shortcuts
├── data/                     # Dữ liệu
│   └── champions.py         # Thông tin tướng, meta
├── commands/                 # Logic xử lý lệnh
│   ├── help_command.py      # Lệnh help
│   ├── random_commands.py   # Random (all, role, team)
│   ├── role_commands.py     # Xem meta theo role
│   └── champion_commands.py # Xem build tướng
└── utils/                    # Hàm tiện ích
    └── helpers.py           # Hàm helper chung
```

---

## Chi tiết từng module

### 1. `bot.py` - File chính
**Chức năng:**
- Khởi tạo Discord bot
- Xử lý event `on_ready` và `on_message`
- Điều hướng request đến các command handler

**Khi nào sửa:**
- Thêm event mới của Discord
- Thay đổi logic điều hướng command
- Thêm lệnh mới (cần import và gọi function)

---

### 2. `config/settings.py` - Cấu hình
**Chứa:**
- `DISCORD_TOKEN`: Token bot (từ .env)
- `COMMAND_PREFIX`: Prefix cho command (!)
- `ROLE_SHORTCUTS`: Dict mapping lệnh viết tắt cho role
- `RANDOM_SHORTCUTS`: Dict mapping lệnh viết tắt cho random

**Khi nào sửa:**
- Thêm/sửa lệnh viết tắt
- Thay đổi prefix command
- Thêm cấu hình mới

**Ví dụ thêm shortcut:**
```python
ROLE_SHORTCUTS = {
    "rad": "ad",
    "rmid": "mid",
    "rnew": "newrole"  # Thêm shortcut mới
}
```

---

### 3. `data/champions.py` - Dữ liệu tướng
**Chứa:**
- `CHAMPIONS`: Dict chứa thông tin tất cả tướng
- `META_BY_ROLE`: Dict phân loại tướng meta theo role

**Khi nào sửa:**
- Thêm tướng mới
- Cập nhật ảnh build
- Sửa note/thông tin tướng
- Cập nhật meta theo patch

**Ví dụ thêm tướng:**
```python
"newchamp": {
    "name": "New Champion",
    "role": "mid",
    "images": ["images/newchamp.webp"],
    "note": "Ghi chú về tướng này"
}
```

Nhớ thêm vào `META_BY_ROLE`:
```python
META_BY_ROLE = {
    "mid": ["anivia", "annie", "newchamp"],  # Thêm vào đây
    ...
}
```

---

### 4. `commands/` - Xử lý lệnh

#### 4.1. `help_command.py`
**Function:** `show_help(message_channel)`
- Hiển thị hướng dẫn sử dụng bot

**Khi nào sửa:**
- Thêm lệnh mới vào hướng dẫn
- Cập nhật text hướng dẫn

#### 4.2. `random_commands.py`
**Functions:**
- `random_all_champions()`: Random 1 tướng bất kỳ
- `random_by_role()`: Random 1 tướng theo role
- `random_team()`: Random đội hình 5 tướng

**Khi nào sửa:**
- Thay đổi format hiển thị
- Thêm logic random mới
- Thay đổi emoji/icon

#### 4.3. `role_commands.py`
**Function:** `show_role_meta()`
- Hiển thị danh sách tướng meta theo role

**Khi nào sửa:**
- Thay đổi format hiển thị danh sách
- Thêm thông tin meta

#### 4.4. `champion_commands.py`
**Function:** `show_champion_build()`
- Hiển thị build của tướng cụ thể

**Khi nào sửa:**
- Thay đổi format hiển thị ảnh
- Thêm thông tin chi tiết

---

### 5. `utils/helpers.py` - Hàm tiện ích

**Functions:**
- `get_champion_files()`: Lấy danh sách file ảnh
- `send_champion_info()`: Gửi thông tin tướng với ảnh
- `get_random_champion()`: Random 1 tướng
- `get_random_team_comp()`: Random đội hình 5 tướng

**Khi nào sửa:**
- Thêm hàm tiện ích mới
- Tối ưu code chung
- Thay đổi logic xử lý file/data

---

## Quy trình thêm tính năng mới

### Ví dụ: Thêm lệnh "random 3 tướng cùng role"

**Bước 1:** Tạo function trong `commands/random_commands.py`
```python
async def random_three_by_role(message_channel, role, meta_by_role, champions):
    """Random 3 tướng cùng role"""
    champs_keys = meta_by_role.get(role, [])
    if len(champs_keys) < 3:
        await message_channel.send("Không đủ tướng để random!")
        return
    
    selected = random.sample(champs_keys, 3)
    # ... logic hiển thị
```

**Bước 2:** Import trong `bot.py`
```python
from commands.random_commands import random_all_champions, random_by_role, random_team, random_three_by_role
```

**Bước 3:** Thêm xử lý trong `on_message()` của `bot.py`
```python
if content.startswith("random3"):
    parts = content.split()
    if len(parts) >= 2:
        role = parts[1]
        await random_three_by_role(message.channel, role, META_BY_ROLE, CHAMPIONS)
    return
```

**Bước 4:** Cập nhật help trong `commands/help_command.py`

---

## Quy trình cập nhật data tướng

### Khi có patch mới/meta thay đổi:

1. **Cập nhật `data/champions.py`:**
   - Thêm tướng mới vào `CHAMPIONS`
   - Cập nhật `META_BY_ROLE`

2. **Thêm ảnh:**
   - Upload ảnh build vào folder `images/`
   - Đặt tên: `tentuong.webp`, `tentuong-01.webp`

3. **Test:**
   ```
   @bot tentuong
   @bot role roletuong
   @bot random roletuong
   ```

---

## Best Practices

### 1. Naming Convention
- File: `snake_case.py`
- Function: `snake_case()`
- Variable: `snake_case`
- Constant: `UPPER_CASE`

### 2. Import Order
```python
# 1. Standard library
import os
import random

# 2. Third-party
import discord
from discord.ext import commands

# 3. Local modules
from config.settings import DISCORD_TOKEN
from data.champions import CHAMPIONS
```

### 3. Code Organization
- Mỗi file chỉ chứa logic liên quan
- Function không quá 50 dòng
- Luôn có docstring cho function
- Tách logic phức tạp thành helper function

### 4. Error Handling
- Kiểm tra data trước khi xử lý
- Gửi message lỗi thân thiện cho user
- Log lỗi để debug

---

## Testing

### Test local:
```bash
python bot.py
```

### Test các lệnh:
1. `!ping` - Test bot online
2. `@bot help` - Test help
3. `@bot role ad` - Test role meta
4. `@bot random ad` - Test random role
5. `@bot rdteam` - Test random team
6. `@bot anivia` - Test champion build

---

## Deploy

Sau khi sửa code, chỉ cần:
```bash
git add .
git commit -m "Mô tả thay đổi"
git push
```

Railway sẽ tự động deploy lại!

---

## Troubleshooting

### Bot không phản hồi?
- Check log terminal: `[DEBUG] Nhận tin nhắn từ...`
- Check biến môi trường `DISCORD_TOKEN`
- Check Message Content Intent trong Discord Portal

### Import error?
- Đảm bảo có file `__init__.py` trong mỗi folder
- Check đường dẫn import
- Check Python version (cần 3.11+)

### Ảnh không hiển thị?
- Check file tồn tại trong folder `images/`
- Check đường dẫn trong `CHAMPIONS`
- Check quyền bot upload file trong Discord
