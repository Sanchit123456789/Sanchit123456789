import matplotlib.pyplot as plt
import pandas as pd

# Load the Toyota dataset
df = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/Toyota.csv")
print("Dataset Columns:")
print(df.columns)

# a. Scatter Plot: Age vs Price
plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Price'], alpha=0.6, color='blue')
plt.title('Scatter Plot: Age vs Price')
plt.xlabel('Age (Years)')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# 📌 Explanation:
# Shows how car price drops as the car gets older. It's used to analyze depreciation with age.

# b. Histogram: Distribution of KM
plt.figure(figsize=(8, 5))
plt.hist(df['KM'], bins=30, color='green', edgecolor='black')
plt.title('Histogram: Distribution of Kilometers Driven')
plt.xlabel('KM Driven')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 📌 Explanation:
# Helps understand how many cars have been driven within specific ranges of kilometers.

# c. Bar Plot: Count of Cars by FuelType
fuel_counts = df['FuelType'].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(fuel_counts.index, fuel_counts.values, color='orange', edgecolor='black')
plt.title('Bar Plot: Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Cars')
plt.grid(True)
plt.show()

# 📌 Explanation:
# This shows how many cars belong to each fuel type category (e.g., Petrol, Diesel, etc.)

