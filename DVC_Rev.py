import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "Daisy", "Ethan"],
    "age": [14, 15, 13, 14, 15]
}

df = pd.DataFrame(data)

# 1st change
# df.loc[len(df)] = ["Frank", 14]

# 2nd change
# df.loc[len(df)] = ["Thorffin", 17]

df.to_csv("students.csv", index=False)

print("students.csv created!!!")
