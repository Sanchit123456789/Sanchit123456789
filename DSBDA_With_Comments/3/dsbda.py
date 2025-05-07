import pandas as pd  # For handling tabular data
import numpy as np   # For numerical operations

# Load the housing dataset
housing = pd.read_csv("housing.csv")
housing.head()  # Displays the first 5 rows (in Jupyter)

# Create a new column 'average_rooms' by dividing total rooms by number of households
housing['average_rooms'] = housing['total_rooms'] / housing['households']

# Filter data where median income is greater than 5 and average rooms is less than 6
subset = housing[(housing['median_income'] > 5) & (housing['average_rooms'] < 6)]
print("\nSubset of Data:\n", subset.head())  # Displaying the first few rows of the filtered subset

print("\nSubset of Data:\n", subset.head())  # Redundant line (repeats the same print output)

# Create a DataFrame with region info based on specific latitude and longitude
region_lookup = pd.DataFrame({
    'latitude': [34.19, 37.85],
    'longitude': [-118.5, -122.3],
    'region': ['Southern CA', 'Northern CA']
})

# Round latitude and longitude to 2 decimal places in both subset and region_lookup
subset['lat_rounded'] = subset['latitude'].round(2)
subset['lon_rounded'] = subset['longitude'].round(2)
region_lookup['lat_rounded'] = region_lookup['latitude'].round(2)
region_lookup['lon_rounded'] = region_lookup['longitude'].round(2)

# Merge subset with region_lookup on rounded lat & lon to assign region
merged = pd.merge(subset, region_lookup, on=['lat_rounded', 'lon_rounded'], how='left')
print("\nMerged Data:\n", merged[['median_income', 'average_rooms', 'region']].head())  # Showing merged result

# Sort merged data by house value and population, both in descending order
sorted_data = merged.sort_values(by=['median_house_value', 'population'], ascending=[False, False])
print("\nSorted Data:\n", sorted_data[['median_house_value', 'population']].head())

# Generate descriptive statistics and transpose the result for readability
summary_stats = housing.describe().transpose()
print("\nTransposed Summary Stats:\n", summary_stats)

# Create income bins using pd.cut to categorize median_income into labeled ranges
housing['income_bin'] = pd.cut(housing['median_income'], bins=[0,2,4,6,8,10,15], labels=['0-2','2-4','4-6','6-8','8-10','10+'])

# Similarly, categorize housing age into age groups using bins
housing['age_bin'] = pd.cut(housing['housing_median_age'], bins=[0,10,20,30,40,50,60], labels=['0-10','10-20','20-30','30-40','40-50','50+'])

# Create a pivot table to compute average house value for each combination of income_bin and age_bin
pivot = housing.pivot_table(values='median_house_value', index='income_bin', columns='age_bin', aggfunc='mean')
print("\nAverage House Value (Pivot Table):\n", pivot)

