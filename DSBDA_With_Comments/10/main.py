import pandas as pd

# ----- Load the datasets -----
# Read the employee information and performance CSV files into pandas DataFrames
emp_df = pd.read_csv('employee_info.csv')
perf_df = pd.read_csv('performance.csv')

# ----- Clean invalid ages -----
# If the age is greater than 100, set it to 100 (or you can drop these rows if needed)
emp_df['Age'] = emp_df['Age'].apply(lambda x: 100 if x > 100 else x)

# ----- Clean join dates -----
# Convert 'JoinDate' to datetime, and coerce any errors (invalid dates) to NaT (Not a Time)
emp_df['JoinDate'] = pd.to_datetime(emp_df['JoinDate'], errors='coerce')

# Drop rows where 'JoinDate' is NaT (invalid or missing join date)
emp_df = emp_df.dropna(subset=['JoinDate'])

# ----- Clean department names -----
# Strip any leading/trailing spaces and capitalize the first letter of each word in the department name
emp_df['Department'] = emp_df['Department'].str.strip().str.title()

# Display cleaned employee data
print("\nCleaned Employee Info:\n", emp_df.head())

# ----- Merge the dataframes -----
# Merge employee info (emp_df) with performance data (perf_df) based on 'EmployeeID'
# This will keep only rows that have matching 'EmployeeID' in both DataFrames
combined_df = pd.merge(emp_df, perf_df, on='EmployeeID', how='inner')

# Display the combined dataset
print("\nCombined Dataset:\n", combined_df.head())

# ----- Calculate average review score -----
# Create a new column 'AverageScore' by taking the mean of 'ReviewScore1' and 'ReviewScore2' for each employee
combined_df['AverageScore'] = combined_df[['ReviewScore1', 'ReviewScore2']].mean(axis=1)

# Display the data with the calculated average score
print("\nWith Average Score:\n", combined_df[['EmployeeID', 'AverageScore']].head())

# ----- Categorize performance based on average score -----
# Define a function to categorize performance into 'Low', 'Medium', or 'High' based on average score
def performance_bucket(score):
    if score < 60:
        return 'Low'
    elif score < 80:
        return 'Medium'
    else:
        return 'High'

# Apply the 'performance_bucket' function to the 'AverageScore' column to create a 'PerformanceCategory' column
combined_df['PerformanceCategory'] = combined_df['AverageScore'].apply(performance_bucket)

# Display the data with the performance category
print("\nWith Performance Category:\n", combined_df[['EmployeeID', 'AverageScore', 'PerformanceCategory']].head())

# ----- Handle missing or invalid department names -----
# Replace any blank departments with 'Unknown'
combined_df['Department'] = combined_df['Department'].replace('', 'Unknown')

# (Optional) If you have a predefined list of valid departments, replace any mismatched department names with 'Unknown'
valid_departments = ['Sales', 'Hr', 'Engineering', 'Marketing', 'Finance']
combined_df['Department'] = combined_df['Department'].apply(
    lambda x: x if x in valid_departments else 'Unknown'
)

# Display the final cleaned dataset
print("\nFinal Cleaned Dataset:\n", combined_df.head())

