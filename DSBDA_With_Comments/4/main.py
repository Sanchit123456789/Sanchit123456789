import pandas as pd  # Importing pandas for data manipulation

# Load the Wine Quality dataset
df = pd.read_csv('WineQT.csv')  # Replace with the correct file path if needed

# ----- a. Subset wines where quality ≥ 7 and alcohol > 10% -----
subset_a = df[(df['quality'] >= 7) & (df['alcohol'] > 10)]
print("\nSubset (quality ≥ 7 and alcohol > 10%):\n", subset_a.head())

# Explanation:
# - This filters wines that are of higher quality (7 or above)
# - Also ensures alcohol content is above 10%

# ----- b. Merge red and white wine datasets -----
# Simulate having separate datasets by duplicating the original and assigning types

red_wine = df.copy()           # Simulate red wine dataset
red_wine['type'] = 'red'       # Add 'type' column to indicate red wine

white_wine = df.copy()         # Simulate white wine dataset
white_wine['type'] = 'white'   # Add 'type' column to indicate white wine

# Combine both datasets into one using concat
merged_df = pd.concat([red_wine, white_wine], ignore_index=True)
print("\nMerged red and white wines:\n", merged_df.head())

# Explanation:
# - This creates a combined DataFrame with both red and white wines
# - Useful for comparison or modeling based on wine type

# ----- c. Sort wines by citric acid and residual sugar -----
sorted_df = df.sort_values(by=['citric acid', 'residual sugar'])
print("\nSorted by citric acid and residual sugar:\n", sorted_df.head())

# Explanation:
# - This sorts the dataset first by 'citric acid' (ascending by default)
# - If two rows have the same citric acid, it uses 'residual sugar' as a tiebreaker

# ----- d. Transpose summary statistics of chemical properties by quality -----
summary_stats = df.groupby('quality').agg({
    'fixed acidity': 'mean',
    'volatile acidity': 'mean',
    'citric acid': 'mean',
    'residual sugar': 'mean',
    'chlorides': 'mean',
    'alcohol': 'mean'
})

transposed_stats = summary_stats.transpose()
print("\nTransposed summary statistics:\n", transposed_stats)

# Explanation:
# - Groups data by 'quality' and computes average values for each chemical feature
# - Transposing makes qualities as columns and features as rows, easier for comparison

# ----- e. Pivot table showing average key features by wine quality -----
pivot_table = df.pivot_table(
    index='quality',
    values=['alcohol', 'residual sugar', 'citric acid', 'pH'],
    aggfunc='mean'
)
print("\nPivot table (average values by quality):\n", pivot_table)

# Explanation:
# - A pivot table summarizes the dataset by showing the average values of selected features
# - Grouped by wine 'quality'

