import pandas as pd

# Load the dataset
df = pd.read_csv('Toyota.csv')

# a. Remove missing values
# Dropping rows with any missing values (NaN). This operation removes any row that has at least one NaN.
df_clean = df.dropna()
print("After removing missing values, shape:", df_clean.shape)

# b. Handle missing 'Doors' value (if any, fill with 4 doors or drop rows)
# If there are any NaN values in the 'Doors' column, we fill them with '4' (a default value).
df_clean['Doors'] = df_clean['Doors'].fillna('4')

# Ensure 'Doors' column is in a uniform numeric format
# We extract any digits from the 'Doors' column (which might have non-numeric characters like '4 doors') and convert to integers
df_clean['Doors'] = df_clean['Doors'].astype(str).str.extract('(\d)').fillna('4').astype(int)

# Print unique values in the 'Doors' column to ensure uniformity
print("Unique Doors values after standardization:", df_clean['Doors'].unique())

# c. Provide concise summary of all numeric variables
# This will give us a statistical summary of all numeric columns like mean, standard deviation, min, max, etc.
numeric_summary = df_clean.describe()
print("\nSummary of numeric variables:\n", numeric_summary)

# d. Remove all duplicate records
# Drops any rows that are duplicates, meaning rows with identical values across all columns
df_nodup = df_clean.drop_duplicates()
print("\nAfter removing duplicates, shape:", df_nodup.shape)

# e. Get dummies for categorical data 'FuelType' (One-hot encoding)
# One-hot encoding for 'FuelType' will create a new binary column for each unique category in 'FuelType'.
df_encoded = pd.get_dummies(df_nodup, columns=['FuelType'], prefix='Fuel')
print("\nData after one-hot encoding 'FuelType':\n", df_encoded.head())

# Optional: Save the cleaned and encoded dataset
# If desired, you can save the cleaned and encoded DataFrame to a new CSV file for future use.
# df_encoded.to_csv('Toyota_cleaned.csv', index=False)

