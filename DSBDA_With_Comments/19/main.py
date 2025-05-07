import pandas as pd

# Load the dataset
df = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/Toyota.csv")
df.head()
print(df.columns)

# a. Sort observations on Price values (ascending order)
# Sorting the DataFrame by 'Price' in ascending order (from lowest to highest)
df_sorted = df.sort_values(by='Price', ascending=True)
print("Sorted DataFrame by Price:\n", df_sorted[['Price']].head())

# b. Create Subsets
# - Selecting specific columns
# Here, we are selecting only the 'Price', 'Age', and 'FuelType' columns from the DataFrame.
columns_subset = df[['Price', 'Age', 'FuelType']]
print("\nColumn Subset:\n", columns_subset.head())

# - Selecting rows and specific columns (e.g., first 5 rows of 'Price' and 'KM')
# Using .loc to select rows from index 0 to 4 and columns 'Price' and 'KM'
rows_cols_subset = df.loc[0:4, ['Price', 'KM']]
print("\nRow and Column Subset:\n", rows_cols_subset)

# c. Subset of cars with Price > 15000 and Age < 8
# Filtering the dataset to find cars with Price > 15000 and Age < 8
price_age_subset = df[(df['Price'] > 15000) & (df['Age'] < 8)]
print("\nCars with Price > 15000 and Age < 8:\n", price_age_subset[['Price', 'Age']].head())

# d. Subset of cars consuming Petrol
# Filtering the DataFrame to include only rows where 'FuelType' is 'Petrol'
petrol_cars = df[df['FuelType'] == 'Petrol']
print("\nPetrol Cars Subset:\n", petrol_cars[['FuelType']].head())

# e. Apply decimal normalization on Price column
# Decimal normalization of the 'Price' column
# Here, we are normalizing the 'Price' column by dividing each value by 10^n, where n is the number of digits in the maximum 'Price' value.
max_price = df['Price'].abs().max()  # Finding the maximum value in 'Price'
df['Price_DecimalNormalized'] = df['Price'] / (10 ** len(str(int(max_price))))  # Normalizing
print("\nDecimal Normalized Price:\n", df[['Price', 'Price_DecimalNormalized']].head())

