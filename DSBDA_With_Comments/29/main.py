import pandas as pd

# Load the Salaries dataset
df = pd.read_csv('Salaries.csv')

# a. Get the rank and salary of all staff that does NOT belong to discipline A
staff_not_in_discipline_A = df[df['discipline'] != 'A'][['rank', 'salary']]
print("\n[a] Rank and Salary of staff NOT in Discipline A:")
print(staff_not_in_discipline_A)

# b. Get rank, salary, and years of service of:
#    - all male staff
#    - only female professors
male_staff = df[df['sex'] == 'Male'][['rank', 'salary', 'service']]
female_professors = df[(df['sex'] == 'Female') & (df['rank'] == 'Prof')][['rank', 'salary', 'service']]

# Combine the two groups using concat
staff_combined = pd.concat([male_staff, female_professors])
print("\n[b] Rank, Salary, and Service of all Male Staff and Female Professors:")
print(staff_combined)

# c. Get all female staff who are:
#    - either Professors OR
#    - earning more than 75000
female_staff_condition = df[(df['sex'] == 'Female') & ((df['rank'] == 'Prof') | (df['salary'] > 75000))]
print("\n[c] Female staff who are Professors OR earning > 75000:")
print(female_staff_condition[['rank', 'salary', 'sex']])

# d. Get rank and salary of all staff who:
#    - are NOT Professors
#    - AND have at least 10 years of service
non_professors_service_10_years = df[(df['rank'] != 'Prof') & (df['service'] >= 10)][['rank', 'salary']]
print("\n[d] Rank and Salary of Non-Professors with ≥10 years of service:")
print(non_professors_service_10_years)

