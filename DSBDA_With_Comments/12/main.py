import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ----- Load the dataset -----
df = pd.read_csv('StudentsPerformance.csv')  # Load the student performance dataset

# ----- Check and fill missing test scores with their column mean -----
# For each of the columns 'math score', 'reading score', and 'writing score', 
# we check if there are any missing values and fill them with the mean of the respective column
for col in ['math score', 'reading score', 'writing score']:
    if df[col].isnull().sum() > 0:  # Check if there are missing values in the column
        df[col] = df[col].fillna(df[col].mean())  # Fill missing values with the column's mean

# Show the first few rows of the test score columns after imputing missing values
print("\nAfter imputing missing test scores:\n", df[['math score', 'reading score', 'writing score']].head())

# ----- Calculate the average score -----
# Calculate the average score for each student based on their math, reading, and writing scores
df['AverageScore'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Show the dataset with the calculated average score
print("\nWith Average Score:\n", df[['math score', 'reading score', 'writing score', 'AverageScore']].head())

# ----- Define performance bands -----
# Define a function to categorize students based on their average score
def performance_band(score):
    if score >= 85:
        return 'Excellent'  # Excellent performance if the score is 85 or higher
    elif score >= 60:
        return 'Average'  # Average performance if the score is between 60 and 85
    else:
        return 'Poor'  # Poor performance if the score is below 60

# Apply the performance_band function to each student's average score
df['PerformanceBand'] = df['AverageScore'].apply(performance_band)

# Show the dataset with the new performance band
print("\nWith Performance Band:\n", df[['AverageScore', 'PerformanceBand']].head())

# ----- Check for duplicates -----
# Check if there are any duplicate rows in the dataset
duplicates = df.duplicated()
print("\nNumber of duplicate records:", duplicates.sum())  # Print the number of duplicates

# ----- Optional: Remove duplicates -----
# If there are any duplicates, remove them
df = df.drop_duplicates()

# Show the shape of the dataset after removing duplicates (rows, columns)
print("\nData after removing duplicates:", df.shape)

# ----- Apply Label Encoding -----
# Create an instance of LabelEncoder to convert categorical columns into numeric values
le = LabelEncoder()

# Encode the 'gender', 'lunch', and 'test preparation course' columns
# The encoded columns will have suffix '_Encoded' added to the original column names
for col in ['gender', 'lunch', 'test preparation course']:
    df[col + '_Encoded'] = le.fit_transform(df[col])

# Show the first few rows of the dataset with the encoded columns
print("\nWith Encoded Columns:\n", df[['gender', 'gender_Encoded', 'lunch', 'lunch_Encoded', 
                                      'test preparation course', 'test preparation course_Encoded']].head())

