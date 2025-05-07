import pandas as pd

# ----- Load the datasets -----
# Read the CSV files into pandas DataFrames
patients_df = pd.read_csv('patients.csv')
visits_df = pd.read_csv('visits.csv')

# ----- Handle missing values -----
# Fill missing diagnosis codes in visits_df with 'Unknown'
visits_df['Diagnosis'] = visits_df['Diagnosis'].fillna('Unknown')

# Fill missing ages in patients_df with the median age (the middle value of the Age column)
patients_df['Age'] = patients_df['Age'].fillna(patients_df['Age'].median())

# Display the cleaned datasets to confirm missing values were handled
print("\nPatients DataFrame after handling missing ages:\n", patients_df.head())
print("\nVisits DataFrame after handling missing diagnosis codes:\n", visits_df.head())

# ----- Standardize gender values -----
# Replace inconsistent gender values with consistent 'Male' and 'Female'
patients_df['Gender'] = patients_df['Gender'].replace({
    'M': 'Male', 'Male': 'Male',
    'F': 'Female', 'Female': 'Female'
})

# Display the standardized gender column
print("\nPatients DataFrame with standardized gender:\n", patients_df.head())

# ----- Merge datasets on PatientID -----
# Merge visits_df with patients_df using 'PatientID' as the key to combine the information
# The 'inner' merge will only keep the rows that match on 'PatientID' in both DataFrames
merged_df = pd.merge(visits_df, patients_df, on='PatientID', how='inner')

# Display the merged DataFrame to confirm the result
print("\nMerged DataFrame:\n", merged_df.head())

# ----- Group by PatientID to summarize visits -----
# Group the merged DataFrame by 'PatientID' and aggregate:
# - Count the total number of visits for each patient
# - Count the number of unique diagnoses each patient has
grouped_df = merged_df.groupby('PatientID').agg(
    total_visits=('VisitID', 'count'),   # Count of VisitID per patient
    unique_diagnoses=('Diagnosis', 'nunique')  # Number of unique diagnoses per patient
).reset_index()

# Display the grouped data to check the total visits and unique diagnoses per patient
print("\nGrouped DataFrame with total visits and unique diagnoses:\n", grouped_df.head())

# ----- Correct out-of-range values for age -----
# Ensure no age exceeds 120, if so, replace with 120 (realistic age cap)
merged_df['Age'] = merged_df['Age'].apply(lambda x: 120 if x > 120 else x)

# Display the DataFrame after correcting the ages
print("\nMerged DataFrame after correcting out-of-range ages:\n", merged_df.head())

