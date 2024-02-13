import csv

def parse_csv(line, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    rows = []
    for l in line:
        rows.append(l)

        # Read the file headers
    headers = rows[0]
    records = []
    if select:
        ind = [headers.index(column) for column in select]
        headers = select
    else:
        ind = []

    for row in rows:
        print(row)
        if not row:    # Skip rows with no data
            continue

        if ind:
            row = [rows[index] for index in ind]
        record = dict(zip(headers, row))
        print(record)
        records.append(record)

    return rows

with open('Data/portfolio.csv') as f:
    d = parse_csv(f, ['name'])
# print(d)