from os.path import join
import pandas as pd
import json


# -------------------------------------- #
#  Load the addresses from my JSON file  #
# -------------------------------------- #

with open('address_book.json', 'r') as f:
    d = json.load(f)

# create dictionary to hold desired results
d1 = {}

# work through and leave out the lattitudes and longitudes
for k, v in d.items():
    if k == 'lattitudes' or k == 'longitudes':
        print('Skipping longs and latts')
    elif int(k) in range(182):
        addr = [x.strip() for x in v.split(',')][1:]
        nice = ', '.join(addr)
        print(nice)
        d1[int(k)] = nice
    else:
        print('Went through some unexpected condition!')

# put the data into a dataframe
addr = pd.Series(d1, name='address')
addr.index.name = 'id'


# ------------------------------------------------ #
#  Write the data into Excel from pandas directly  #
# ------------------------------------------------ #

FOLDER = '/home/n1k31t4/gdrive/contracts_to_analyze/'
FILE = 'Adressen.xlsx'
TAB = 'Adressen'
TARGET = join(FOLDER, FILE)

writer = pd.ExcelWriter(TARGET)

addr.to_excel(writer, 'addresses')
writer.save()

# I then copied and pasted the output into the tab 'Adressen' in the file 'Lexccelerate' in Google Drive.
