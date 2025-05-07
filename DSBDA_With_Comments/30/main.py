import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the Toyota dataset
df = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/Toyota.csv")
print("Dataset Columns:")
print(df.columns)

# a. Scatter Plot: Car Price vs Age
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Age', y='Price')
plt.title('Car Price by Age')
plt.xlabel('Age (Years)')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# Explanation:
# Shows the relationship between car age and price. Generally, price decreases as age increases.

# b. Histogram: Distribution of KM Driven
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='KM', bins=30, kde=True)
plt.title('Distribution of Kilometers Driven (KM)')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Explanation:
# Displays how many cars fall within certain ranges of kilometers driven. The KDE line shows the density.

# c. Bar Plot: Count of Cars by Fuel Type
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='FuelType', order=df['FuelType'].value_counts().index)
plt.title('Count of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# Explanation:
# Shows the number of cars available for each fuel type (like Petrol, Diesel, etc.)

