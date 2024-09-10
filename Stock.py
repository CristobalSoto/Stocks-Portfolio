from datetime import date

class Stock:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.price_history = {}

    def add_price(self, price_date: date, price: float):
        """Adds a price for a specific date to the stock's price history."""
        self.price_history[price_date] = price

    def price(self, query_date: date) -> float:
        """Returns the price of the stock on the given date."""
        return self.price_history.get(query_date, None)
