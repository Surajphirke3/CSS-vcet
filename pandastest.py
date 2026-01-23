import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [75, 88, 92]
}

df = pd.DataFrame(data)

print(df)
print("\nAverage Marks:", df["Marks"].mean())
