# Import necessary libraries
import pandas as pd

# Load the dataset
schools = pd.read_csv("schools.csv")

# Display the first few rows of the dataset
schools.head() 

# Filter schools with average math scores above 80% of the maximum score (800)
best_avg_maths = schools['average_math'] >= (0.8 * 800) 

# Create a subset of schools that meet the criteria
best_in_maths = schools[best_avg_maths] 

# Sort the schools by average math score in descending order
best_in_maths_srt = best_in_maths.sort_values('average_math', ascending=False)

# Select only the school name and average math score columns
best_math_schools = best_in_maths_srt.loc[:, ['school_name', 'average_math']]

# Display the first few rows of the best math schools
best_math_schools.head()

# Create a new column for total SAT scores by summing average math, reading, and writing scores
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing'] 

# Sort the schools by total SAT scores in descending order and select the top 10
top_10_schools = (schools.sort_values('total_SAT', ascending=False)).head(10)

# Select only the school name and total SAT score columns
top_10_schools = top_10_schools.loc[:, ['school_name', 'total_SAT']] 

# Calculate the mean and standard deviation of total SAT scores for each borough
borough_sat_mean_std = schools.groupby('borough')['total_SAT'].agg(['std', 'mean']).round(2) 

# Add num_schools column with number of schools in each borough 
borough_sat_mean_std['num_schools'] = schools['borough'].value_counts()

# Find the maximum standard deviation of total SAT scores across boroughs
std_max = borough_sat_mean_std['std'].max() 

# Filter the boroughs with the maximum standard deviation
largest_std_dev = borough_sat_mean_std[borough_sat_mean_std['std'] == std_max]

# Rearrange the columns to have 'num_schools', 'mean', and 'std' in that order
largest_std_dev = largest_std_dev[['num_schools', 'mean', 'std']]

# Define a dictionary to rename the columns
names_dict = {'mean': 'average_SAT', 'std':'std_SAT'} 

# Rename the columns using the dictionary
largest_std_dev = largest_std_dev.rename(columns=names_dict)

