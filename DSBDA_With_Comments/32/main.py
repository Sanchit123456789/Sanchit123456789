import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Toyota.csv")

# Set a consistent visual style
sns.set(style="whitegrid")

# a. Scatter Plot: Age vs Price
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Price', data=df, color='blue')
plt.title('Scatter Plot: Age vs Price')
plt.xlabel('Age (Years)')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# ✅ Use-case: Helps visualize how the price of a car changes with age.

# b. Histogram: Distribution of KM (Kilometers Driven)
plt.figure(figsize=(8, 5))
sns.histplot(df['KM'], bins=30, kde=True, color='green')
plt.title('Histogram: Distribution of KM')
plt.xlabel('Kilometers Driven')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# ✅ Use-case: Shows how frequently different ranges of kilometers appear in the dataset.

# c. Bar Plot: Count of Cars by Fuel Type
plt.figure(figsize=(6, 4))
sns.countplot(x='FuelType', data=df, palette='Set2')
plt.title('Bar Plot: Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# ✅ Use-case: Displays how many cars belong to each fuel type (e.g., Petrol, Diesel, CNG).

