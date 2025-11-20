# Discord Bot - League of Legends Meta Champion

Bot Discord để xem tướng meta và build cho League of Legends.

## Tính năng
- Xem danh sách tướng meta theo role
- Random tướng theo role
- Random đội hình 5 tướng (1 cho mỗi vị trí)
- Xem build chi tiết của tướng
- Hỗ trợ lệnh viết tắt

## Cấu trúc project

```
lol-discord-bot/
├── bot.py                 # File chính khởi chạy bot
├── config/
│   ├── __init__.py
│   └── settings.py        # Cấu hình bot (token, shortcuts)
├── data/
│   ├── __init__.py
│   └── champions.py       # Data tướng và meta theo role
├── commands/
│   ├── __init__.py
│   ├── help_command.py    # Lệnh help/hướng dẫn
│   ├── random_commands.py # Lệnh random (all, role, team)
│   ├── role_commands.py   # Lệnh xem meta theo role
│   └── champion_commands.py # Lệnh xem build tướng
├── utils/
│   ├── __init__.py
│   └── helpers.py         # Hàm tiện ích
├── images/                # Thư mục chứa ảnh build
├── .env                   # File chứa token (không commit)
├── .env.example           # Mẫu file .env
├── .gitignore
├── requirements.txt
├── Procfile              # Deploy Railway
├── runtime.txt           # Python version
└── README.md
```

## Cài đặt

1. Clone repo này
2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

3. Tạo file `.env` và thêm token Discord:
```
DISCORD_TOKEN=your_bot_token_here
```

4. Chạy bot:
```bash
python bot.py
```

## Lệnh sử dụng

### Xem hướng dẫn
- `@meta-champion help` hoặc `@meta-champion h`

### Xem tướng meta theo role
- `@meta-champion role ad` hoặc `@meta-champion rad`
- `@meta-champion role mid` hoặc `@meta-champion rmid`
- `@meta-champion role jg` hoặc `@meta-champion rjg`
- `@meta-champion role top` hoặc `@meta-champion rtop`
- `@meta-champion role sp` hoặc `@meta-champion rsp`

### Random tướng theo role
- `@meta-champion random ad` hoặc `@meta-champion rdad`
- `@meta-champion random mid` hoặc `@meta-champion rdmid`
- Tương tự cho các role khác...

### Random tướng bất kỳ
- `@meta-champion random all` hoặc `@meta-champion rdall`

### Random đội hình 5 tướng
- `@meta-champion random team` hoặc `@meta-champion rdteam`
- `@meta-champion rd5`

### Xem build tướng cụ thể
- `@meta-champion anivia`
- `@meta-champion jinx`
- Tên tướng viết thường, không dấu

### Test bot
- `!ping`

## Deploy lên Railway

1. Tạo tài khoản tại [Railway.app](https://railway.app)
2. Kết nối với GitHub
3. Deploy project này
4. Thêm biến môi trường `DISCORD_TOKEN` trong Railway dashboard
5. Bot sẽ tự động chạy 24/7

## License
MIT
