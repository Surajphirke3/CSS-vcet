import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hours = np.array([1, 2, 3, 4, 5])
marks = np.array([35, 45, 55, 65, 75])

df = pd.DataFrame({
    "Hours": hours,
    "Marks": marks
})

print(df)

plt.scatter(df["Hours"], df["Marks"] , color='red')
plt.plot(df["Hours"], df["Marks"] , color='red')
plt.title("Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()
