import requests
import yfinance as yf
from utils.constants import ALPHA_VANTAGE_API_KEY

def fetch_ohlc(stock_name):
    ticker = yf.Ticker(stock_name)
    hist = ticker.history(period="1mo")
    return hist[['Open', 'High', 'Low', 'Close']]

def fetch_ticker_symbol(stock_name):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": stock_name,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json().get("bestMatches", [])
    if data:
        return data[0]["1. symbol"]
    return None

def fetch_historical_data(ticker_symbol):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_MONTHLY",
        "symbol": ticker_symbol,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(base_url, params=params)
    data = response.json().get("Monthly Time Series", {})
    return data
