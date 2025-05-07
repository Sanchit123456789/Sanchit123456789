import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Load the dataset
df = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/airquality.csv")
df.head()  # Display the first few rows of the dataset
print(df.columns)  # Print column names to check the structure of the dataset

# a. Create data subset with specific columns and index range
# Select columns 'Ozone', 'Solar.R', 'Wind', and 'Temp' for the first 100 rows (index 0 to 99)
subset_df = df.loc[0:99, ['Ozone', 'Solar.R', 'Wind', 'Temp']]  

# b. Replace NaN values rationally
# For each column, replace NaN values with the median of the respective column (common strategy for numerical data)
df['Ozone'] = df['Ozone'].fillna(df['Ozone'].median())
df['Solar.R'] = df['Solar.R'].fillna(df['Solar.R'].median())
df['Wind'] = df['Wind'].fillna(df['Wind'].median())
df['Temp'] = df['Temp'].fillna(df['Temp'].median())

# c. Apply Min-Max Normalization on Solar.R
# The MinMaxScaler scales data to the range [0, 1]
scaler = MinMaxScaler()
df['Solar.R_normalized'] = scaler.fit_transform(df[['Solar.R']])

# d. Plot Month-wise Temperature
# Create a boxplot to show the distribution of temperature for each month
plt.figure(figsize=(8, 5))  # Set the figure size
sns.boxplot(x='Month', y='Temp', data=df)  # Create the boxplot with 'Month' on x-axis and 'Temp' on y-axis
plt.title("Month-wise Temperature")  # Add title to the plot
plt.xlabel("Month")  # Label x-axis
plt.ylabel("Temperature (F)")  # Label y-axis
plt.grid(True)  # Add grid for better readability
plt.show()  # Display the plot

