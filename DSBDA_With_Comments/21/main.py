import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv('Toyota.csv')

# a. Get unique values of categorical 'Doors'
# This helps us understand what distinct values exist in the 'Doors' column, whether it's numeric or contains other formats
unique_doors = df['Doors'].unique()
print("Unique values in 'Doors':", unique_doors)

# b. Transform all values in 'Doors' to the same format (numeric or string)
# We want to ensure all 'Doors' values are numeric for consistency
# Convert the 'Doors' column to string format, then extract any numeric value present (digits only)
df['Doors'] = df['Doors'].astype(str).str.extract('(\d)')  # Extract numbers if present, else will remain NaN
# Fill NaN values with '4' (assuming most cars have 4 doors) and convert the result to integer format
df['Doors'] = df['Doors'].fillna('4').astype(int)  # Fill NaN with 4 and convert to int
print("Unique 'Doors' values after transformation:", df['Doors'].unique())

# c. Apply Decimal scaling normalization on 'HP'
# First, we ensure the 'HP' column is numeric, converting any non-numeric entries to NaN
df['HP'] = pd.to_numeric(df['HP'], errors='coerce')

# Find the maximum absolute value in the 'HP' column (ignoring NaN values)
max_hp = df['HP'].max()

# Check if the max_hp is not NaN and not zero (to avoid invalid scaling)
if pd.notna(max_hp) and max_hp != 0:
    # Decimal scaling factor is determined by the number of digits in the maximum 'HP' value
    decimal_scale_factor = 10 ** len(str(abs(int(max_hp))))  # Find the scale factor by the number of digits in the max HP
    # Apply decimal scaling by dividing the 'HP' values by the decimal scale factor
    df['HP_normalized'] = df['HP'] / decimal_scale_factor
    print("Normalized HP values (Decimal Scaling):", df[['HP', 'HP_normalized']].head())
else:
    print("Max HP value is either NaN or 0, unable to apply Decimal Scaling.")

# Optional: Save the transformed data to a new CSV file
# df.to_csv('Toyota_transformed.csv', index=False)

