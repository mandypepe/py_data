import pandas as pd
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from IPython import display
import random

tuple = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                   ['one', 'two', 'one', 'two''one', 'two', 'one', 'two']
                   ]))
#crea pares por posiciones de cada lista
print('tuple----------------------------')
print(tuple)
print('index----------------------------')
index=pd.MultiIndex.from_tuples(tuple, names=['primero', 'segundo'])
print(index)

df=pd.DataFrame(np.random.randn(7, 2), index=index, columns=['A','B'])
print('new df----------------------------')
df2=df[:4]
print(df2)
staked=df2.stack()
#  compress levels en el dataframe
print('staked----------------------------')
print(staked)
# unestack

unestaked=staked.unstack()
print('unestaked----------------------------')
print(unestaked)

unestaked=staked.unstack(0)
print('unestaked(0)----------------------------')
print(unestaked)
unestaked=staked.unstack(1)
print('unestaked(1)----------------------------')
print(unestaked)

