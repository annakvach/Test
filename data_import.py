import pandas as pd


# import txt file
df = pd.read_csv('BigData/LLP_Genomed_Ayr_OVNG50V02_20230213_FinalReport.txt',
                 sep='\t',
                 header=0,
                 skiprows=list(range(9)))

# combine 'Allele1 - AB', 'Allele2 - AB'
target_cols = ['Allele1 - AB', 'Allele2 - AB']
df['combined'] = df[target_cols].apply(lambda row: '/'.join(row.values.astype(str)), axis=1)

# leave only useful columns
df1 = df[["SNP Name","Sample ID", "combined"]]

# unmelt df1 to get "SNP Name" as cols, "Sample ID" as rows
df_unmelted = df1.pivot(index='Sample ID', columns='SNP Name', values='combined')

# save data as json
df_unmelted.to_json(path_or_buf="BigData/Result_Table.json")

