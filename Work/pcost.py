import csv

def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f).split(',')
    row = csv.reader(f)
    price = []
    for i in row:
        price.append(float(i[2]))
    return sum(price)

print(portfolio_cost('Data/portfolio.csv'))