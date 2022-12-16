# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {
                headers[0]: row[0],
                headers[1]: int(row[1]),
                headers[2]: float(row[2])
            }
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('Skipping empty line...')
                pass

    return prices

# TODO: make args optional and read from course' default portfolio/prices files
def compute(name, portfolio_list, price_list):
    portfolio = read_portfolio(portfolio_list)
    prices = read_prices(price_list)

    # select dict in portfolio that contains name as value
    # does not work if name doesn't exist in either file
    for d in portfolio:
        if d.get('name') == name:
            portfolio_lookup = portfolio[portfolio.index(d)]['price']
    price_lookup = prices.get(name, 0.0)

    if portfolio_lookup > price_lookup:
        print(f'Net loss of {portfolio_lookup - price_lookup:0.2f}')
    else:
        print(f'Net gain of {price_lookup - portfolio_lookup:0.2f}')
