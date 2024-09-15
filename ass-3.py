
# 1. Asks the user for their name, age, and favorite number

name=input("What's your name?")
age=input("What's your age?")
fav_number=input("What's your favorite number?")

# 2. Uses NumPy to generate a random array of 10 numbers and calculates the mean, median, and standard deviation
import numpy as np
rand_num=np.random.rand(10)
mean=np.mean(rand_num)
median=np.median(rand_num)
st_dev=np.std(rand_num)
print("Random 10 numbers are: ",rand_num)
print("Mean is: ",mean)
print("Median is: ",median)
print("Standard deviation is: ",st_dev)

# 3. Use scikit-learn to create a simple linear regression model based on the user's age and favorite number

import pandas as pd
# from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = np.array([[age]]).reshape(-1, 1)  # User's age as the feature
y = np.array([fav_number])  # User's favorite number as the target
reg_model = LinearRegression().fit(X, y)
predicted_value = reg_model.predict([[age]])

print(f"\nLinear Regression: For age {age}, predicted favorite number is {predicted_value[0]}")

# 4.Calculate the correlation coefficient between the user's age and favorite number
import statistics
correlation_coefficient = statistics.correlation([age, fav_number], [age, fav_number])
print(f"Correlation Coefficient: {correlation_coefficient:.2f}")

# 5.Check the user's age using conditional statements
if age < 18:
 print("You're a Child!")
elif age == 21:
 print("You're 21")
else:
 print("You're an Adult!!!")

 # 6. Use a loop to generate a list of prime numbers up to 100 using 'sympy' library
 import sympy
prime_numbers = []
for i in range(2, 101):
 if sympy.isprime(i):
    prime_numbers.append(i)
print("Prime numbers up to 100:", prime_numbers)

# 7. Create a simple plot of the user's age vs. favorite number using matplotlib
import matplotlib.pyplot as plt
plt.scatter([age], [fav_number])
plt.xlabel("Age")
plt.ylabel("Favorite Number")
plt.title("Age vs Favorite Number")
plt.show()