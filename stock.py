# libraries
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import requests
from matplotlib.dates import DateFormatter

from HistoricalQuote import HistoricalQuotesParser

if __name__ == '__main__':

    url = "https://restv2.fireant.vn/symbols/MSN/historical-quotes"
    params = {
        "startDate": "2021-02-02",
        "endDate": "2024-02-02",
        "offset": "0",
        "limit": "30",
    }

    headers = {
        "authority": "restv2.fireant.vn",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,es;q=0.6",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSIsImtpZCI6IkdYdExONzViZlZQakdvNERWdjV4QkRITHpnSSJ9.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4iLCJhdWQiOiJodHRwczovL2FjY291bnRzLmZpcmVhbnQudm4vcmVzb3VyY2VzIiwiZXhwIjoxODg5NjIyNTMwLCJuYmYiOjE1ODk2MjI1MzAsImNsaWVudF9pZCI6ImZpcmVhbnQudHJhZGVzdGF0aW9uIiwic2NvcGUiOlsiYWNhZGVteS1yZWFkIiwiYWNhZGVteS13cml0ZSIsImFjY291bnRzLXJlYWQiLCJhY2NvdW50cy13cml0ZSIsImJsb2ctcmVhZCIsImNvbXBhbmllcy1yZWFkIiwiZmluYW5jZS1yZWFkIiwiaW5kaXZpZHVhbHMtcmVhZCIsImludmVzdG9wZWRpYS1yZWFkIiwib3JkZXJzLXJlYWQiLCJvcmRlcnMtd3JpdGUiLCJwb3N0cy1yZWFkIiwicG9zdHMtd3JpdGUiLCJzZWFyY2giLCJzeW1ib2xzLXJlYWQiLCJ1c2VyLWRhdGEtcmVhZCIsInVzZXItZGF0YS13cml0ZSIsInVzZXJzLXJlYWQiXSwianRpIjoiMjYxYTZhYWQ2MTQ5Njk1ZmJiYzcwODM5MjM0Njc1NWQifQ.dA5-HVzWv-BRfEiAd24uNBiBxASO-PAyWeWESovZm_hj4aXMAZA1-bWNZeXt88dqogo18AwpDQ-h6gefLPdZSFrG5umC1dVWaeYvUnGm62g4XS29fj6p01dhKNNqrsu5KrhnhdnKYVv9VdmbmqDfWR8wDgglk5cJFqalzq6dJWJInFQEPmUs9BW_Zs8tQDn-i5r4tYq2U8vCdqptXoM7YgPllXaPVDeccC9QNu2Xlp9WUvoROzoQXg25lFub1IYkTrM66gJ6t9fJRZToewCt495WNEOQFa_rwLCZ1QwzvL0iYkONHS_jZ0BOhBCdW9dWSawD6iF1SIQaFROvMDH1rg",
        "origin": "https://fireant.vn",
        "referer": "https://fireant.vn",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }

    response = requests.get(url, params=params, headers=headers)
    # Assuming 'data' is the key containing the historical quotes in the response JSON
    response_data = response.json()
    historical_quotes_parser = HistoricalQuotesParser(response_data)

    for quote in historical_quotes_parser.raw_data:
        print(quote)

    dates = [datetime.strptime(quote.date, "%Y-%m-%dT%H:%M:%S") for quote in historical_quotes_parser.parse()]
    closing_prices = [quote.close for quote in historical_quotes_parser.parse()]
    sellForeignValue = [quote.sellForeignValue for quote in historical_quotes_parser.parse()]
    buyForeignValue = [quote.buyForeignValue for quote in historical_quotes_parser.parse()]

    # Creating the line plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, sellForeignValue, label='sellForeignValue', marker='o')
    plt.plot(dates, buyForeignValue, label='buyForeignValue', marker='o')

    # Adding labels and title
    plt.xlabel('Date')
    plt.ylabel('sellForeignValue')
    plt.title('Historical Closing Prices')
    plt.legend()
    plt.grid(True)

    # Formatting date on x-axis
    date_format = DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.gcf().autofmt_xdate()

    # Show the plot
    plt.show()
