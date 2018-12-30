import pandas as pd
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from IPython import display
import random

s=pd.Series(np.random.randint(0,7, size=10))
print(s.value_counts())
stri=pd.Series(['A','B','aba','BANCA',np.nan,'CUBA','dog'])
print(stri.str.lower())

df= pd.DataFrame(np.random.randn(14, 6))
print("------------------")
print(df)
partes=[df[:3],df[3:7],df[7:]]

print('-------- df[:3]')
print(df[:3])

print('-------- df[3:7]')
print(df[3:7])

print('-------- df[7:]')
print(df[7:])
print("------------------")
print (partes)
pd.concat(partes)
print("------------------partes concatenadas")
print (partes)


left= pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
rigth= pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

print("------------------ left")
print (left)

print("------------------derecha")
print (rigth)

print("------------------derecha izq concatenadas por una columna ")
print (pd.merge(left,rigth,on='key'))

otherletf=pd.DataFrame({'key':['foo','bar'],'laval':[2,4]})
otherright=pd.DataFrame({'key':['foo','bar'],'laval':[3,5]})
print("------------------otraderecha")
print (otherletf)
print("------------------otraderecha")
print (otherright)

print('----------------- otra derecha otra izq mescladas')
print(pd.merge(otherright,otherletf, on='key'))


df3=pd.DataFrame(np.random.randn(8,6),columns=['A','B','C','D','E','F'])
print('----------------- df3')
print(df3)
#asigno laas 3ra  row de todas las columnas
S=df3.iloc[3]

print('----------------- S')
print(S)
#adiciono  S ignorando los index
df3.append(S,ignore_index=True)
print('----------------- df3 adicionandoles S adiciona un row mas')
print(df3)

