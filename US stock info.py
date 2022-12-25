#https://www.alphavantage.co/support/#api-key
#go to aboove link for free api key
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
APIkey = #Enter your API key here
ts = TimeSeries(key=APIkey, output_format='pandas')
data, meta_data = ts.get_intraday('GOOGL')
print(data)
