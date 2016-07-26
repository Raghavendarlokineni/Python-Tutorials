"""from urllib import request """

import csv
import sys
from stock_functions import *
from csv_links import *

stock_details = []
search = None
file_path = 'C:/Users/rlokinen/Desktop/python/stock.txt'

index = 1
stock_map = []
dict1 = {}

"""
following code will help in creating the list of dictioanries with all the stocks
and respective csv path. User can add the list in the file csv_links.py
"""
for i in range(len(stocks)):
    dict1['name'] = stocks[i]
    dict1['csv'] = csv_list[i]
    stock_map.append(dict1.copy())    


"""
will search the stock name from the user input in the stock_map list
and calls the function to download the file. If found else exit the program
"""

for stock in range(len(stocks)):
    
    if sys.argv[1].lower() == stock_map[stock]['name']:
        search = stock_map[stock]['csv']
        download_file(search, file_path)
        
if(search == None):
    print("use proper names",stocks)
    exit()

"""
csv module helps in operating the csv files. All data is stored in to the list stock_details
"""

with open(file_path, 'r') as csvfile:
    lines = csv.DictReader(csvfile)

    for line in lines:
      stock_details.append(line)

if sys.argv[2].upper() == 'HIGH':
    High = high_range(stock_details)
    print(stock_details[High])
elif sys.argv[2].upper() == 'LOW':
    Low = low_range(stock_details)
    print(stock_details[Low])
else:
    print("user options are ", options)


