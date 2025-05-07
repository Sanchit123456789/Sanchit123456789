import pandas as pd

# Load the dataset
df = pd.read_csv("Toyota.csv")
print("Initial Data:\n", df.head())
print("\nColumns:", df.columns)

# Subset: Cars priced above 10,000 and FuelType is Petrol
subset = df[(df['Price'] > 10000) & (df['FuelType'] == 'Petrol')]
print("\nSubset Data:\n", subset.head())

# Create a DataFrame to map FuelType to Region
region_df = pd.DataFrame({
    'FuelType': ['Petrol', 'Diesel', 'CNG'],
    'Region': ['Urban', 'Rural', 'Metro']
})

# Merge the region information into the main dataset
merged = pd.merge(df, region_df, on='FuelType', how='left')
print("\nMerged Data (with Region based on FuelType):\n", merged[['FuelType', 'Region']].head())

# Sort dataset by Price (descending) and KM (ascending)
sorted_df = df.sort_values(by=['Price', 'KM'], ascending=[False, True])
print("\nSorted Data:\n", sorted_df[['Price', 'KM']].head())

# Generate transposed summary statistics
summary_transposed = df.describe().transpose()
print("\nTransposed Summary:\n", summary_transposed)

# Create a pivot table: Average Price based on FuelType and Doors
pivot = df.pivot_table(values='Price', index='FuelType', columns='Doors', aggfunc='mean')
print("\nPivot Table (Average Price):\n", pivot)

