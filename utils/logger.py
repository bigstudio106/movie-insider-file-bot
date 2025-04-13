from config import LOG_GROUP, API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client

# Pyrogram client for logging
log_client = Client("logger_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def send_log(message: str):
    if LOG_GROUP:
        try:
            await log_client.send_message(chat_id=int(LOG_GROUP), text=message)
        except Exception as e:
            print(f"[LOG ERROR]: {e}")
