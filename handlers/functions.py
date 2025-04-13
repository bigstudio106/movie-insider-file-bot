import os
import requests
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")
SHORTYFI_API = os.getenv("SHORTYFI_API")
client = MongoClient(MONGO_URI)
db = client['movie_insider']
collection = db['users']

def generate_verification_link(user_id):
    token = generate_shortyfi_token()
    verification_link = f"https://shortyfi.com/{token}"  # Modify as per API
    store_user_verification_status(user_id, "pending")
    return verification_link

def generate_shortyfi_token():
    response = requests.post(
        "https://shortyfi.com/api/v1/auth/token",
        json={"api_key": SHORTYFI_API}
    )
    data = response.json()
    return data.get("data", {}).get("access_token")

def store_user_verification_status(user_id, status):
    collection.update_one({"user_id": user_id}, {"$set": {"verification_status": status}}, upsert=True)

def is_user_verified(user_id):
    user = collection.find_one({"user_id": user_id})
    if user and user.get("verification_status") == "verified":
        return True
    return False
