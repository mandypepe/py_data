import pandas as pd
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from IPython import display
import random


###### JOIN
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

frames = [df1, df2, df3]

print('---------------frames')
print(frames)
concatenados = pd.concat(frames)
# pd.concat(objs,
# axis=0,
# join='outer',
# join_axes=None,
# ignore_index=False,
# keys=None,
# levels=None,
# names=None,
# verify_integrity=False,
# copy=True)
##
#
#
print('--------------- concatenados')
print(concatenados)
result = pd.concat(frames, keys=['x', 'y', 'z'])
print('-------------------------------  result')
print(result)
onlyYkeys = result.loc['y']
print('-------------------------------  onlyYkeys')
print(onlyYkeys)

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])
union4=pd.concat([df1,df4],axis=1,sort=False)
print('-------------------------------  union4')
print(union4)

joininner = pd.concat([df1, df4], axis=1, join='inner')
print('-------------------------------  joininner')
print(joininner)

joindf1index = pd.concat([df1, df4], axis=1, join_axes=[df1.index])

print('-------------------------------  joindf1index')
print(joindf1index)

# append
df1appenddf2=df1.append(df2)
print('-------------------------------  df1appenddf2')
print(df1appenddf2)

df1appenddf4=df1.append(df4)
print('-------------------------------  df1appenddf4')
print(df1appenddf4)

df1appenddf2df3=df1.append([df2, df3])
print('-------------------------------  df1appenddf2df3')
print(df1appenddf2df3)

# concat  ingnore index
concatignorinindex =pd.concat([df1, df4], ignore_index=True)
print('-------------------------------  concatignorinindex')
print(concatignorinindex)

# append  ingnore index
appendignorinindex =df1.append(df4, ignore_index=True)
print('-------------------------------  appendignorinindex')
print(appendignorinindex)

# concatenando series y dataframe

s1 = pd.Series(['X0', 'X1', 'X2', 'X3'], name='X')

series_dataframe_concat=pd.concat([df1,s1],axis=1)
print('-------------------------------  series_dataframe_concat')
print(series_dataframe_concat)

s2 = pd.Series(['_0', '_1', '_2', '_3'])

series_dataframe_concat2 = pd.concat([df1, s2, s2, s2], axis=1)

print('-------------------------------  series_dataframe_concat2')
print(series_dataframe_concat2)

series_dataframe_concat_ignore_index = pd.concat([df1, s1], axis=1, ignore_index=True)
print('-------------------------------  series_dataframe_concat_ignore_index')
print(series_dataframe_concat_ignore_index)


s3 = pd.Series([0, 1, 2, 3], name='foo')
s4 = pd.Series([0, 1, 2, 3])
s5 = pd.Series([0, 1, 4, 5])
concat_index_set=pd.concat([s3, s4, s5], axis=1, keys=['red','blue','yellow'])

print('-------------------------------  concat_index_set')
print(concat_index_set)

print('-------------------------------  result.index.levels')
print(result.index.levels)

# appendind rows
s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])
appending_rows = df1.append(s2, ignore_index=True)

print('-------------------------------  appending_rows')
print(appending_rows)

# appending dics
dicts = [{'A': 1, 'B': 2, 'C': 3, 'X': 4},
         {'A': 5, 'B': 6, 'C': 7, 'Y': 8}]

appendin_dics=df1.append(dicts, ignore_index=True)
print('-------------------------------  appendin_dics')
print(appendin_dics)

######## MERGING

###
# pd.merge(
# left,
# right,
# how='inner',
# on=None,
# left_on=None,
# right_on=None,
#          left_index=False,
#          right_index=False,
#          sort=True,
#          suffixes=('_x', '_y'),
#          copy=True,
#          indicator=False,
#          validate=None)


##
# left	    LEFT OUTER JOIN	    Use keys from left frame only
# right	    RIGHT OUTER JOIN	Use keys from right frame only
# outer	    FULL OUTER JOIN	    Use union of keys from both frames
# inner	    INNER JOIN	        Use intersection of keys from both frames
#
# ####

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

result = pd.merge(left, right, on='key')
print('-------------------------------  result')
print(result)


left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                   'key2': ['K0', 'K1', 'K0', 'K1'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

result_k1_k2 = pd.merge(left, right, on=['key1', 'key2'])

print('-------------------------------  result_k1_k2')
print(result_k1_k2)

result_how_left = pd.merge(left, right, how='left', on=['key1', 'key2'])
print('-------------------------------  result_how_left')

print(result_how_left)

result_how_right = pd.merge(left, right, how='right', on=['key1', 'key2'])

print('-------------------------------  result_how_right')
print(result_how_right)

result_how_outer = pd.merge(left, right, how='outer', on=['key1', 'key2'])
print('-------------------------------  result_how_outer')
print(result_how_outer)

result_how_inner = pd.merge(left, right, how='inner', on=['key1', 'key2'])
print('-------------------------------  result_how_inner')
print(result_how_inner)

left = pd.DataFrame({'A' : [1,2], 'B' : [1, 2]})

right = pd.DataFrame({'A' : [4,5,6], 'B': [2, 2, 2]})
#result = pd.merge(left, right, on='B', how='outer', validate="one_to_one")
result_validate_one_to_many = pd.merge(left, right, on='B', how='outer', validate="one_to_many")
print('-------------------------------  result_validate_one_to_many')
print(result_validate_one_to_many)

#merge() accepts the argument indicator
##
# Merge key only in 'left' frame	    left_only
# Merge key only in 'right' frame	    right_only
# Merge key in both frames	            both
# #

df1 = pd.DataFrame({'col1': [0, 1], 'col_left':['a', 'b']})

df2 = pd.DataFrame({'col1': [1, 2, 2],'col_right':[2, 2, 2]})

indicator =pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print('-------------------------------  indicator')
print(indicator)

# name a la columna indicador
indicator_con_string=pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print('-------------------------------  indicator_con_string ')
print(indicator_con_string)
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                   'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])


right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                     'D': ['D0', 'D2', 'D3']},
                       index=['K0', 'K2', 'K3'])

result = left.join(right)

result_how_outer = left.join(right, how='outer')
print('-------------------------------  result_how_outer ')
print(result_how_outer)

result_how_inner = left.join(right, how='inner')
print('-------------------------------  result_how_inner ')
print(result_how_inner)
how
resul_right_index_left_index = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print('-------------------------------  resul_right_index_left_index_how ')
print(resul_right_index_left_index)

resul_right_index_left_index_how_inner = pd.merge(left, right, left_index=True, right_index=True, how='inner')
