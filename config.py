# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Basic Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
FORCE_JOIN = os.getenv("FORCE_JOIN")
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")
SHORTYFI_API = os.getenv("SHORTYFI_API")

# Optional Defaults
LOG_GROUP = os.getenv("LOG_GROUP", None)
