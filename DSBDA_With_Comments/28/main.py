import pandas as pd

# Load the Salaries dataset
df = pd.read_csv('Salaries.csv')

# a. Create Data Subsets

# 1. Subset by selecting specific columns ('rank' and 'salary') - first 10 rows
subset_columns = df[['rank', 'salary']].head(10)
print("\nSubset: First 10 rows with 'rank' and 'salary':")
print(subset_columns)

# 2. Subset by applying condition (rank = 'AssocProf')
subset_condition = df[df['rank'] == 'AssocProf']
print("\nSubset: Rows where rank is 'AssocProf':")
print(subset_condition)

# b. Merge Data

# Create a sample additional dataset for merging
df_additional = pd.DataFrame({
    'rank': ['AsstProf', 'AssocProf', 'Prof'],
    'new_column': ['A', 'B', 'C']
})

# Merge datasets on the 'rank' column
merged_data = pd.merge(df, df_additional, on='rank', how='inner')
print("\nMerged Data (on 'rank'):")
print(merged_data.head())

# c. Sort Data

# Sort by salary in descending order
sorted_data = df.sort_values(by='salary', ascending=False)
print("\nTop 5 entries sorted by 'salary' (descending):")
print(sorted_data[['rank', 'salary']].head())

# d. Transpose Data

# Transpose the entire dataframe (rows <-> columns)
transposed_data = df.T
print("\nTransposed DataFrame (first few rows):")
print(transposed_data.head())

# e. Shape and Reshape Data

# Display original shape (rows, columns)
print("\nShape of the dataset:")
print(df.shape)

# Reshape the DataFrame values (e.g., into 2D array with 6 columns)
# Note: Total elements must be divisible by 6 to avoid error
reshaped_data = df.values.reshape(-1, 6)
print("\nReshaped Data (flattened to 2D array with 6 columns):")
print(reshaped_data[:5])  # Show only first 5 rows

