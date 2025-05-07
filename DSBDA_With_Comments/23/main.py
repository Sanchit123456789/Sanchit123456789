import pandas as pd

# Load the dataset
df = pd.read_csv('Toyota.csv')

# a. Remove duplicate records and display concise summary
# Removing any duplicate rows in the dataset
df_cleaned = df.drop_duplicates()

# Displaying concise summary (including data types, non-null counts) of the dataset after removing duplicates
print("\nConcise summary of the dataset after removing duplicates:")
print(df_cleaned.info())  # info() provides column names, non-null count, and data types

# b. Create Subset selecting columns 'Price', 'Age', 'FuelType' and initial 10 records
# Creating a subset by selecting only the columns 'Price', 'Age', and 'FuelType' for the first 10 records
subset = df_cleaned[['Price', 'Age', 'FuelType']].head(10)
print("\nSubset of 'Price', 'Age', 'FuelType' for the first 10 records:")
print(subset)  # Displaying the subset of the dataset

# c. Transpose of this subset
# Transposing the subset to swap rows and columns
subset_transposed = subset.T
print("\nTranspose of the subset:")
print(subset_transposed)  # Transposed view of the subset

# d. Apply mean-max normalization on the 'HP' column
# Ensuring that the 'HP' column is numeric, forcing errors (non-numeric values) to NaN
df_cleaned['HP'] = pd.to_numeric(df_cleaned['HP'], errors='coerce')

# Filling NaN values in the 'HP' column with the median of the 'HP' column
df_cleaned['HP'].fillna(df_cleaned['HP'].median(), inplace=True)

# Applying mean-max normalization: (X - min) / (max - min)
df_cleaned['HP_normalized'] = (df_cleaned['HP'] - df_cleaned['HP'].min()) / (df_cleaned['HP'].max() - df_cleaned['HP'].min())

# Displaying the first few rows of the 'HP' and 'HP_normalized' columns to check the result
print("\nDataset after applying mean-max normalization on HP column:")
print(df_cleaned[['HP', 'HP_normalized']].head())  # Checking the result of normalization

