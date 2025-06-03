import pandas as pd

df = {
    "Array_1": [30, 70, 100],
    "Array_2": [65.1, 49.50, 30.7]
}

data = pd.DataFrame(df)

print(data.corr())