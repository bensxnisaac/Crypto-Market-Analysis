
def transform_market_data(df):
    """Transforms the raw market data DataFrame to a more structured format."""

    df = df[[
        "id", 
        "symbol", 
        "name", 
        "current_price", 
        "market_cap", 
        "total_volume", 
        "price_change_percentage_24h"
    ]].copy()

    df.columns = [
        "coin_id", 
        "symbol", 
        "name", 
        "current_price", 
        "market_cap", 
        "volume_24h", 
        "price_change_percentage_24h"
    ]

    df["symbol"] = df["symbol"].str.upper()
    df["market_cap"] = df["market_cap"].astype(float)

    return df
