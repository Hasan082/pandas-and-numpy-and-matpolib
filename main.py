import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)


# Accessing full data Frame
print(df)
print("=============")

# Accessing One Element
print(df["Name"])
print("=============")

# Accessing Rows:
print(df.iloc[1])
print("=============")

# Slicing:
print(df[['Name', 'Age']])
print(df[1:3])
print("=============")

# Finding Unique Elements:
print(df['Age'].unique())
print("=============")

# Conditional Filtering:
high_above_25 = df[df['Age'] > 25 ]
print(high_above_25)
print("=============")


import yfinance as yf

# Fetch AMD stock data with max period
amd_stock = yf.Ticker("AMD")
stock_data = amd_stock.history(period="max")

# Reset index to make 'Date' a column
stock_data.reset_index(inplace=True)

# Get the Volume of AMD traded on the first day (first row)
first_day_volume = stock_data.iloc[0]['Volume']

print(first_day_volume)

