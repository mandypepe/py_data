import pandas as pd
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from IPython import display
import random
rng =pd.date_range('1/1/2018',periods=100,freq='S')
print('-------------------------')
print(rng)

ts=pd.Series(np.random.randint(0,500,len(rng)),index=rng)

print('-------------------------ts')
print(ts)

res=ts.resample('1Min').sum()
print('-------------------------res')
print(res)


rng =pd.date_range('1/1/2018 00:00',periods=5,freq='D')
ts=pd.Series(np.random.randn(len(rng)),rng)
print('-------------------------ts')
print(ts)

ts_utc=ts.tz_localize('UTC')
print('-------------------------ts_utc')
print(ts_utc)

ts_utc_to_US_est =ts_utc.tz_convert('US/Eastern')
print('-------------------------ts_utc_to_US_est')
print(ts_utc_to_US_est)


rng = pd.date_range('1/1/2012', periods=5, freq='M')

print('-------------------------rng')
print(rng)
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print('-------------------------ts')
print(ts)

peri=ts.to_period()

print('-------------------------peri')
print(peri)

peri_to_timestamp=peri.to_timestamp()
print('-------------------------peri_to_timestamp')
print(peri_to_timestamp)

prngq = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
print('-------------------------prngq')
print(prngq)
ts = pd.Series(np.random.randn(len(prngq)), prngq)
print('-------------------------ts')
print(ts)

ts.index = (prngq.asfreq('M', 'e') + 1).asfreq('H', 's') + 9

print('-------------------------ts.index')
print(ts.index)