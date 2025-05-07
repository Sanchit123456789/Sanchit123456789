import pandas as pd

# Load the dataset
df = pd.read_csv("Toyota.csv")

# a. Display the shape, summary, and count of missing values in the dataset
# Displaying the shape of the dataset (rows and columns)
print("Shape of the dataset:", df.shape)
# Displaying a summary of the dataset, which includes statistics like mean, std, min, and max for numeric columns
print("\nSummary of the dataset:")
print(df.describe())
# Count of missing values for each column
print("\nCount of missing values:")
print(df.isnull().sum())

# b. Remove duplicate records
# Dropping any duplicate rows in the dataset
df_cleaned = df.drop_duplicates()
# Displaying the shape of the dataset after removing duplicates
print("\nShape after removing duplicates:", df_cleaned.shape)

# c. Clean the dataset by replacing missing values with appropriate values
# Convert 'KM' and 'HP' columns to numeric, forcing errors (non-numeric) to NaN
df_cleaned['KM'] = pd.to_numeric(df_cleaned['KM'], errors='coerce')
df_cleaned['HP'] = pd.to_numeric(df_cleaned['HP'], errors='coerce')

# Fill missing values in various columns with the most appropriate value
# Filling missing values in the 'Price' column with the mean of the column
df_cleaned['Price'].fillna(df_cleaned['Price'].mean(), inplace=True)
# Filling missing values in 'Age' with the median (because age is typically more stable)
df_cleaned['Age'].fillna(df_cleaned['Age'].median(), inplace=True)
# Filling missing values in the 'KM' and 'HP' columns with the median
df_cleaned['KM'].fillna(df_cleaned['KM'].median(), inplace=True)
df_cleaned['HP'].fillna(df_cleaned['HP'].median(), inplace=True)
# Filling missing values in the 'CC' column with the median
df_cleaned['CC'].fillna(df_cleaned['CC'].median(), inplace=True)
# Filling missing values in 'Doors' column with the most frequent value (mode)
df_cleaned['Doors'].fillna(df_cleaned['Doors'].mode()[0], inplace=True)
# Filling missing values in 'Weight' column with the mean
df_cleaned['Weight'].fillna(df_cleaned['Weight'].mean(), inplace=True)

# For categorical columns (FuelType, MetColor, Automatic), we replace missing values with the most frequent value (mode)
df_cleaned['FuelType'].fillna(df_cleaned['FuelType'].mode()[0], inplace=True)
df_cleaned['MetColor'].fillna(df_cleaned['MetColor'].mode()[0], inplace=True)
df_cleaned['Automatic'].fillna(df_cleaned['Automatic'].mode()[0], inplace=True)

# Display the cleaned dataset's missing values count after replacement
print("\nCount of missing values after cleaning:")
print(df_cleaned.isnull().sum())

# d. Convert the datatype of 'MetColor' and 'Automatic' columns to object type
# Converting 'MetColor' and 'Automatic' columns to object type because they are categorical and should be treated as strings
df_cleaned['MetColor'] = df_cleaned['MetColor'].astype('object')
df_cleaned['Automatic'] = df_cleaned['Automatic'].astype('object')

# Display the data types of the columns after conversion
print("\nData types after conversion:")
print(df_cleaned.dtypes)

