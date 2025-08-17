stock_prices = {"AAPL": 180, "TSLA": 250, "MSFT": 300}
portfolio = {}
total_value = 0
while True:
    stock = input("Enter stock name (or 'done'):").upper()
    if stock == "Done":
        break
    qty = int(input("Enter quantity:"))
    if stock in stock_prices:
        portfolio[stock] = qty
    else:
        print("stock not found in list!")
for stock, qty in portfolio.items():
    total_value += stock_prices[stock] * qty
print("you portfolio:", portfolio)
print("Total value: $", total_value)                