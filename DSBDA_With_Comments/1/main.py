import pandas as pd  # Importing pandas library for data manipulation

# Load the dataset
df = pd.read_csv('iris.csv')  # Reading the Iris dataset from a CSV file into a DataFrame
#print(df)

# Filtering: selecting rows where petal length > 1.5 and variety is 'Setosa'
subset_a = df[(df['petal.length'] > 1.5) & (df['variety'] == 'Setosa')]
print(subset_a)  # Displaying the filtered subset

# Creating another DataFrame manually with additional details about each variety
df2 = pd.DataFrame({
    'variety': ['Setosa', 'Versicolor', 'Virginica'],  # Species names
    'Color': ['Blue', 'Pink', 'Purple'],               # Example colors
    'Habitat': ['Garden', 'Field', 'Swamp']            # Example habitats
})

# Merging the original iris dataset with df2 based on the 'variety' column
merged_b = pd.merge(df, df2, on='variety')  # Performs an inner join by default
print(merged_b)  # Displaying the merged DataFrame

# Sorting the dataset by sepal width and then by sepal length
sorted_c = df.sort_values(by=['sepal.width', 'sepal.length'])
print(sorted_c)  # Displaying the sorted DataFrame

# Transposing the DataFrame: rows become columns and columns become rows
transposed_d = df.transpose()
print(transposed_d)  # Displaying the transposed DataFrame

# Add an 'Id' column if it's not already present in the dataset
if 'Id' not in df.columns:
    df['Id'] = range(1, len(df) + 1)  # Assigning a unique ID starting from 1

# Melting the DataFrame: converting wide format to long format
# Keeping 'Id' and 'variety' fixed, unpivoting measurement columns into two columns: variable and value
melted_e = pd.melt(df, id_vars=['Id', 'variety'], value_vars=['sepal.length', 'sepal.width', 'petal.length', 'petal.width'])
print("\nMelted DataFrame:\n", melted_e.head())  # Displaying first few rows of melted DataFrame

# Pivoting the melted data: converting long format back to wide format
# Creating a table with 'Id' and 'variety' as rows, variable names as columns, and values filled in
pivoted_e = melted_e.pivot_table(index=['Id', 'variety'], columns='variable', values='value')
print("\nPivoted DataFrame:\n", pivoted_e.head())  # Displaying first few rows of pivoted DataFrame

