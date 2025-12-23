import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')
df.columns = df.columns.str.strip().str.lower()

plt.figure(figsize=(10, 6))

plt.scatter(df.index, df['average iq'], color='purple', alpha=0.7)

plt.title('Average IQ by Country Index')
plt.xlabel('Country Index')
plt.ylabel('Average IQ')

plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
