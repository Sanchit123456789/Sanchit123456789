import pandas as pd
from scipy.stats import zscore

# Load the dataset
df = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/Toyota.csv")
df.head()
print(df.columns)

# a. Remove all missing values
# Drops any row with missing values across any column in the dataset
df_cleaned = df.dropna()

# b. Display datatypes and concise summary of all numeric variables
# Displays the data types of all columns and a statistical summary of numeric columns
print("\nData Types:\n", df_cleaned.dtypes)
print("\nSummary of Numeric Variables:\n", df_cleaned.describe())

# c. Remove all duplicate records
# Removes any duplicate rows based on all columns
df_no_duplicates = df_cleaned.drop_duplicates()

# d. Apply Z-score Normalization on Price column
# Z-score normalizes the 'Price' column, which standardizes it to have a mean of 0 and a standard deviation of 1
df_no_duplicates['Price_Zscore'] = zscore(df_no_duplicates['Price'])

print("\nZ-score Normalized Price:\n", df_no_duplicates[['Price', 'Price_Zscore']].head())

# e. Shape and reshape using pivot_table
# Reshaping the data using pivot_table to calculate the average 'Price' based on 'FuelType' and 'Doors' categories
pivot_table = df_no_duplicates.pivot_table(values='Price', index='FuelType', columns='Doors', aggfunc='mean')

print("\nPivot Table (Avg Price by FuelType and Doors):\n", pivot_table)

