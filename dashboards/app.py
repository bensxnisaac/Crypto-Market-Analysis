import streamlit as st
import sqlite3
import pandas as pd


st.set_page_config(page_title="Crypto Market Dashboard", layout="wide")
st.title("Crypto Market Dashboard")


def load_data():
    conn = sqlite3.connect("data/crypto_market_data.db")
    df = pd.read_sql("SELECT * FROM crypto_market_data", conn)
    conn.close()
    return df

st.subheader("Market Data")
df = load_data()
min_market_cap = st.slider("Minimum Market Cap", int(df["market_cap"].min()), int(df["market_cap"].max()), int(df["market_cap"].min()))
filtered_df = df[df["market_cap"] >= min_market_cap]
st.dataframe(filtered_df)

st.metric("Number of Cryptocurrencies", len(df))
st.metric("Total Market Cap", f"{int(df["market_cap"].sum()):,} USD")
st.metric("Average Price", f"{round(df["current_price"].mean(), 2):,} USD")
st.metric("Total 24h Trading Volume", f"{int(df["volume_24h"].sum()):,} USD")



top10 = df.nlargest(10, "market_cap")[["name", "symbol", "market_cap"]]
st.subheader("Top 10 Cryptocurrencies by Market Cap")
st.bar_chart(top10.set_index("name")["market_cap"])

st.subheader("Top 10 Cryptocurrencies by 24h Trading Volume")
top10_volume = df.nlargest(10, "volume_24h")[["name", "symbol", "volume_24h"]]
st.bar_chart(top10_volume.set_index("name")["volume_24h"])

st.subheader("Top 10 Cryptocurrencies by Gains")
top10_gains = df.nlargest(10, "price_change_percentage_24h")[["name", "symbol", "price_change_percentage_24h"]]
st.bar_chart(top10_gains.set_index("name")["price_change_percentage_24h"])

st.subheader("Top 10 Cryptocurrencies by Losses")
top10_losses = df.nsmallest(10, "price_change_percentage_24h")[["name", "symbol", "price_change_percentage_24h"]]
st.bar_chart(top10_losses.set_index("name")["price_change_percentage_24h"])

st.subheader("Top 10 Cryptocurrencies by Current Price")
top10_price = df.nlargest(10, "current_price")[["name", "symbol", "current_price"]]
st.bar_chart(top10_price.set_index("name")["current_price"])

st.subheader("Price vs Volume")
st.line_chart(df[["current_price", "volume_24h"]])