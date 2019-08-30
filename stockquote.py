import requests 
import json
import datetime
import pandas as pd
from ta import *

def init():
	XUEQIU_URL = "https://xueqiu.com/"
	headers = {"User-Agent": "Mozilla/5.0"}
	res = requests.get(XUEQIU_URL, headers=headers)
	cookie_str = str(res.headers["Set-Cookie"])
	headers["Cookie"] = cookie_str
	return headers

def stock_quote(headers, ins_name):
	XUEQIU_URL = "https://stock.xueqiu.com"
	QUOTE_URL = XUEQIU_URL + "/v5/stock/chart/minute.json?symbol=%s&period=1d"
	res = requests.get(QUOTE_URL % ins_name, headers=headers)
	tick_arr = json.loads(res.text)["data"]["items"]
	return tick_arr

def conv_timestamp(ts):
	return datetime.datetime.fromtimestamp(ts/1000)

def my_strategy(current, bb_high, bb_low, rsi):

	return

headers = init()
tick_arr = stock_quote(headers, "02318")
df = pd.DataFrame.from_records(tick_arr)
df["timestamp"] = df["timestamp"].apply(conv_timestamp)
df = df.drop(columns=["capital", "kdj", "ratio", "volume_compare"])
print (df)

df['bb_high'] = bollinger_hband(df["current"], n=20, ndev=2)
df['bb_low'] = bollinger_lband(df["current"], n=20, ndev=2)
df['rsi'] = rsi(df["current"], n=14)

print (df)
