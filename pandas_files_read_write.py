import pandas as pd
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from IPython import display
import random

df = pd.DataFrame(np.random.randn(1000, 4),columns=['A', 'B', 'C', 'D'])
print(df)
#escribo
df.to_csv('foo.csv')
# leo
pd.read_csv('foo.csv')
#Writing to a HDF5 Store.
df.to_hdf('foo.h5','df')
# leo
pd.read_hdf('foo.h5','df')

# xls
df.to_excel('foo.xlsx', sheet_name='Hoja1')
#Leo

pd.read_excel('foo.xlsx', 'Hoja1', index_col=None, na_values=['NA'])
