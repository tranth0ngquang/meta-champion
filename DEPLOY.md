# 🚀 HƯỚNG DẪN DEPLOY BOT LÊN RAILWAY

## Bước 1: Chuẩn bị trước khi deploy

### 1.1. Tạo token Discord mới (QUAN TRỌNG!)
⚠️ Token cũ đã bị lộ công khai, BẮT BUỘC phải tạo mới!

1. Vào [Discord Developer Portal](https://discord.developer.com/applications)
2. Chọn bot của bạn
3. Vào tab "Bot"
4. Click "Reset Token" để tạo token mới
5. Copy token mới (chỉ hiện 1 lần!)

### 1.2. Bật Privileged Gateway Intents
1. Trong Discord Developer Portal > Bot
2. Bật "MESSAGE CONTENT INTENT"
3. Bật "SERVER MEMBERS INTENT" (optional)
4. Save Changes

## Bước 2: Chuẩn bị Git Repository

### 2.1. Khởi tạo Git (nếu chưa có)
```bash
cd E:\lol-discord-bot
git init
git add .
git commit -m "Initial commit"
```

### 2.2. Tạo GitHub Repository
1. Vào [GitHub](https://github.com) và tạo repository mới
2. Đặt tên: `lol-discord-bot`
3. Để private hoặc public (tùy bạn)
4. Không tạo README (đã có sẵn)

### 2.3. Push code lên GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/lol-discord-bot.git
git branch -M main
git push -u origin main
```

## Bước 3: Deploy lên Railway

### 3.1. Tạo tài khoản Railway
1. Vào [Railway.app](https://railway.app)
2. Click "Login" và đăng nhập bằng GitHub
3. Cấp quyền cho Railway truy cập GitHub

### 3.2. Tạo Project mới
1. Click "New Project"
2. Chọn "Deploy from GitHub repo"
3. Chọn repository `lol-discord-bot`
4. Railway sẽ tự động phát hiện và deploy

### 3.3. Thêm biến môi trường
1. Trong Railway Dashboard, click vào project
2. Vào tab "Variables"
3. Click "New Variable"
4. Thêm:
   - **Key**: `DISCORD_TOKEN`
   - **Value**: Token mới bạn vừa tạo ở bước 1.1
5. Click "Add"

### 3.4. Deploy
1. Railway sẽ tự động deploy sau khi thêm biến môi trường
2. Xem logs để kiểm tra bot có chạy không
3. Tìm dòng: `Bot đã đăng nhập: meta-champion#...`

## Bước 4: Kiểm tra bot

### 4.1. Kiểm tra trên Discord
Thử các lệnh:
- `@meta-champion help`
- `@meta-champion rad`
- `!ping`

### 4.2. Xem logs trên Railway
1. Vào Railway Dashboard > Project
2. Click tab "Deployments"
3. Click vào deployment mới nhất
4. Xem logs để debug nếu có lỗi

## Bước 5: Cập nhật code sau này

Mỗi khi bạn muốn cập nhật bot:

```bash
# Sửa code
git add .
git commit -m "Mô tả thay đổi"
git push
```

Railway sẽ tự động deploy lại!

## ⚠️ LƯU Ý QUAN TRỌNG

1. **KHÔNG bao giờ commit file `.env`** - File này đã được thêm vào `.gitignore`
2. **Token phải được set trên Railway Dashboard**, không hardcode trong code
3. **Folder `images/`** cần được push lên GitHub để bot có ảnh hiển thị
4. Railway miễn phí có giới hạn 500 giờ/tháng (đủ cho bot chạy 24/7 cả tháng)

## Troubleshooting

### Bot không online?
- Kiểm tra biến môi trường `DISCORD_TOKEN` trên Railway
- Xem logs trên Railway để tìm lỗi
- Kiểm tra Message Content Intent đã bật chưa

### Bot không trả lời?
- Kiểm tra bot có quyền "Read Messages" và "Send Messages" trong server
- Kiểm tra logs xem có nhận tin nhắn không

### Lỗi ảnh không hiển thị?
- Kiểm tra folder `images/` đã push lên GitHub chưa
- Kiểm tra đường dẫn file trong code

## Liên hệ & Hỗ trợ

Nếu gặp vấn đề, check logs trên Railway và Discord Developer Portal!
