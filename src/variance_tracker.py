import pandas as pd 

df = pd.read_csv('data/honolulu_fy26_bfs.csv')

# how far the spending was from the budget. Actual - Budget
df['Variance'] = df['actual'] - df['budget']

# same variance but expressed as a percentage of the budget. (Actual - Budget) / Budget * 100
df['Variance_pct'] = (df['actual'] - df['budget']) / df['budget'] * 100

# This is the threshold for the variance significance. If the variance percentage is greater than this threshold, it will be considered significant.
Threshold_pct = 10
df['Variance_signficant'] = df['Variance_pct'].abs() > Threshold_pct

flagged_df = df[df['Variance_signficant']]
flagged_df = flagged_df.sort_values('Variance', key = abs, ascending = False)
print(flagged_df)
print(df)
