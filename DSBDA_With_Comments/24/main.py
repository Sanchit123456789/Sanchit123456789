import pandas as pd
from scipy.stats import zscore

# Load the dataset
df = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/Toyota.csv")

# Display first 5 rows to check the structure
df.head()

# Print the column names to inspect the dataset structure
print(df.columns)

# a. Add a new column 'Revised' specifying 5% increase in old Price
# We create a new column 'Revised' by increasing the 'Price' by 5%
df['Revised'] = df['Price'] * 1.05

# b. Create a subset of cars' data having Price > 15000 and Age < 8
# We filter the dataset for cars with Price greater than 15000 and Age less than 8
subset_df = df[(df['Price'] > 15000) & (df['Age'] < 8)]

# c. Sort observations in descending order of 'Revised' Price
# Sorting the dataset based on 'Revised' column in descending order
df_sorted = df.sort_values(by='Revised', ascending=False)

# d. Apply Z-score normalization on 'HP' column
# First, we ensure that the 'HP' column contains numeric values and handle errors by coercing non-numeric entries to NaN
df['HP'] = pd.to_numeric(df['HP'], errors='coerce')

# Apply Z-score normalization to the 'HP' column
# Z-score is calculated by subtracting the mean and dividing by the standard deviation
df['HP_Zscore'] = zscore(df['HP'].dropna())  # We drop NaN values to avoid issues in the calculation

# Display results
print("Subset of Cars (Price > 15000, Age < 8):\n", subset_df[['Price', 'Age']].head())
print("\nData Sorted by Revised Price:\n", df_sorted[['Price', 'Revised']].head())
print("\nZ-score Normalized HP:\n", df[['HP', 'HP_Zscore']].head())

