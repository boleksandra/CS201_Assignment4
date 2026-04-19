import pandas as pd
import numpy as np
df = pd.read_csv('random_walk.csv')

# print(df.head())

df['distance'] = (df['x']**2 + df['y']**2)**0.5
# print("Координати та відстані для кожного кроку:")
# print(df[['x', 'y', 'distance']])
max_dist = df['distance'].max()
mean_dist = df['distance'].mean()

print(f"максимальна відстань: {max_dist}")
print(f"середня відстань: {mean_dist}")
print("\nточки з відстанню більшою за середню:")
print(df[df['distance'] > mean_dist])
