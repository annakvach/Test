import pandas as pd


# to import txt file
df = pd.read_csv('BigData/LLP_Genomed_Ayr_OVNG50V02_20230213_FinalReport.txt',
                 sep='\t',
                 header=0,
                 skiprows=list(range(9)))

# # look at the data str
# print(df.info())
#
# for i in list(df.columns):
#     print(str(i),  "\t", df[i].unique(), "\t", df[i].nunique())

# combine 'Allele1 - AB', 'Allele2 - AB'
target_cols = ['Allele1 - AB', 'Allele2 - AB']
df['combined'] = df[target_cols].apply(lambda row: '/'.join(row.values.astype(str)), axis=1)
print(df.head())

# leave only useful columns
df1 = df[["SNP Name","Sample ID", "combined"]]

# unmelt df1
df_unmelted = df1.pivot(index='Sample ID', columns='SNP Name', values='combined')

# temp to del
print(df_unmelted.head(n=23))
print(df_unmelted.info())
df2 = df_unmelted.iloc[:, 0:4]
df2.to_csv("BigData/Temp_04.csv")

# save data as json
df_unmelted.to_json(path_or_buf="BigData/Result_Table.json")



















