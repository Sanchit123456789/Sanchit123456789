import pandas as pd

# Load the Iris dataset
df = pd.read_csv('Iris.csv')

# ----- a. Check for and handle duplicated rows or missing values -----
# Checking for duplicates before removing them
print("Duplicates before:", df.duplicated().sum())
# Dropping duplicated rows
df = df.drop_duplicates()
# Checking the number of duplicates after removing
print("Duplicates after:", df.duplicated().sum())

# Checking for missing values in each column
print("\nMissing values before:\n", df.isnull().sum())
# Filling missing values (NaN) with the median of the numeric columns
df = df.fillna(df.median(numeric_only=True))
# Checking if missing values are handled
print("Missing values after:\n", df.isnull().sum())

# ----- b. Combine with an external species characteristics table -----
# Create a DataFrame with species characteristics (Color and BloomingTime)
species_info = pd.DataFrame({
    'Species': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
    'Color': ['Blue', 'Pink', 'Purple'],
    'BloomingTime': ['Spring', 'Summer', 'Fall']
})

# Merge the original dataframe with the species_info DataFrame based on the 'Species' column
df = pd.merge(df, species_info, on='Species')
print("\nAfter merge:\n", df.head())

# ----- c. Normalize petal/sepal measurements manually -----
# Normalizing columns to a range of 0 to 1 for 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'
# This brings the values to a common scale for better comparison
for col in ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']:
    min_val = df[col].min()  # Find the minimum value in the column
    max_val = df[col].max()  # Find the maximum value in the column
    df[col] = (df[col] - min_val) / (max_val - min_val)  # Normalize the values to the range [0, 1]
print("\nAfter normalization:\n", df.head())

# ----- d. Add size_ratio column -----
# Create a new column 'size_ratio' that is the ratio of PetalLengthCm to SepalLengthCm
df['size_ratio'] = df['PetalLengthCm'] / df['SepalLengthCm']
print("\nWith size_ratio column:\n", df[['Id', 'PetalLengthCm', 'SepalLengthCm', 'size_ratio']].head())

