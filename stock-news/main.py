import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")  # TODO

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")  # TODO

TWILIO_SID = os.environ.get("TWILIO_SID")  # TODO
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")  # TODO

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
stock_response.raise_for_status()
data_values = [value for (key, value) in stock_response.json()["Time Series (Daily)"].items()][:2]
data_keys = [key for (key, value) in stock_response.json()["Time Series (Daily)"].items()][:2]

latest_closing_price = float(data_values[0]['4. close'])
day_before_closing_price = float(data_values[1]['4. close'])

difference = round(latest_closing_price - day_before_closing_price, 2)
diff_percent = round((difference / latest_closing_price) * 100, 2)

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(diff_percent) > 5:
    NEWS_PARAMS = {
        "q": COMPANY_NAME,
        "from": data_keys[1],
        "to": data_keys[0],
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_response.raise_for_status()
    article_list = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}"
                    for article in news_response.json()["articles"][:3]]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in article_list:
        message = client.messages.create(
            body=article,
            from_="___TWILIO_NUMBER___",  # TODO
            to="___YOUR_NUMBER___",  # TODO
        )
        print(message.sid)
