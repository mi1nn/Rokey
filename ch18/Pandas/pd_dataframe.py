# pd_dataframe.py

import pandas as pd

data = [
    [1, "Alice", 30], 
    [2, "Bob", 35],
    [3, "Charlie", 25]
]

df = pd.DataFrame(data, columns = ["ID", "NAME", "AGE"])
print(df)
print(type(df))
print('----------------------')

data = {
    "ID": [1, 2, 3], 
    "NAME": ["Alice", "Bob", "Charlie"],
    "AGE": [30, 25, 35]
}

df = pd.DataFrame(data)
print(df)
