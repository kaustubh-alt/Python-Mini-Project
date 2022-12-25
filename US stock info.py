#https://www.alphavantage.co/support/#api-key
#go to aboove link for free api key
#you need an api key for access to US stock 


from alpha_vantage.timeseries import TimeSeries #you also need to install package 'ALPHAVANTAGE' to run this code
import pandas as pd
APIkey = #Enter your API key here
ts = TimeSeries(key=APIkey, output_format='pandas')
data, meta_data = ts.get_intraday('GOOGL')
print(data)
