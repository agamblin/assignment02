import csv
import matplotlib.pyplot as plt
import sys

filename = "data.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

# printing the field names

prices = []
qty_demanded = []
qty_supplied = []


#  printing first 5 rows
for row in rows:
    # parsing each column of a row
    prices.append(int(row[0]))
    qty_demanded.append(int(row[1]))
    qty_supplied.append(int(row[2]))


plt.plot(qty_demanded, prices, label='Quantity demanded')
plt.plot(qty_supplied, prices, label='Quantity supplied')

plt.xlabel('Quantity')
plt.ylabel('Prices')
plt.title('Equilibrium graph')
plt.legend()
plt.show()
