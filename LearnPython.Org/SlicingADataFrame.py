import pandas as pd

portfolio = pd.DataFrame()

# print(portfolio)

stock_symbols = pd.Series(["IBM" , "ORCL", "MSFT", "AAPL"])
stock_prices = pd.Series([116.86, 56.91, 216.51, 119.26])
number_shares = pd.Series([50, 100, 50, 100])

portfolio["Symbol"] = stock_symbols
portfolio["Price"] = stock_prices
portfolio["Qty"] = number_shares

# print(portfolio["Price"])

# print(dir(portfolio))

# print(portfolio.Price)

#  need to pass column names as a list into square brackets to grab a couple of columns

print(portfolio[["Price", "Symbol"]])

portfolio["Cost"] = " "

print(portfolio)

portfolio["Cost"] = [115.25, 55.00, 210.30, 105.75]

print(portfolio)

portfolio["Amount"] = portfolio["Price"] * portfolio["Qty"]