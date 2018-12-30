import pandas as pd
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from IPython import display
import random
df = pd.DataFrame({'id':[1,2,3,4,5,6],'raw_grade':['a','b','c','d','e','f']})

# convertimos  raw_grade a categorical type
print('-----------------------df')
print(df)
df['grade']=df['raw_grade'].astype('category')
print('-----------------------df[grade]')
print(df['grade'])

# rename category

df['grade'].cat.categories=['exelente','super bien','very bien', 'bien', 'muy mal','pesimo']
print('----------------------- new category df[grade]')
print(df['grade'])

#df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print('----------------------- set category df[grade]')
print(df['grade'])

# sorting by column
df_sorting=df.sort_values(by='grade')
print('----------------------- df_sorting ')
print(df_sorting)

# grouping  by column (and count by type)
df_grouping_size=df.groupby('grade').size()
print('----------------------- df_grouping_size ')
print(df_grouping_size)

