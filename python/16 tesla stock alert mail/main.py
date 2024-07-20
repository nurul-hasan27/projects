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
news_API_key = "c3be8fab00464759b225acc0cb83942a"

my_email = "mdnurulhasan1111@gmail.com"
password = "mopn hrme unyk pale"

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
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = stock_list[1]["4. close"]
print(yesterday_closing_price)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_diff = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
actual_diff = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

print(positive_diff)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = positive_diff/float(yesterday_closing_price) * 100
print(diff_percent)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 0.4:
    news_parameter = {
        "apikey": news_API_key,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    article = news_response.json()["articles"]
    # print(article)
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_article = article[:3]
    # print(three_article)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_article = [f"Headlines: {article['title']}.\nBrief: {article['description']}." for article in three_article]
    print(formatted_article)
#TODO 9. - Send each article as a separate message via Twilio.
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

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
