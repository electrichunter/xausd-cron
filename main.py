import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TWELVE_DATA_API_KEY = os.getenv("TWELVE_DATA_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

def get_xauusd():
    url = "https://api.twelvedata.com/price"
    params = {
        "symbol": "XAU/USD",
        "apikey": TWELVE_DATA_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return {
        "price": float(data["price"]),
        "time": datetime.utcnow().isoformat()
    }

def insert_to_supabase(price_data):
    headers = {
        "apikey": SUPABASE_API_KEY,
        "Authorization": f"Bearer {SUPABASE_API_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

    payload = {
        "time": price_data["time"],
        "price": price_data["price"]
    }

    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/xausd_prices",
        headers=headers,
        json=payload
    )

    if response.status_code in [200, 201, 204]:
        print("✅ Veri Supabase'e kaydedildi.")
    else:
        print("❌ Hata:", response.text)

if __name__ == "__main__":
    data = get_xauusd()
    insert_to_supabase(data)
