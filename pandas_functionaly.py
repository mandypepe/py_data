import pandas as pd
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from IPython import display
import random

index=pd.date_range('1/1/2018', periods=8)
s=pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
df=pd.DataFrame(np.random.randn(8,3),index=index,columns=['A','B',"C"])
wp=pd.Panel(np.random.randn(2,5,4),
            items=['ITEM1','TEM2'],
            major_axis=pd.date_range('1/1/2018',
            periods=5),minor_axis=['A','B','C','D'])

long_series = pd.Series(np.random.randn(1000))
print('-------- HEAD')
print(long_series.head())

print('-------- TAIl')
print(long_series.tail())

# seleciono 2 primeras filas
dfcorto=df[:2]

df.columns=[x.lower() for x in df.columns]
df2=df.copy()
print('---- df lower columas')
print(df)

# get values
print('----- S.values')
print(s.values)

print('----- df.values')
print(df.values)

print('----- wp.values')
print(wp.values)


#### SUB
major_mean = wp.mean(axis='major')
print(wp.sub(major_mean, axis='major'))

## divmod
s=pd.Series(np.arange(10))
# modulo de la divicion
div, rem = divmod(s, 3)

# comparaciones
#comparison methods eq, ne, lt, gt, le, and ge

compara=df.gt(df2)
df2=df2*4
print('----- compara')
print(compara)

compara2=df.lt(df2)
df2=df2*4
print('----- compara2')
print(compara2)

#reductions Boolean Reductions
bolean_df=(df > 0).all()
print('----- bolean_df ')
print(bolean_df)

bolean_any_df=(df > 0).any()
print('----- bolean_any_df ')
print(bolean_any_df)

#bolean_bool_df=df.bool()
print('----- bolean_bool_df ')
#print(bolean_bool_df)

empty_df=df.empty
print('----- empty_df ')
print(empty_df)

df_empty=pd.DataFrame(columns=list('ABC')).empty
print('----- df_empty ')
print(df_empty)


# comparacion de objetos
print('---- obj comparations ')
print(df+df == df*2)
# importana nan values are diferent
print('---- obj comparations.all() ')
print((df+df == df*2).all())

# importana nan values are diferent
print('---- NaN comparations  ')
print(np.nan ==np.nan)

# con el metodo equals si los asume iguALES
print('equals method on comparation')
print((df+df).equals(df*2))

# diferent por indixes
df1 = pd.DataFrame({'col': ['foo', 0, np.nan]})
df2 = pd.DataFrame({'col':[np.nan, 0, 'foo']}, index=[2,1,0])

# indices diferentes orden
print('-----df1')
print(df1)
print('-------df2')
print(df2)
#print
print('-------initial comparation')
print(df1.equals(df2))
# reordering index
print('-------reordering comparation')
print(df1.equals(df2.sort_index()))


# comparing series whit valores
valores=pd.Series(['foo','bars','zoo'])
print('----------------- scalar value comparations')
print(valores=='foo')

indexes=pd.Index(['food','bar','bici'])
print('----------------- scalar value comparations in indexes')
print(indexes=='foo')

# comparar objetos de la misma longitud
# diferentes longitudes daria error
print('obj same length index vs series')
print(pd.Series(['foo', 'bar', 'baz']) == pd.Index(['foo', 'bar', 'qux']))

print('obj same length array vs series')
print(pd.Series(['foo', 'bar', 'baz']) == np.array(['foo', 'bar', 'qux']))


# numpy es diferente
print('obj diferent length array vs array')
print (np.array([1, 2, 3]) == np.array([2]))
# retorna falso si la comparacion no puede ser effectiva
print('obj diferent length array vs array')
print(np.array([1, 2, 3]) == np.array([1, 2]))


##### combinando y sobreponiendo data frame
df1 = pd.DataFrame({'A' : [1., np.nan, 3., 5., np.nan],
                    'B' : [np.nan, 2., 3., np.nan, 6.]})
df2 = pd.DataFrame({'A' : [5., 2., 4., np.nan, 3., 7.],
                    'B' : [np.nan, np.nan, 3., 4., 6., 8.]})
combination=df1.combine_first(df2)

print('function conbine_firts')
print(combination)

## operaciones All such methods have a skipna
##
# count	    Number of non-NA observations
# sum	    Sum of values
# mean	    Mean of values
# mad	    Mean absolute deviation
# median	Arithmetic median of values
# min	    Minimum
# max	    Maximum
# mode	    Mode
# abs	    Absolute Value
# prod	    Product of values
# std	    Bessel-corrected sample standard deviation
# var	    Unbiased variance
# sem	    Standard error of the mean
# skew	    Sample skewness (3rd moment)
# kurt	    Sample kurtosis (4th moment)
# quantile	Sample quantile (value at %)
# cumsum	Cumulative sum
# cumprod	Cumulative product
# cummax	Cumulative maximum
# cummin	Cumulative minimum
#
# cumsum() and cumprod() preserve the location of NaN values.
#
#  some NumPy methods, like mean, std, and sum, will exclude NAs
# ##

df.mean(0)
df.mean(1)
df.sum(0, skipna=False) # skip NaN
df.sum(axis=1, skipna=True)
ts_stand = (df - df.mean()) / df.std()
ts_stand.std()
xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)
xs_stand.std(1)

series = pd.Series(np.random.randn(5))

s1 = pd.Series(np.random.randn(5))
frame = pd.DataFrame(np.random.randn(5,3), columns=['A','B','C'])
# describe
seleccionando =series.describe(percentiles=[.05, .25, .75, .95])
 # mixed type describe selecciona las columnas numericas
# solo OBJ
#frame.describe(include=['object'])
# solo Numeros
frame.describe(include=['number'])
# todos
frame.describe(include='all')
# maximo y minimo vaor series y DF
s1.idxmin()
s1.idxmax()
df1.idxmin(axis=0)
df1.idxmax(axis=1)
# conteo de valores , retorna valores y su cantidad
data = np.random.randint(0, 7, size=50)
s.value_counts()
pd.value_counts(data)
# mode () es mas o menos la misma opcion de counts
s1.mode()
frame.mode()






