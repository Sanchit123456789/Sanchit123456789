import pandas as pd

# Load the dataset
df = pd.read_csv('Toyota.csv')

# a. Sort observations on Price values (ascending order)
df_sorted = df.sort_values(by='Price', ascending=True)
print("\nDataset sorted by 'Price' in ascending order:")
print(df_sorted[['Price', 'Age']].head())  # Display top 5 records after sorting

# b. Create subsets by selecting columns and rows
# Selecting specific columns and displaying first 10 rows
subset_columns = df[['Price', 'Age', 'FuelType']].head(10)
print("\nSubset: 'Price', 'Age', 'FuelType' for first 10 rows:")
print(subset_columns)

# Selecting rows 10 to 20 and specific columns using .loc
subset_rows_columns = df.loc[10:20, ['Price', 'Age', 'FuelType']]
print("\nSubset: rows 10 to 20 and columns 'Price', 'Age', 'FuelType':")
print(subset_rows_columns)

# c. Subset of cars having Price > 15000 and Age < 8
subset_price_age = df[(df['Price'] > 15000) & (df['Age'] < 8)]
print("\nSubset of cars with Price > 15000 and Age < 8:")
print(subset_price_age)

# d. Subset of cars that use Petrol as FuelType
subset_petrol = df[df['FuelType'] == 'Petrol']
print("\nSubset of cars consuming Petrol:")
print(subset_petrol)

# e. Apply Decimal Normalization on Price column
# Find the max value in Price column to determine number of digits
max_price = df['Price'].max()
decimal_factor = len(str(int(max_price)))  # e.g., 23950 → 5 digits → divide by 10^5
df['Price_normalized'] = df['Price'] / (10 ** decimal_factor)

# Display result after normalization
print("\nPrice column after decimal normalization:")
print(df[['Price', 'Price_normalized']].head())

