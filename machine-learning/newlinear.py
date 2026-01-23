# Simple Linear Regression with User Input

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
dataset = pd.read_csv('../data/studentstudyhours.csv')

X = dataset.iloc[:, :-1].values   # Study Hours
y = dataset.iloc[:, -1].values    # Exam Score

# Split dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

# Train model
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Visualization (optional)
plt.scatter(X_train, y_train, color='green')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Study Hours vs Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.show()


# 7) Visualising the Test set results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('study hours vs scored test')
plt.xlabel('study hours')
plt.ylabel('exam scores')
plt.show()

#  User input for prediction
hours = float(input("Enter number of study hours: "))

predicted_score = regressor.predict([[hours]])[0]

# Cap the marks at 100
if predicted_score > 100:
    predicted_score = 100
elif predicted_score < 0:
    predicted_score = 0

print(f"Predicted exam score: {predicted_score:.2f}")