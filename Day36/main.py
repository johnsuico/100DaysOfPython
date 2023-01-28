import requests as req, os
from dotenv import load_dotenv
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv('DAY36_APIKEY_STOCK')
NEWS_API_KEY = os.getenv('DAY36_APIKEY_NEWS')

stock_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

res = req.get(STOCK_ENDPOINT, params=stock_params)
data = res.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = float(data_list[0]['4. close'])
day_before_yesterday_closing_price = float(data_list[1]['4. close'])

difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)

diff_percent = (difference / yesterday_closing_price) * 100

if diff_percent > 5:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qinTitle': COMPANY_NAME
    }

    news_res = req.get(NEWS_ENDPOINT, params=news_params)
    articles = news_res.json()['articles']
    three_articles = articles[:3]

    formatted_articles_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    print(formatted_articles_list)