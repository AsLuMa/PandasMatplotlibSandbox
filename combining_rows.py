import pandas as pd

df = pd.DataFrame({'anugs': [1, 1, 3, 4, 1, 1, 4],
                   'hootsman': [7, 7, 9, 10, 8, 8, 10],
                   'zargotrhax': [12, 12, 13, 15, 13, 13, 15],
                   'legendary_jetpack': ['gloryhammer', 'unicorn_army', 'terror_vortex', None, 'goblin_king', 'goblin_king', 'au']})
df = df.sort_values('anugs')
df = df.reset_index(drop=True)
print(df)

# 1 compares previous row, -1 next row
df_pnr_shf = df['anugs'].shift(1)
df_lg_shf = df['hootsman'].shift(1)
df_dag_shf = df['zargotrhax'].shift(1)

# MUST sort the values by index before running this
# fetches index by previous row when .shift(1)
# iterrows() returns i = index value and row = series of values
# TODO remove duplicates
for i, row in df.iterrows():
    if (df_pnr_shf[i] == row[0]) & (df_lg_shf[i] == row[1]) & (df_dag_shf[i] == row[2]):
        # df.loc[i] = {'pasnr': 11, 'legenr': 11, 'dag': 11, 'dgkode': 'bajs'}
        df.at[i, 'legendary_jetpack'] = f'{df.loc[i][3]}, {df.loc[i-1][3]}'
        df = df.drop(labels=i-1, axis=0)
print(df)

