from datetime import date

from Stock import Stock

class Portfolio:
    def __init__(self):
        self.stocks = []
        self.inflation_data = {}

    def add_stock(self, stock: Stock):
        """Adds a stock to the portfolio."""
        self.stocks.append(stock)

    def add_inflation(self, inflation_date: date, inflation_rate: float):
        """Adds inflation data for a specific date."""
        self.inflation_data[inflation_date] = inflation_rate

    def get_inflation(self, query_date: date) -> float:
        """Gets the inflation rate for a specific date, returns 0 if not found."""
        return self.inflation_data.get(query_date, 0)

    def calculate_nominal_profit(self, start_date: date, end_date: date) -> float:
        total_profit = 0.0
        start_value = 0.0
        end_value = 0.0

        for stock in self.stocks:
            start_price = stock.price(start_date)
            end_price = stock.price(end_date)

            if start_price is not None and end_price is not None:
                total_profit += (end_price - start_price)
                start_value += start_price
                end_value += end_price

        if start_value == 0:
            return 0.0, 0.0

        return total_profit, start_value, end_value

    def calculate_nominal_annualized_return(self, start_value: float, end_value: float, start_date: date, end_date: date) -> float:
        days_between = (end_date - start_date).days

        if days_between <= 0:
            return 0.0

        # For short periods, return the simple return instead
        if days_between < 30:
            return (end_value / start_value) - 1

        # Nominal annualized return for longer periods
        years_between = days_between / 365.25
        return (end_value / start_value) ** (1 / years_between) - 1


    def calculate_real_annualized_return(self, nominal_return: float, start_date: date, end_date: date) -> float:
        # Calculate inflation between the two dates
        start_inflation = self.get_inflation(start_date)
        end_inflation = self.get_inflation(end_date)
        average_inflation = (start_inflation + end_inflation) / 2

        # Real return (adjusted for inflation)
        return ((1 + nominal_return) / (1 + average_inflation)) - 1

    def get_inflation(self, query_date: date) -> float:
        """Gets the inflation rate for a specific date, returns 0 if not found."""
        return self.inflation_data.get(query_date, 0)

    def profit(self, start_date: date, end_date: date) -> tuple:
        # Calculate nominal profit
        total_profit, start_value, end_value = self.calculate_nominal_profit(start_date, end_date)

        if start_value == 0:
            return 0.0, 0.0, 0.0

        # Calculate nominal annualized return
        nominal_annualized_return = self.calculate_nominal_annualized_return(start_value, end_value, start_date, end_date)

        # Calculate real annualized return (inflation-adjusted)
        real_annualized_return = self.calculate_real_annualized_return(nominal_annualized_return, start_date, end_date)

        return total_profit, nominal_annualized_return, real_annualized_return



