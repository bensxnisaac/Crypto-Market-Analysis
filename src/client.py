import requests
import pandas as pd

BASE_URL = "https://api.coingecko.com/api/v3"

def get_market_data(page=1, per_page=100):
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": page,
        "sparkline": False
    }

    """Fetches market data from CoinGecko API."""
    response = requests.get(f"{BASE_URL}/coins/markets", params=params)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Error fetching market data: {response.status_code}")
