import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Pokemon.csv')
df2 = df[df['type1'] != 'Blastoise']
type1_total = df2[['type1', 'total']]
type1_mean_total = type1_total.groupby('type1').mean()

plt.figure(figsize=(12, 6))
plt.scatter(type1_mean_total.index, type1_mean_total['total'])
plt.title('Mean Total by Type 1 (excluding 0th category)')
plt.xlabel('Type 1')
plt.ylabel('Mean Total')
plt.xticks(rotation=45) 
plt.grid(True)
plt.show()
