import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv("/Users/chetan suryawanshi/Downloads/DataSet for Exam/Heart.csv")

# Display the first few rows to understand the structure of the dataset
df.head()

# Print column names to understand the dataset's features
print(df.columns)

# a. Fill missing values in 'chol', 'restecg', and 'thal' columns
# - 'chol' is filled with the median of its column (assuming numerical data)
# - 'restecg' and 'thal' are filled with the most frequent (mode) value in their respective columns
df['chol'] = df['chol'].fillna(df['chol'].median())
df['restecg'] = df['restecg'].fillna(df['restecg'].mode()[0])
df['thal'] = df['thal'].fillna(df['thal'].mode()[0])

# b. One-Hot Encoding for categorical columns: 'sex', 'cp', and 'thal'
# - One-Hot Encoding creates binary columns for each category in the original categorical feature
# - drop_first=True removes the first category to avoid the dummy variable trap (multicollinearity)
df = pd.get_dummies(df, columns=['sex', 'cp', 'thal'], drop_first=True)

# c. Create AgeGroup column based on age ranges
# - The age group is categorized into 'young', 'middle-aged', and 'elderly'
def age_group(age):
    if age < 40:
        return 'young'
    elif 40 <= age < 60:
        return 'middle-aged'
    else:
        return 'elderly'

df['AgeGroup'] = df['age'].apply(age_group)

# Optional: One-Hot Encode AgeGroup for modeling
# - One-Hot Encoding will create binary columns for the different age groups
df = pd.get_dummies(df, columns=['AgeGroup'], drop_first=True)

# d. Normalize features: 'chol', 'thalach', and 'oldpeak' using StandardScaler
# - StandardScaler standardizes the data to have a mean of 0 and standard deviation of 1
scaler = StandardScaler()
df[['chol', 'thalach', 'oldpeak']] = scaler.fit_transform(df[['chol', 'thalach', 'oldpeak']])

# e. Prepare features and target variable
# - X will hold the features (independent variables)
# - y will hold the target variable (dependent variable, 'target')
X = df.drop('target', axis=1)
y = df['target']

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier model using the training data
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance using accuracy score and classification report
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

