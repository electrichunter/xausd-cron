import os
import requests
import time
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv

from pathlib import Path
load_dotenv(dotenv_path=Path('.env'))


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_API_KEY")  # <-- burası

API_KEY = os.getenv("TWELVEDATA_API_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_price():
    url = f"https://api.twelvedata.com/price?symbol=XAU/USD&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "price" in data:
        now = datetime.utcnow().isoformat()
        value = float(data["price"])

        # Supabase'e kaydet
        supabase.table("altin_fiyatlari").insert({"time": now, "value": value}).execute()
        print(f"[{now}] Veri kaydedildi: {value}")
    else:
        print("Veri çekme hatası:", data)

if __name__ == "__main__":
    while True:
        fetch_price()
        time.sleep(300)  # 5 dakika
print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY:", SUPABASE_KEY)
print("API_KEY:", API_KEY)
