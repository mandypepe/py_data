import pandas as pd
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from IPython import display
import random

df=pd.DataFrame({'A':['foo','barr','foo','bar','foo','barr','foo','bar'],
                 'B':['one','one','two','three','one','one','two','three'],
                 'C': np.random.randn(8),
                 'D':np.random.randn(8)
                 })
print ('----------------df ')
print(df)
#agrupando por A
print ('----------------gruping a  and sum all colums')
print (df.groupby('A').sum())

#grouping by many colunms
print ('----------------gruping a, b and sum all colums')
print (df.groupby(['B','A']).sum())
