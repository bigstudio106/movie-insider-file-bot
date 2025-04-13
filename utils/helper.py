import os
import time
from .access_token import get_latest_token

BASE_URL = "https://shortyfi.com/api/v1/link/short"

def generate_verification_link(user_id: int) -> str:
    token = get_latest_token()
    if not token:
        return "Verification system error. Try again later."

    # Shorten a dummy verification link using shortyfi
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "title": f"Verify User {user_id}",
        "original_url": f"https://t.me/{os.getenv('BOT_USERNAME')}?start=verify_{user_id}"
    }

    import requests
    try:
        response = requests.post(BASE_URL, json=payload, headers=headers)
        data = response.json()
        return data.get("data", {}).get("short_url", "Error generating link")
    except Exception as e:
        print("Shortyfi error:", e)
        return "Error generating verification link"
