import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [35, 45, 55, 65, 75]

plt.plot(hours, marks, marker='o')
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

