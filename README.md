# Crypto-Market-Analysis

Creating a data pipeline from a CoinGecko API

## Installation

Create a virtual environment if you don't have one created:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the data pipeline, execute the following command:

```bash
python main.py
```

This will start the application and execute the scheduled job to fetch and analyze cryptocurrency market data from the CoinGecko API.

It is scheduled to run everyday at London market session opening. You can adjust it to your preferences.

## For Streamlit Dashboards

Run:

```bash
streamlit run dashboards/app.py
```

The dashboard will be on Local URL:

```bash
 http://localhost:8501
```
