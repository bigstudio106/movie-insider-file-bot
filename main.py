# main.py

from telegram.ext import Updater
from config import BOT_TOKEN
from handlers.start_handler import start_handler
from handlers.query_handler import query_handler
from handlers.force_join import force_join_handler
from handlers.query_handler import handle_user_query
dp.add_handler(MessageHandler(Filters.text & ~Filters.command("start"), handle_user_query))

def main():
    
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(start_handler)
    dp.add_handler(force_join_handler)
    dp.add_handler(query_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
