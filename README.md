# Movie Insider File Bot

**Movie Insider File Bot** ek powerful Telegram bot hai jo users ko files/documents ko search aur retrieve karne ki suvidha deta hai. Yeh bot specific Telegram channels se files fetch karta hai aur MongoDB database me store karke users ko search ke basis par results provide karta hai.

---

## Features

- Telegram file/document search via caption or filename
- Force join system for channel subscription
- MongoDB-based auto-save & query
- Admin log system
- Auto-verification with expiring tokens
- Shortyfi API integration for token link shortening

---

## Tech Stack

- Python 3.10+
- python-telegram-bot
- MongoDB
- Koyeb (for deployment)
- Shortyfi API

---

## Environment Variables

`.env` file me following variables define karna zaroori hai:

```env
BOT_TOKEN=your_bot_token
MONGO_URI=your_mongo_uri
ADMIN_ID=your_admin_telegram_id
FORCE_JOIN=https://t.me/your_channel
SOURCE_CHANNEL=-100xxxxxxxxxx
SHORTYFI_API=your_shortyfi_api_key
