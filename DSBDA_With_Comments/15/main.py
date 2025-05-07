import pandas as pd

# Load the dataset
df = pd.read_csv('Toyota.csv')

# ----- a. Data Cleaning -----
# Checking initial missing values in the dataset
print("Initial missing values:\n", df.isnull().sum())

# Convert numeric columns to proper numeric, forcing errors to NaN
# These columns represent numerical data but might contain some non-numeric values
numeric_cols = ['Price', 'Age', 'KM', 'HP', 'CC', 'Weight']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Converts to numeric, non-convertible values become NaN

# Fill missing numerical values with median for each column
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())  # Replaces NaN with median

# Fill missing categorical values with mode for each column
categorical_cols = ['FuelType', 'MetColor', 'Automatic', 'Doors']
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])  # Replaces NaN with mode (most frequent value)

# Checking if missing values have been handled
print("After cleaning missing values:\n", df.isnull().sum())

# Remove duplicate rows from the dataset
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates()  # Removes duplicate rows
print("Duplicates after:", df.duplicated().sum())

# ----- b. Data Integration -----
# Example of integrating external data (Fuel Efficiency Ratings)
fuel_efficiency = pd.DataFrame({
    'FuelType': ['Petrol', 'Diesel', 'CNG'],
    'EfficiencyRating': [3, 4, 5]  # Hypothetical efficiency ratings
})
# Merging fuel efficiency data into the main dataframe based on 'FuelType'
df = pd.merge(df, fuel_efficiency, on='FuelType', how='left')

# ----- c. Data Transformation -----
# Adding 'Age_Years' by converting months to years
df['Age_Years'] = df['Age'] / 12  # Dividing Age by 12 to get age in years

# Normalizing 'KM' (kilometers driven) to a 0-1 scale for easier comparison
df['KM_Normalized'] = (df['KM'] - df['KM'].min()) / (df['KM'].max() - df['KM'].min())

# ----- d. Error Correcting -----
# Ensuring that 'HP' and 'CC' are positive by taking absolute values
df['HP'] = df['HP'].apply(lambda x: abs(x) if x < 0 else x)  # Correct negative horsepower values
df['CC'] = df['CC'].apply(lambda x: abs(x) if x < 0 else x)  # Correct negative engine capacity values

# Correcting invalid 'Doors' values by replacing them with the most frequent valid value
door_mode = df['Doors'].mode()[0]  # Get the most frequent valid number of doors
df['Doors'] = df['Doors'].apply(lambda x: door_mode if x not in [2, 3, 4, 5] else x)

# Preview the final cleaned dataset
print("\nFinal cleaned dataset preview:\n", df.head())

# Optionally save cleaned data to a new file (uncomment to save)
# df.to_csv('Toyota_cleaned.csv', index=False)

