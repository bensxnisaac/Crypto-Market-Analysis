import sqlite3
from sqlite3 import Error
import os

os.makedirs("data", exist_ok=True)

DATABASE_PATH = "data/crypto_market_data.db"

def create_connection():
    """Create a database connection to the SQLite database specified by DATABASE_PATH."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

