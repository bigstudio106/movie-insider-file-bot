# verification.py

import os
import requests
import time
from pymongo import MongoClient

# Load env variables
MONGO_URI = os.getenv("MONGO_URI")
SHORTYFI_API = os.getenv("SHORTYFI_API")
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")

# MongoDB setup
client = MongoClient(MONGO_URI)
db = client['movie_insider']
collection = db['tokens']

def generate_shortyfi_token():
    try:
        response = requests.post(
            "https://shortyfi.com/api/v1/auth/token",
            json={"api_key": SHORTYFI_API}
        )
        data = response.json()
        return data.get("data", {}).get("access_token")
    except Exception as e:
        print("Error generating shortyfi token:", e)
        return None

def store_token(token):
    timestamp = int(time.time())
    collection.insert_one({
        "access_token": token,
        "timestamp": timestamp
    })

def main():
    new_token = generate_shortyfi_token()
    if new_token:
        store_token(new_token)
        print("New Shortyfi token generated and stored in MongoDB.")
    else:
        print("Failed to generate Shortyfi token.")

if __name__ == "__main__":
    main()
