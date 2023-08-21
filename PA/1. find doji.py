import zrd_login
import pdb
import pickle
import datetime

kite = zrd_login.kite


def init():
	global watchlist
	watchlist = ["COALINDIA","TITAN","BAJFINANCE","TATAMOTORS","IOC","M&M","ICICIBANK","TATASTEEL","SHREECEM","JSWSTEEL","CIPLA","HINDUNILVR","NTPC","BAJAJ-AUTO","GRASIM","BAJAJFINSV","HEROMOTOCO","SBIN","ASIANPAINT","HDFC","BHARTIARTL","EICHERMOT","ULTRACEMCO","MARUTI","ADANIPORTS","UPL","SUNPHARMA","KOTAKBANK","INDUSINDBK","VEDL","LT","POWERGRID","ITC","AXISBANK","TECHM","ZEEL","WIPRO","HCLTECH","INFY","DRREDDY","TCS","NESTLEIND","BRITANNIA","HINDALCO"]

init()

def doji_finder(ohlc, ltp):	
	openx = ohlc['open']
	close = ohlc['close']
	high = ohlc['high']
	low = ohlc['low']
	doji_or_not = (openx - ltp) <= (high - low)*0.1

	return doji_or_not


doji_list = {}




for name in watchlist:

	zrd_name = "NSE:" + name
	data = kite.quote(zrd_name)
	ohlc = data[zrd_name]['ohlc']
	ltp = data[zrd_name]['last_price']

	doji_or_not = doji_finder(ohlc, ltp)

	if doji_or_not == True:
		doji_list[name] = {'high' : ohlc['high'], 'low': ohlc['low']}

		# print(name, doji_or_not)



print(doji_list)


date = datetime.datetime.now().date().strftime("%d %B")
filename = date + 'doji.pickle'


with open(filename, 'wb') as doji_file:
   pickle.dump(doji_list, doji_file)








