import pandas as pd

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
