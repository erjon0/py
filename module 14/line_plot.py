from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')

df.columns = df.columns.str.strip().str.lower()

avg_iq_by_continent = df.groupby('continent')['average iq'].mean()

plt.figure(figsize=(10, 6))
avg_iq_by_continent.plot(kind='line', marker='o', color='skyblue')

plt.title('Average IQ by Continent')
plt.xlabel('Continent')
plt.ylabel('Average IQ')

plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.show()
