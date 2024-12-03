import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('AQI_Data.csv')

# a) Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head(5))  # Display the first 5 rows of the DataFrame

# b) Display the last 6 rows
print("\nLast 6 rows of the dataset:")
print(df.tail(6))  # Display the last 6 rows of the DataFrame

# c) Show the summary statistics for all numeric columns
print("\nSummary statistics for all numeric columns:")
print(df.describe())  # Display summary statistics for numeric columns

# d) Use numpy to compute the mean AQI, PM2.5, and PM10 values for each city
print("\nMean AQI, PM2.5, and PM10 values for each city:")
# Assuming the dataset has columns named 'City', 'AQI', 'PM2.5', and 'PM10'
mean_values = df.groupby('City')[['AQI', 'PM2.5', 'PM10']].mean().reset_index()

# Display the mean values
print(mean_values)  # Display the mean values for each city