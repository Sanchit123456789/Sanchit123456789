import pandas as pd

# a. Read dataset and display summary
df = pd.read_csv('airquality.csv')  # Load the dataset
print("Dataset Summary:\n")
print(df.describe())  # Summary statistics of the dataset (e.g., mean, std, min, max)
print("\nDataset Info:\n")
print(df.info())  # Information about the dataset (e.g., column data types, non-null counts)

# b. Create data subsets
# Subset 1: rows with index 11 to 49 (Python index is zero-based)
subset1 = df.iloc[11:50]

# Subset 2: rows where Temp < 60
subset2 = df[df['Temp'] < 60]

# Print the shape (dimensions) of the subsets
print("\nSubset 1 (index 11 to 49):", subset1.shape)
print("Subset 2 (Temp < 60):", subset2.shape)

# c. Merge observations of any two subsets (union, remove duplicates)
# Merging both subsets, removing any duplicate rows (union)
merged_subset = pd.concat([subset1, subset2]).drop_duplicates()

# Print the shape of the merged dataset
print("\nMerged Subset Shape:", merged_subset.shape)

# d. Apply sort on Temp values
# Sorting the original dataframe by the 'Temp' column in ascending order
sorted_df = df.sort_values(by='Temp')

# Display the top 5 rows of the sorted dataset
print("\nTop 5 after sorting by Temp:\n", sorted_df.head())

# Optional: Save the merged and sorted datasets to new CSV files
# merged_subset.to_csv('merged_subset.csv', index=False)
# sorted_df.to_csv('sorted_airquality.csv', index=False)

