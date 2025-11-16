# Discord Bot - League of Legends Meta Champion

Bot Discord để xem tướng meta và build cho League of Legends.

## Tính năng
- Xem danh sách tướng meta theo role
- Random tướng theo role
- Xem build chi tiết của tướng
- Hỗ trợ lệnh viết tắt

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
