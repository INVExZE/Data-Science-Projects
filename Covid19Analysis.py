import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('covid19_data.csv')

# Display the first few rows of the dataset
print(df.head())

# Display basic information about the dataset
print(df.info())

# Display basic statistical details
print(df.describe())

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Fill missing values with 0
df = df.fillna(0)

# Group data by date and sum up the cases for each day
daily_data = df.groupby('date').sum().reset_index()
print(daily_data.head())

# Calculate daily new cases
daily_data['new_cases'] = daily_data['confirmed'].diff().fillna(0)

# Calculate daily new deaths
daily_data['new_deaths'] = daily_data['deaths'].diff().fillna(0)

# Calculate daily new recoveries
daily_data['new_recoveries'] = daily_data['recovered'].diff().fillna(0)

# Convert to numpy arrays for numerical operations
new_cases = daily_data['new_cases'].to_numpy()
new_deaths = daily_data['new_deaths'].to_numpy()
new_recoveries = daily_data['new_recoveries'].to_numpy()

# Calculate some statistics
mean_new_cases = np.mean(new_cases)
median_new_cases = np.median(new_cases)
variance_new_cases = np.var(new_cases)

print(f'Mean new cases: {mean_new_cases}')
print(f'Median new cases: {median_new_cases}')
print(f'Variance of new cases: {variance_new_cases}')

# Plot the spread of the virus over time
plt.figure(figsize=(14, 7))

plt.plot(daily_data['date'], daily_data['confirmed'], label='Confirmed Cases', color='blue')
plt.plot(daily_data['date'], daily_data['deaths'], label='Deaths', color='red')
plt.plot(daily_data['date'], daily_data['recovered'], label='Recovered', color='green')

plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('COVID-19 Spread Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot daily new cases
plt.figure(figsize=(14, 7))

plt.bar(daily_data['date'], daily_data['new_cases'], label='New Cases', color='orange')

plt.xlabel('Date')
plt.ylabel('Number of New Cases')
plt.title('Daily New COVID-19 Cases')
plt.legend()
plt.grid(True)
plt.show()

# Plot daily new deaths and recoveries
plt.figure(figsize=(14, 7))

plt.bar(daily_data['date'], daily_data['new_deaths'], label='New Deaths', color='black')
plt.bar(daily_data['date'], daily_data['new_recoveries'], label='New Recoveries', color='purple')

plt.xlabel('Date')
plt.ylabel('Number of New Deaths/Recoveries')
plt.title('Daily New Deaths and Recoveries')
plt.legend()
plt.grid(True)
plt.show()
