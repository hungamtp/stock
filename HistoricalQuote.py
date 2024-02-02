class HistoricalQuote:
    def __init__(self, date, open_price, high, low, close, volume, buyForeignValue, sellForeignValue):
        self.date = date
        self.open_price = open_price
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.buyForeignValue = buyForeignValue
        self.sellForeignValue = sellForeignValue


    def __str__(self):
        return f"{self.date}: Open={self.open_price}, High={self.high}, Low={self.low}, Close={self.close}, Volume={self.volume}"


class HistoricalQuotesParser:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def parse(self):
        parsed_quotes = []

        for quote_data in self.raw_data:
            date = quote_data.get("date", "")
            open_price = quote_data.get("open", 0)
            high = quote_data.get("high", 0)
            low = quote_data.get("low", 0)
            close = quote_data.get("close", 0)
            volume = quote_data.get("volume", 0)
            sellForeignValue = quote_data.get("sellForeignValue", 0)
            buyForeignValue = quote_data.get("buyForeignValue", 0)

            historical_quote = HistoricalQuote(date, open_price, high, low, close, volume, buyForeignValue, sellForeignValue)
            parsed_quotes.append(historical_quote)

        return parsed_quotes


