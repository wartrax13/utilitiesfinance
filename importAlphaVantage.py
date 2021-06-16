import numpy as np
import pandas as pd
from pandas_datareader import data as wb

#DADOS ALPHA VANTAGE
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key = 'DICBS2BQRGFUUR7I', output_format='pandas')
PG_av, metadata = ts.get_daily_adjusted('PG', outputsize='full')
#print(PG_av)

#DADOS DA APPLE
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key = 'DICBS2BQRGFUUR7I', output_format='pandas')
AAPL_av, metadata = ts.get_daily_adjusted('AAPL', outputsize='full')
#print(AAPL_av)

#CONCATENADO
pfolio_av = pd.concat([PG_av['5. adjusted close'], AAPL_av['5. adjusted close']], axis = 1)
#(pfolio_av)

#LISTA
pfolio_av.columns = ['PG', 'AAPL']
print(pfolio_av)