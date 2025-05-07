import pandas as pd  # Importing pandas for data manipulation

# Reading the dataset into a DataFrame
df = pd.read_csv('StudentsPerformance.csv')
df  # Displays the DataFrame (in Jupyter, it would auto-display)

# Filtering students who scored above 80 in math and completed the test preparation course
subset_a = df[(df['math score'] > 80) & (df['test preparation course'] == 'completed')]
print("\nSubset a:\n", subset_a.head())  # Displaying top 5 records of the filtered subset



# Adding a unique student_id column for merging purpose
df['student_id'] = range(1, len(df) + 1)  # Assigning IDs starting from 1

# Creating a list of socioeconomic statuses: high, medium, low (cycled to match DataFrame length)
statuses = (['high', 'medium', 'low'] * ((len(df) // 3) + 1))[:len(df)]  # Repeats and trims the list

# Creating a new DataFrame with student_id and socioeconomic status
demographic_df = pd.DataFrame({
    'student_id': range(1, len(df) + 1),
    'socioeconomic status': statuses
})

# Merging the original DataFrame with the demographic data on student_id
merged_b = pd.merge(df, demographic_df, on='student_id')
print("\nMerged dataset:\n", merged_b.head())  # Showing first 5 rows of the merged data



# Sorting students by reading and writing scores in descending order
sorted_c = df.sort_values(by=['reading score', 'writing score'], ascending=False)
print("\nSorted c:\n", sorted_c.head())  # Displaying top 5 students based on scores

# Grouping data by gender and calculating average math, reading, and writing scores
avg_scores = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()

# Transposing the result to switch rows and columns
transposed_d = avg_scores.transpose()
print("\nTransposed d (average scores by gender):\n", transposed_d)



# Creating a pivot table to show average scores grouped by lunch type and test prep course status
pivot_e = pd.pivot_table(
    df,
    index=['lunch', 'test preparation course'],  # Grouping by these two columns
    values=['math score', 'reading score', 'writing score'],  # Aggregating these score columns
    aggfunc='mean'  # Taking the mean for each group
)
print("\nPivot table e (average scores by lunch and test prep):\n", pivot_e)

