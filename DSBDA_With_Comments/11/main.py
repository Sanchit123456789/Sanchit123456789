import pandas as pd
import numpy as np

# ----- Load the Titanic dataset -----
df = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/Titanic-Dataset.csv")

# Display the first few rows and columns of the dataset
df.head()
print(df.columns)

# ----- a. Handle missing Age and Cabin values -----
# Fill missing 'Age' values with the median value of the 'Age' column
df['Age'] = df['Age'].fillna(df['Age'].median())  # Using median to handle missing age values

# Fill missing 'Cabin' values with 'Unknown'
df['Cabin'] = df['Cabin'].fillna('Unknown')  # 'Unknown' is used for missing cabin info

# ----- b. Convert 'Sex' and 'Embarked' columns to numeric -----
# First, fill missing values in 'Embarked' with the most frequent (mode) value
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # Filling missing 'Embarked' with mode

# Convert 'Sex' from categorical values ('male', 'female') to numeric (0, 1)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Convert 'Embarked' from categorical values ('S', 'C', 'Q') to numeric (0, 1, 2)
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# ----- c. Create a new feature 'FamilySize' -----
# Create a new feature 'FamilySize' which is the sum of 'SibSp' (siblings/spouse aboard) and 'Parch' (parents/children aboard)
df['FamilySize'] = df['SibSp'] + df['Parch']  # FamilySize represents the total number of family members on board

# ----- d. Bin 'Fare' into categories -----
# Define bins for the 'Fare' column: low, medium, high, and very high
fare_bins = [-1, 7.91, 14.454, 31, df['Fare'].max()]  # Fare bins based on distribution of fare values
fare_labels = ['Low', 'Medium', 'High', 'Very High']  # Labels for each fare category

# Apply the bins to 'Fare' and create a new column 'FareCategory' based on the specified labels
df['FareCategory'] = pd.cut(df['Fare'], bins=fare_bins, labels=fare_labels)

# Show the processed data with selected columns
print(df[['Age', 'Cabin', 'Sex', 'Embarked', 'FamilySize', 'Fare', 'FareCategory']].head())

