# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    '''
    Computes stock portfolio costs from CSV files
    '''

    totalcost = 0

    with open(filename, 'rt') as file:
        lines = csv.reader(file)
        headers = next(lines)
        for line in lines:
            try:
                shares = int(line[1]) * float(line[2])
            except ValueError:
                print("Skipping empty line")
                pass
            totalcost += shares

    return totalcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
