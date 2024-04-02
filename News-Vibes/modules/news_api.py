import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils.constants import NEWS_API_KEY

def fetch_news(stock_name):
    time_period = (datetime.now() - relativedelta(months=1)).strftime("%Y-%m-%d")
    base_url = "https://newsapi.org/v2/everything?"
    query = f"q={stock_name}&from={time_period}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(base_url + query)
    articles = response.json().get('articles', [])
    return [(article['title'], article['publishedAt']) for article in articles]
