import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('AQI_Data.csv')

# A) Check for missing values in the dataset
print("Missing values in each column before replacement:")
print(df.isnull().sum())  # Display the count of missing values in each column

# Replace missing values in numeric columns with the column mean
numeric_cols = df.select_dtypes(include=[np.number]).columns  # Get numeric columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())  # Replace NaN with mean

# Print the updated DataFrame
print("\nUpdated DataFrame after replacing missing values with column means:")
print(df)

# B) Extract the AQI column as a NumPy array
aqi_values = df['AQI'].to_numpy()  # Extract AQI column as a NumPy array

# Calculate and display the mean, median, and standard deviation of the AQI values
mean_aqi = np.mean(aqi_values)
median_aqi = np.median(aqi_values)
std_aqi = np.std(aqi_values)

print("\nStatistics for AQI values:")
print(f"Mean AQI: {mean_aqi}")
print(f"Median AQI: {median_aqi}")
print(f"Standard Deviation of AQI: {std_aqi}")