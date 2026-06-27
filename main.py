import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
df.columns = df.columns.str.strip()

# Show first 5 rows
print("First 5 rows:")
print(df.head())
print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)
print("\nMissing values:")
print(df.isnull().sum())

plt.figure(figsize=(12,6))

sns.barplot(
    x='Region',
    y='Estimated Unemployment Rate (%)',
    data=df
)

plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")
plt.show()

# Convert Date column to proper date format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

plt.figure(figsize=(12,6))

sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=df
)

plt.title("Unemployment Rate Over Time")
plt.xticks(rotation=45)
plt.show()
top_states = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

top_states = top_states.sort_values(ascending=False).head(5)

print("\nTop 5 States with Highest Unemployment:")
print(top_states)