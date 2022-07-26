import pandas as pd

portfolio = pd.DataFrame()

# print(portfolio)

stock_symbols = pd.Series(["IBM" , "ORCL", "MSFT", "AAPL"])
stock_prices = pd.Series([116.86, 56.91, 216.51, 119.26])
number_shares = pd.Series([50, 100, 50, 100])

portfolio["Symbol"] = stock_symbols
portfolio["Price"] = stock_prices
portfolio["Qty"] = number_shares

print(portfolio.index)
print(portfolio.columns)
print(portfolio.values)