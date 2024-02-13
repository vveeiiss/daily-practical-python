import csv

def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f).split(',')
    row = csv.reader(f)
    price = []
    for num, i in enumerate(row, start=1):
        try:
            price.append(float(i[2]))
        except ValueError:
            print(f'Row {num}: Bad row: {i}')
    return sum(price)

print(portfolio_cost('Data/missing.csv'))