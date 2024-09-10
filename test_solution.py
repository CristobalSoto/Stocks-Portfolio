from datetime import date
from Portfolio import Portfolio
from Stock import Stock

apple = Stock('AAPL')
apple.add_price(date(2022, 1, 1), 150)
apple.add_price(date(2023, 1, 1), 180)

microsoft = Stock('MSFT')
microsoft.add_price(date(2022, 1, 1), 300)
microsoft.add_price(date(2023, 1, 1), 350)


portfolio = Portfolio()
portfolio.add_stock(apple)
portfolio.add_stock(microsoft)
portfolio.add_inflation(date(2022, 1, 1), 0.03)  
portfolio.add_inflation(date(2023, 1, 1), 0.025) 

start_date = date(2022, 1, 1)
end_date = date(2023, 1, 1)

total_profit, nominal_annualized_return, real_annualized_return = portfolio.profit(start_date, end_date)

print(f"Total Profit: ${total_profit}")
print(f"Annualized Nominal Return: {nominal_annualized_return * 100:.2f}%")
print(f"Annualized Real Return: {real_annualized_return * 100:.2f}%")