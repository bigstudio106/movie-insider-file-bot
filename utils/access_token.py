import os
import requests
import time
from pymongo import MongoClient

# Load environment variables
MONGO_URI = os.getenv("MONGO_URI")
SHORTYFI_API = os.getenv("SHORTYFI_API")

# MongoDB Setup
client = MongoClient(MONGO_URI)
db = client["movie_insider"]
token_collection = db["tokens"]

def generate_shortyfi_token():
    try:
        response = requests.post(
            "https://shortyfi.com/api/v1/auth/token",
            json={"api_key": SHORTYFI_API}
        )
        data = response.json()
        return data.get("data", {}).get("access_token")
    except Exception as e:
        print("[ERROR] Token Generation Failed:", e)
        return None

def store_token(token):
    token_collection.insert_one({
        "access_token": token,
        "timestamp": int(time.time())
    })

def get_latest_token():
    latest = token_collection.find_one(sort=[("timestamp", -1)])
    return latest.get("access_token") if latest else None

def refresh_and_get_token():
    token = generate_shortyfi_token()
    if token:
        store_token(token)
        return token
    else:
        return get_latest_token()
