import os
import requests
import time
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")
SHORTYFI_API = os.getenv("SHORTYFI_API")

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
        print("Error generating token:", e)
        return None

def store_token(token):
    timestamp = int(time.time())
    collection.insert_one({
        "access_token": token,
        "timestamp": timestamp
    })
    print(f"[✓] Token stored: {token[:10]}... at {timestamp}")

if __name__ == "__main__":
    while True:
        token = generate_shortyfi_token()
        if token:
            store_token(token)
        else:
            print("[!] Failed to generate token")
        
        # Wait for 1 hour (3600 seconds)
        time.sleep(3600)
