import zrd_login
import pdb
import pickle
import datetime

kite = zrd_login.kite


def read_todays_doji_values():
	date = datetime.datetime.now().date().strftime("%d %B")
	filename = date + 'doji.pickle'
	file = open (filename, "rb")
	doji_data = pickle.load(file)

	return doji_data

doji_data = read_todays_doji_values()

def find_all_tradable_names(doji_data):	
	watchlist = []
	for name in doji_data:
		zrd_name = 'NSE:' + name
		watchlist.append(zrd_name)

	return watchlist

watchlist = find_all_tradable_names(doji_data)



bought_scripts = [] 
sold_scripts = []


while True:

	bigdata = kite.ltp(watchlist)


	for name in bigdata:
		only_name = name.replace('NSE:' , '')

		high = doji_data[only_name]['high']
		low = doji_data[only_name]['low']
		ltp = bigdata[name]['last_price']


		if (ltp > high) and (name not in bought_scripts):
			print("buy", name)
			bought_scripts.append(name)


		if (ltp < low) and (name not in  sold_scripts):
			print("sell", name)
			sold_scripts.append(name)
