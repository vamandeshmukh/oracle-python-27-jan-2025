
import csv
import numpy as np

nifty50_file = r'D:\VamanPro\Codes\oracle-jan-2025\00-training-code\stock-market-app\data\NIFTY-50-30-01-2024-to-30-01-2025.csv'
# nifty_bank_file = r'D:\VamanPro\Codes\oracle-jan-2025\00-training-code\stock-market-app\data\NIFTY-BANK-30-01-2024-to-30-01-2025.csv'

with open(nifty50_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  
    data = [row for row in reader]

header = [column.lstrip('\ufeff').strip() for column in header]
# print(f"Headers: {header}")  

nfd = np.array(data)

close_prices = nfd[:, header.index('Close')].astype(float)
dates = nfd[:, header.index('Date')]

highest_close = round(np.max(close_prices), 2)
highest_close_index = np.argmax(close_prices)
highest_close_date = dates[highest_close_index]

print(f"Highest Closing Price: {highest_close} on {highest_close_date}")

