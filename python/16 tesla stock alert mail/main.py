import requests
# import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_API_key = "NY3C9Z29E2OZ89UY"
news_API_key = "--- that generated key --"

my_email = "mdnurulhasan1111@gmail.com"
password = "--- my password ---"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stocks_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": 5,
    "apikey": stock_API_key,
}

response_stock = requests.get(url="https://www.alphavantage.co/query", params=stocks_parameter)
response_stock.raise_for_status()
stock_data = response_stock.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]
yesterday_closing_price = stock_list[0]["4. close"]
print(yesterday_closing_price)

day_before_yesterday_closing_price = stock_list[1]["4. close"]
print(yesterday_closing_price)

positive_diff = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
actual_diff = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

print(positive_diff)

diff_percent = positive_diff/float(yesterday_closing_price) * 100
print(diff_percent)

if diff_percent > 0.4:
    news_parameter = {
        "apikey": news_API_key,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    article = news_response.json()["articles"]
    # print(article)


    three_article = article[:3]
    # print(three_article)

    formatted_article = [f"Headlines: {article['title']}.\nBrief: {article['description']}." for article in three_article]
    print(formatted_article)

    for articles in formatted_article:
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = "sonufarhan1111@gmail.com"
        if actual_diff > 0:
            msg['Subject'] = f"{STOCK_NAME}: 🔺{round(diff_percent, 1)}%"
        else:
            msg['Subject'] = f"{STOCK_NAME}: 🔻{round(diff_percent, 1)}%"
        # msg['Subject'] = 'Subject with Unicode Characters: ’ and 🔺'
        body = articles
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg=msg)

