import numpy as np
import pandas as pd

# To Load the dataset
df = pd.read_csv('weather_data.csv')

# To Display the first few rows of the dataset
print(df.head())

# To Display basic information about the dataset
print(df.info())

# To Display basic statistical details
print(df.describe())

# To Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Fill missing values with the mean of the respective columns
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
df['humidity'] = df['humidity'].fillna(df['humidity'].mean())
df['precipitation'] = df['precipitation'].fillna(df['precipitation'].mean())

# To Ensure there are no missing values
print(df.isnull().sum())

# To Convert to numpy arrays for numerical operations
temperature = df['temperature'].to_numpy()
humidity = df['humidity'].to_numpy()
precipitation = df['precipitation'].to_numpy()

# To Calculate some statistics using Numpy
mean_temperature = np.mean(temperature)
median_temperature = np.median(temperature)
variance_temperature = np.var(temperature)

mean_humidity = np.mean(humidity)
median_humidity = np.median(humidity)
variance_humidity = np.var(humidity)

mean_precipitation = np.mean(precipitation)
median_precipitation = np.median(precipitation)
variance_precipitation = np.var(precipitation)

print(f'Mean temperature: {mean_temperature}')
print(f'Median temperature: {median_temperature}')
print(f'Variance of temperature: {variance_temperature}')

print(f'Mean humidity: {mean_humidity}')
print(f'Median humidity: {median_humidity}')
print(f'Variance of humidity: {variance_humidity}')

print(f'Mean precipitation: {mean_precipitation}')
print(f'Median precipitation: {median_precipitation}')
print(f'Variance of precipitation: {variance_precipitation}')

# Using pandas to summarize the data
summary_stats = df.describe()

mean_temp_pd = summary_stats.loc['mean', 'temperature']
median_temp_pd = df['temperature'].median()
variance_temp_pd = df['temperature'].var()

mean_humidity_pd = summary_stats.loc['mean', 'humidity']
median_humidity_pd = df['humidity'].median()
variance_humidity_pd = df['humidity'].var()

mean_precipitation_pd = summary_stats.loc['mean', 'precipitation']
median_precipitation_pd = df['precipitation'].median()
variance_precipitation_pd = df['precipitation'].var()

print("\nSummary Statistics using Pandas:")
print(f'Mean temperature: {mean_temp_pd}')
print(f'Median temperature: {median_temp_pd}')
print(f'Variance of temperature: {variance_temp_pd}')

print(f'Mean humidity: {mean_humidity_pd}')
print(f'Median humidity: {median_humidity_pd}')
print(f'Variance of humidity: {variance_humidity_pd}')

print(f'Mean precipitation: {mean_precipitation_pd}')
print(f'Median precipitation: {median_precipitation_pd}')
print(f'Variance of precipitation: {variance_precipitation_pd}')
