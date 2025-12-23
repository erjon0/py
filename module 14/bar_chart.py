import pandas as pd

import matplot as plt

df=pd.read_csv('avgIQpercountry.csv')

filtered_df=df[df['iq']>=100]

filtered_df=filtered_df.sort_values(by='iq',ascending=False)

print(filtered_df)

plt.figure(figsize=(14,8))

bars=plt.bar(filtered_df['average iq by contry (iq>=100)'],fontsize=16)

plt.xlabel('contry',fontsize=14)
plt.xlabel('average iq',fontsize=14)

plt.xticks(rotation=90,fontsize=0.8)
plt.xticks(fontsize=10)

plt.grid(axis='y',linestyle='--',alpha=0.8)

plt.bar_label(bars,fmt='%.2f',fontsize=10,color='black')
plt.tight.