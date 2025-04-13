import os
from pymongo import MongoClient

# Load Mongo URI
MONGO_URI = os.getenv("MONGO_URI")

# MongoDB Setup
client = MongoClient(MONGO_URI)
db = client["movie_insider"]

# Collections
user_collection = db["users"]
token_collection = db["tokens"]

# User Verification Check
def is_user_verified(user_id: int) -> bool:
    user = user_collection.find_one({"user_id": user_id})
    return user and user.get("verified", False)

# Add new user or update verification status
def set_user_verified(user_id: int):
    user_collection.update_one(
        {"user_id": user_id},
        {"$set": {"verified": True}},
        upsert=True
    )

# Save new user as unverified
def save_unverified_user(user_id: int):
    if not user_collection.find_one({"user_id": user_id}):
        user_collection.insert_one({"user_id": user_id, "verified": False})
