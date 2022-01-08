import pandas as pd
import matplotlib.pyplot as plt

# ---- # Note: none of these bar-charts make any logical sense. This script is just for learning Pandas and Matplotlip.

df_1 = pd.DataFrame({'anugs': [1, 1, 45, 444, 555, 666, 4],
                   'hootsman': [7, 7, 456, 765, 123, 765, 10],
                   'zargotrhax': [12, 12, 13, 10, 98, 49, 15],
                   'undead_unicorn_army': ['Atraxa', 'Brandished Heart', 'Bonfire of the Damned', None, 'Krenko, Mobb Boss', 'Gonti', 'Mizzix']})

df = pd.DataFrame({'anugs': [1, 1, 3, 4, 1, 1, 4],
                   'hootsman': [7, 7, 9, 10, 8, 8, 10],
                   'zargotrhax': [12, 12, 13, 15, 13, 13, 15],
                   'legendary_jetpack': ['gloryhammer', 'unicorn_army', 'terror_vortex', 'not_none', 'goblin_king', 'goblin_king', 'au']})
df = df.sort_values('anugs')
df = df.reset_index(drop=True)
# print(df)

# ---- # Uncomment for bar plot
# sth = range(len(df['legendary_jetpack']))
# plt.bar(sth, df['hootsman'], data=df)
# plt.xticks(sth, labels=df['legendary_jetpack'])
# plt.show()

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
        df.at[i, 'legendary_jetpack'] = f'{df.loc[i][3]}, {df.loc[i-1][3]}'
        df = df.drop(labels=i-1, axis=0)
# print(df)

# ---- # Uncomment for bar plot
# sth = range(len(df['legendary_jetpack']))
# plt.bar(sth, df['hootsman'], data=df)
# plt.xticks(sth, labels=df['legendary_jetpack'])
# plt.show()

df = df.set_index(['anugs', 'hootsman', 'zargotrhax'])
df_1 = df_1.set_index(['anugs', 'hootsman', 'zargotrhax'])

inner_joined_df = df.join(df_1, on=['anugs', 'hootsman', 'zargotrhax'], how='inner')
left_joined_df = df.join(df_1, on=['anugs', 'hootsman', 'zargotrhax'], how='left')
# print(inner_joined_df)
print(left_joined_df)

list_hootsman = [x[1] for x in left_joined_df.index]
x_ax = range(len(left_joined_df['legendary_jetpack']))
print(left_joined_df['legendary_jetpack'])
plt.bar(x_ax, list_hootsman)
plt.xticks(x_ax, labels=left_joined_df['legendary_jetpack'])
plt.show()
