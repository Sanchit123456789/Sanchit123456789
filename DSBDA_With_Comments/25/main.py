import pandas as pd

# Load the dataset
df = pd.read_csv("Toyota.csv")

# a. Create a subset selecting 'Price', 'Age', 'FuelType', 'Automatic' columns
# We select specific columns from the dataframe to focus on relevant data
subset_a = df[['Price', 'Age', 'FuelType', 'Automatic']]

# Display the first few records of subset_a
print("Subset with columns 'Price', 'Age', 'FuelType', 'Automatic':")
print(subset_a.head())

# b. Create a subset for all Petrol vehicles (assuming 'FuelType' column contains values like 'Petrol')
# Filter the dataframe where the 'FuelType' is 'Petrol'
subset_b = df[df['FuelType'] == 'Petrol']

# Display the first few records of subset_b (all Petrol vehicles)
print("\nSubset with all Petrol vehicles:")
print(subset_b.head())

# c. Create a subset for cars with Price > 15000 and Age < 8
# Filter the dataframe where 'Price' is greater than 15000 and 'Age' is less than 8 years
subset_c = df[(df['Price'] > 15000) & (df['Age'] < 8)]

# Display the first few records of subset_c (Price > 15000 and Age < 8)
print("\nSubset of cars with Price > 15000 and Age < 8 years:")
print(subset_c.head())

# d. Merge the two subsets: Petrol vehicles and cars with Price > 15000 and Age < 8
# Combine the two subsets (subset_b and subset_c) using pd.concat
# This will stack the rows of both dataframes
merged_subset = pd.concat([subset_b, subset_c])

# Display the merged records
print("\nMerged records from subset_b and subset_c:")
print(merged_subset.head())

