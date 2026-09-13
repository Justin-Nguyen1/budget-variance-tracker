import pandas as pd 

df = pd.read_csv('data/honolulu_fy26_bfs.csv')

# how far the spending was from the budget. Actual - Budget
df['Variance'] = df['Actual'] - df['Budget']

# same variance but expressed as a percentage of the budget. (Actual - Budget) / Budget * 100
df['Variance_pct'] = (df['Actual'] - df['Budget']) / df['Budget'] * 100

print(df)
