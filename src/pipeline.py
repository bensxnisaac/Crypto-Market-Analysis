from src.client import get_market_data
from src.transform import transform_market_data
from src.db import create_connection
import pandas as pd


def run_pipeline():
    print("Extracting data from CoinGecko API...")
    df = get_market_data()

    print("Transforming data...")
    df = transform_market_data(df)

    df["date"] = pd.Timestamp.today().date()
    df["last_updated"] = pd.Timestamp.now()


    print("Saving data to CSV file...")
    df.to_csv("data/crypto_market_data.csv", index=False)
  
    print("Loading data into SQLite database...")
    conn = create_connection()
    if conn is not None:
        df.to_sql("crypto_market_data", conn, if_exists="replace", index=False)
        conn.close()
        print("Data has been successfully stored in the database.")
    else:
        print("Failed to create database connection.")


