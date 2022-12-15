# pcost.py
#
# Exercise 1.27

totalcost = 0

with open('Data/portfolio.csv', 'rt') as file:
    headers = next(file).split(',')
    for line in file:
        row = line.split(',')   
        shares = int(row[1]) * float(row[2])
        totalcost += shares

print(f'Total cost {totalcost}')
