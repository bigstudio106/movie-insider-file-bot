import logging
import os
from telegram import Bot
from telegram.ext import Updater, Dispatcher
from config import BOT_TOKEN

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize bot and updater
bot = Bot(token=BOT_TOKEN)
updater = Updater(bot=bot, use_context=True)
dispatcher: Dispatcher = updater.dispatcher
