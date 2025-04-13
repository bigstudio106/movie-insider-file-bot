from config import LOG_GROUP, BOT_TOKEN
from telegram import Bot

bot = Bot(token=BOT_TOKEN)

def send_log(message: str):
    if LOG_GROUP:
        try:
            bot.send_message(chat_id=int(LOG_GROUP), text=message)
        except Exception as e:
            print(f"[LOG ERROR]: {e}")
