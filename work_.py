import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
df[df['distance'] > mean_dist].to_json('filtered_walk.json', orient='records', indent=4)


plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y'], label='траєкторія', color='#FF69B4', alpha=0.7, linewidth=2)
plt.scatter(0,0, color='#9400D3', marker='o', label='початок (0,0)')
plt.scatter(df['x'].iloc[-1], df['y'].iloc[-1], color='#800000', marker='X', label='кінець')
plt.xlabel('вісь абсцис')
plt.ylabel('Вісь ординат')
plt.title('шлях до точки відхилення')
plt.grid(True)
plt.legend()
plt.show()
