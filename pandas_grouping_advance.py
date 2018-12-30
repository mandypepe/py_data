import pandas as pd
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from IPython import display
import random

## AGREGATE  GROPING
# mean()	    Compute mean of groups
# sum()	        Compute sum of group values
# size()	    Compute group sizes
# count()	    Compute count of group
# std()	        Standard deviation of groups
# var()	        Compute variance of groups
# sem()	        Standard error of the mean of groups
# describe()	Generates descriptive statistics
# first()	    Compute first of group values
# last()	    Compute last of group values
# nth()	        Take nth value, or a subset if n is a list
# min()	        Compute min of group values
# max()	        Compute max of group values
# ###

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print('------df ')
print(df)

# agrupando por columnas

grouped = df.groupby('A'
                     )
print('---------------------- gruped'
      )
print(grouped.head())
groupedAB = df.groupby(['A', 'B'])
print('----------------------  groupedAB ')
print(groupedAB)


def get_letter_type(letter):
    if letter.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'

gruped_functions=df.groupby(get_letter_type,axis=1)
print('------------------------ gruped_functions')
print(gruped_functions)

lst = [1, 2, 3, 1, 2, 3,1]
s = pd.Series([1, 2, 3, 10, 20, 30,np.nan], lst)
print('-------------------- S'
      )
print(s)
grouped = s.groupby(level=0)
print('---------------------- group ped firts')
print(grouped.first())

print('---------------------- group ped last')
print(grouped.last())

print('---------------------- group ped last')
print(grouped.sum())

# gruped sorting
df2 = pd.DataFrame({'X' : ['B', 'B', 'A', 'A'], 'Y' : [1, 2, 3, 4]})
print('--------df2')
print(df2)
groupby_X_sum =df2.groupby(['X']).sum()
print('---------------------- groupby_X_sum')
print(groupby_X_sum)

groupby_X_sum_sort_false= df2.groupby(['X'], sort=False).sum()
print('---------------------- groupby_X_sum_sort_false')
print(groupby_X_sum_sort_false)

df3 = pd.DataFrame({'X' : ['A', 'B', 'A', 'B'], 'Y' : [1, 4, 3, 2]})
print('---------------------- df3')
print(df3)
getA_groupbyX=df3.groupby(['X']).get_group('A')
print('---------------------- getA_groupbyX')
print(getA_groupbyX)
getB_groupbyX=df3.groupby(['X']).get_group('B')
print('---------------------- getB_groupbyX')
print(getB_groupbyX)

#grouping obj
obj_groups=df.groupby('A').groups
print('---------------------- obj_groups')
print(obj_groups)

group_get_function=df.groupby(get_letter_type, axis=1).groups
print('---------------------- group_get_function')
print(group_get_function)

grouped_groups=df.groupby(['A','B'])

print('------------------- grouped_groups')
print(grouped_groups.groups)
long=len(grouped_groups)
print('------------------- long')
print(long)


gb=df.groupby('A')
##
# gb.agg        gb.boxplot    gb.cummin     gb.describe   gb.filter     gb.get_group  gb.height     gb.last       gb.median     gb.ngroups    gb.plot       gb.rank       gb.std        gb.transform
# gb.aggregate  gb.count      gb.cumprod    gb.dtype      gb.first      gb.groups     gb.hist       gb.max        gb.min        gb.nth        gb.prod       gb.resample   gb.sum        gb.var
# gb.apply      gb.cummax     gb.cumsum     gb.fillna     gb.gender     gb.head       gb.indices    gb.mean       gb.name       gb.ohlc       gb.quantile   gb.size       gb.tail       gb.weight
# #

# GroupBy with MultiIndex
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
s = pd.Series(np.random.randn(8), index=index)
print('---------------- multiple index')
print(s)

gropuedmultiple_level0=grouped = s.groupby(level=0)
print('---------------- gropuedmultiple . sum')
print(gropuedmultiple_level0.sum())
gropued_level_second =s.groupby(level='second').sum()
print('------------ gropued_level_second ')
print(gropued_level_second)

sums=s.sum(level='second')
print('------------ sums ')
print(sums)

groupin_multiplex=s.groupby(level=['first', 'second']).sum()
# new s.groupby(['first', 'second']).sum() NO LEVELS
print('------------ groupin_multiplex ')
print(groupin_multiplex)

#Grouping DataFrame with Index Levels and Columns
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
df = pd.DataFrame({'A': [1, 1, 1, 1, 2, 2, 3, 3],
                'B': np.arange(8)},
                 index=index)
group_index_columns= df.groupby([pd.Grouper(level=1), 'A']).sum()
print('------------ group_index_columns ')
print(group_index_columns)
#Index levels may also be specified by name.
group_index_columns_name=df.groupby([pd.Grouper(level='second'), 'A']).sum()

print('------------ group_index_columns_name ')
print(group_index_columns_name)
#Index level names may be specified as keys directly
group_index_columns_directo=df.groupby(['second', 'A']).sum()

print('------------ group_index_columns_directo ')
print(group_index_columns_directo)

#DataFrame column selection in GroupBy
grouped = df.groupby(['A'])
print('------------ grouped ')
print(grouped)
#grouped_C = grouped['C']
print('------------ grouped_C ')
#print(grouped_C)
#grouped_D = grouped['D']
print('------------ grouped_D ')
#print(grouped_D)
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
# Iterating through groups
grouped = df.groupby('A')
for name, group in grouped:
    print('----------- name')
    print(name)
    print('----------- group')
    print(group)
# grouping by multiple keys,
for name, group in df.groupby(['A', 'B']):
    print('----------- name multiple')
    print(name)
    print('----------- group multiple ')
    print(group)
# Selecting a group
# group can be selected using get_group():
bar_=grouped.get_group('bar')
print('----------- group bar_ ')
print(bar_)
gropued_multiple=df.groupby(['A', 'B']).get_group(('bar', 'one'))
print('----------- gropued_multiple')
print(gropued_multiple )

#Aggregation
grouped2 = df.groupby('A')
agregado=grouped2.aggregate(np.sum)
print('--- agregado')
print(agregado)

grouped3 = df.groupby(['A', 'B'])
agregado3=grouped3.aggregate(np.sum)
print('--- agregado3')
print(agregado3)

grouped_index_False = df.groupby(['A', 'B'], as_index=False)
agregado_grouped_index_False=grouped_index_False.aggregate(np.sum)
print('--- agregado_grouped_index_False')
print(agregado_grouped_index_False)

gruped_index_false_sum=df.groupby('A', as_index=False).sum()
print('--- gruped_index_false_sum')
print(gruped_index_false_sum)
RESete_index_false_sum=df.groupby(['A', 'B']).sum().reset_index()
print('--- RESete_index_false_sum')
print(RESete_index_false_sum)

print('-----------------gruped size')
print(grouped.size())

print('-----------------gruped describe')
print(grouped.describe())
## apling fuctions



grouped_byA = df.groupby('A')
print('----------------- grouped by A')
print(grouped_byA.head())
sub_gruped_byA_byC =grouped_byA['C'].agg([np.sum, np.mean, np.std])
print('----------------- multiples funciones a la ves sub_gruped_byA_byC ')
print(sub_gruped_byA_byC)

# a un agrupado se le pueden pasar muchas funciones a cada una de sus columnas

all_colums_multiple_functions_ongroup=grouped_byA.agg([np.sum, np.mean, np.std])
print('----------------- all_colums_multiple_functions_ongroup ')
print(all_colums_multiple_functions_ongroup)

# RENOMBRAR LOS NOMBRES DE LAS COLUMNAS  SOBRE LAS FUNCIONES APLICADAS

RENAME_colums_multiple_functions_ongroup=grouped_byA.agg([np.sum, np.mean, np.std]).rename(columns={'sum': 'sumando',
'mean': 'mediando',
'std': 'stand'})

print('----------------- RENAME_colums_multiple_functions_ongroup ')
print(RENAME_colums_multiple_functions_ongroup)

#Applying different functions to DataFrame columns

diferent_function_diferent_colums=grouped_byA.agg({'C': np.sum, 'D' : lambda x: np.std(x, ddof=1)})
print('----------------- diferent_function_diferent_colums ')
print(diferent_function_diferent_colums)
#The function names can also be strings
#grouped.agg({'C' : 'sum', 'D' : 'std'})

#optimization

sum_all_rows=df.groupby('A').sum()
print('----------------- sum_all_rows ')
print(sum_all_rows)
media_dos_columnas=df.groupby(['A', 'B']).mean()
print('----------------- media_dos_columnas ')
print(media_dos_columnas)

# trans formacion
index = pd.date_range('10/1/2017', periods=1100)

print('----------------- index ')
print(index)

ts = pd.Series(np.random.normal(0.5, 2, 1100), index)

print('----------------- ts ')
print(ts)

tss = ts.rolling(window=100,min_periods=100).mean().dropna()

print('----------------- tss ')
print(tss)

key=lambda x: x.year
zscore = lambda x: (x - x.mean()) / x.std()
transformed = ts.groupby(key).transform(zscore)

print('----------------- transformed ')
print(transformed)

groupedkey = ts.groupby(key)
print('----------------- groupedkey mean ')
print(groupedkey.mean())

print('----------------- groupedkey std ')
print(groupedkey.std())

grouped_trans = transformed.groupby(key)

print('----------------- grouped_trans std ')
print(grouped_trans.std())

print('----------------- grouped_trans mean ')
print(grouped_trans.mean())


data_range = lambda x: x.max() - x.min()
# transforming_lamnda=ts.groupby(key).transform('max') - ts.groupby(key).transform('min')
# las dos opciones son el mismo resultado

transforming_lamnda=ts.groupby(key).transform(data_range)

print('----------------- transforming_lamnda ')
print(transforming_lamnda)

data_df = pd.DataFrame({'A': np.random.randn(1000),
                        'B': np.random.randn(1000),
                        'C': np.random.randn(1000)})
print('----------------- data_df ')
print(data_df)

countries = np.array(['US', 'UK', 'GR', 'JP'])
print('----------------- countries ')
print(countries)
key = countries[np.random.randint(0, 4, 1000)]
print('----------------- key ')
print(key)
grouped = data_df.groupby(key)
print('----------------- grouped ')
print(grouped.head())

grupedcount=grouped.count()
print('----------------- grupedcount ')
print(grupedcount)

f = lambda x: x.fillna(x.mean())
transformed = grouped.transform(f)

print('----------------- transformed ')
print(transformed)

f_re = pd.DataFrame({'A': [1] * 10 + [5] * 10,
                     'B': np.arange(20)})

print('----------------- f_re ')
print(f_re)


df_r_rollin_by_media=f_re.groupby('A').rolling(2).B.mean()
print('----------------- df_r_rollin_by_media ')
print(df_r_rollin_by_media)

df_r_expanding_by_SUM=f_re.groupby('A').expanding().sum()
print('----------------- df_r_expanding_by_SUM ')
print(df_r_expanding_by_SUM)

sf = pd.Series([1, 1, 2, 3, 3, 3])
grpedsf=sf.groupby(sf)
print('----------------- grpedsf ')
print(grpedsf)
mayores_sum_que_2=sf.groupby(sf).filter(lambda x: x.sum()> 2)

print('----------------- mayores_sum_que_2 ')
print(mayores_sum_que_2)

dff = pd.DataFrame({'A': np.arange(8),
                    'B': list('aabbbbcc')})
print('----------------- dff ')
print(dff)
longitud_mayor_q_2=dff.groupby('B').filter(lambda x: len(x) > 2)

print('----------------- longitud_mayor_q_2 ')
print(longitud_mayor_q_2)

# retornar los objetos que no pasan el filtro con NANA
NAN_FILL=dff.groupby('B').filter(lambda x: len(x) > 2, dropna=False)

print('----------------- NAN_FILL ')
print(NAN_FILL)

dff['C'] = np.arange(8)
print('----------------- dff[C] ')
print(dff)
espesific_columns=dff.groupby('B').filter(lambda x: len(x['C']) > 2)

print('----------------- espesific_columns ')
print(espesific_columns)