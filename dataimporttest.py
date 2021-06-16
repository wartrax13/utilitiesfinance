#Importando dados da bolsa de valores

import numpy as np
import pandas as pd

ser = pd.Series(np.random.random(5), name = 'Column 01')
print(ser)

from pandas_datareader import data as wb

PG = wb.DataReader('PG', data_source='yahoo', start ='1995-1-1')
print(PG)

#PG.info()
#PG.head(20)
#PG.tail(20)

tickers = ['PG', 'MSFT', 'T', 'F', 'GE']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

print(new_data.tail())