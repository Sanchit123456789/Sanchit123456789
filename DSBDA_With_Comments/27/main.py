import pandas as pd
from scipy.stats import zscore

# Load dataset
df = pd.read_csv("Toyota.csv")
print("\nAvailable columns:")
print(df.columns)

# a. Remove missing values
df_cleaned = df.dropna()

# b. Display datatypes and concise summary of numeric variables
print("\nData Types of Cleaned Dataset:")
print(df_cleaned.dtypes)

print("\nSummary of Numeric Variables:")
print(df_cleaned.describe())

# c. Remove all duplicate records
df_cleaned = df_cleaned.drop_duplicates()

# d. Apply Z-score normalization on 'Price' column
# Ensure 'Price' is numeric
df_cleaned['Price'] = pd.to_numeric(df_cleaned['Price'], errors='coerce')

# Z-score normalization
df_cleaned['Price_Zscore'] = zscore(df_cleaned['Price'])

print("\nZ-score Normalized 'Price' column:")
print(df_cleaned[['Price', 'Price_Zscore']].head())

# e. Pivot table: average Price grouped by FuelType and Doors
pivot_table = df_cleaned.pivot_table(values='Price', index='FuelType', columns='Doors', aggfunc='mean')

print("\nPivot Table (Average Price by FuelType and Doors):")
print(pivot_table)

