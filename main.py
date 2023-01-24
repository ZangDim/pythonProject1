import pandas as pd
import numpy as np
df = pd.read_csv('export_database_FA.csv')

mp = df.groupby(['zip_code', 'bottles_sold','item_description'])
df['Percentage_sales'] = (df['sale_dollars'] / df['sale_dollars'].sum())*100
ps = df.groupby(['store_name','Percentage_sales'])

print(mp.first())
print(ps.first())

#REPORT : As recommended in Github. The visualization was made via Tableau!


















