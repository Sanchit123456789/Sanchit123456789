import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# ----- Load the datasets -----
# Read the applicants and exam_scores CSV files into pandas DataFrames
applicants = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/applicants.csv")
exam_scores = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/exam_scores.csv")

# Display the first few rows of both DataFrames to understand the data
applicants.head()
exam_scores.head()

# Print column names to inspect the structure of both DataFrames
print(applicants.columns)
print(exam_scores.columns)

# ----- Fill missing SAT/ACT scores -----
# Fill missing SAT and ACT scores with the mean of each column
exam_scores[['SAT', 'ACT']] = exam_scores[['SAT', 'ACT']].fillna(exam_scores[['SAT', 'ACT']].mean())

# ----- Merge applicants and exam_scores -----
# Join the applicants DataFrame with the exam_scores DataFrame on 'ApplicationID'
# 'inner' merge will only keep rows that match in both DataFrames
combined = pd.merge(applicants, exam_scores, on='ApplicationID', how='inner')

# ----- Normalize SAT/ACT scores -----
# Apply Min-Max scaling to normalize SAT and ACT scores between 0 and 1
scaler = MinMaxScaler()
combined[['SAT', 'ACT']] = scaler.fit_transform(combined[['SAT', 'ACT']])

# ----- Convert Admission_Status to binary -----
# Strip extra spaces and convert Admission_Status to lowercase for consistency
combined['Admission_Status'] = combined['Admission_Status'].str.strip().str.lower()

# Create a new column 'Admission_Label' where 'admitted' = 1 and 'not admitted' = 0
combined['Admission_Label'] = combined['Admission_Status'].apply(lambda x: 1 if x == 'admitted' else 0)

# ----- Remove duplicates and fix invalid scores -----
# Remove duplicate rows based on the 'ApplicationID' column to keep only unique records
combined = combined.drop_duplicates(subset='ApplicationID')

# ----- (Optional) Reverse the normalization for SAT/ACT and handle invalid scores -----
# Inverse transform to approximate original SAT and ACT scores
combined['SAT_orig'] = scaler.inverse_transform(combined[['SAT', 'ACT']])[:, 0]
combined['ACT_orig'] = scaler.inverse_transform(combined[['SAT', 'ACT']])[:, 1]

# Set any originally invalid SAT/ACT scores to NaN if they fall outside valid ranges
# SAT score should be between 400 and 1600, ACT should be between 1 and 36
combined.loc[(combined['SAT_orig'] < 400) | (combined['SAT_orig'] > 1600), 'SAT'] = None
combined.loc[(combined['ACT_orig'] < 1) | (combined['ACT_orig'] > 36), 'ACT'] = None

# ----- Drop helper columns -----
# Drop the 'SAT_orig' and 'ACT_orig' columns used for validation, as they are no longer needed
combined.drop(['SAT_orig', 'ACT_orig'], axis=1, inplace=True)

# ----- Final cleaned data -----
# Display the final cleaned and combined data
print("\nCleaned & Combined Data:\n", combined.head())

