from secret import Secret
import requests
import pandas as pd 
from pprint import pprint

headers = {
    'Content-Type': 'application/json'
}

ticker = 'EURUSD'
requestResponse = requests.get("https://api.tiingo.com/tiingo/fx/prices?tickers={}&startDate=2022-01-02&resampleFreq=5min&token={}".format(ticker, Secret.api_key), 
                                headers=headers)
# print(requestResponse.json())
# pprint(requestResponse.headers)
# pprint(requestResponse.json())
data = requestResponse.json()
# pprint(data[0[:3])
# print(type(data[0]))

df = pd.DataFrame.from_dict(data)
# print(df)    
df.to_csv('{}.csv'.format(ticker))
# df = pd.read_json(requestResponse.json())
# print(df.head())
