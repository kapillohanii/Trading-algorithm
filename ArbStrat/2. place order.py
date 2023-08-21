import zrd_login
import pdb
import pickle
import datetime

kite = zrd_login.kite


def init():
	global watchlist, traded_scripts
	watchlist = ["SUNPHARMA","MARICO","LUPIN","BEL","TORNTPHARM","MINDTREE","APOLLOHOSP","MUTHOOTFIN","CIPLA","WIPRO","ITC","GLENMARK","TATACONSUM","JUSTDIAL","ULTRACEMCO","BATAINDIA","TORNTPOWER","CADILAHC","RELIANCE","TECHM","AMBUJACEM","ADANIPORTS","DRREDDY","ZEEL","AMARAJABAT","BOSCHLTD","GODREJCP","MANAPPURAM","BRITANNIA","BAJAJ-AUTO","DABUR","SHREECEM","TATAPOWER","MGL","BHARATFORG","RECLTD","UJJIVAN","VOLTAS","SIEMENS","COLPAL","BERGEPAINT","ASIANPAINT","CONCOR","GMRINFRA","NMDC","LT","HINDPETRO","GRASIM","MRF","HAVELLS","NTPC","IGL","ESCORTS","SRF","AUROPHARMA","DIVISLAB","MFSL","CUMMINSIND","INFRATEL","EXIDEIND","UPL","BHARTIARTL","INDIGO","TATACHEM","APOLLOTYRE","COALINDIA","PIDILITIND","IOC","NATIONALUM","SBILIFE","GAIL","RAMCOCEM","PAGEIND","TITAN","HINDUNILVR","INFY","DLF","PFC","BIOCON","PNB","JINDALSTEL","SRTRANSFIN","SUNTV","CENTURYTEX","HEROMOTOCO","HDFCBANK","ONGC","BALKRISIND","TVSMOTOR","ICICIPRULI","ACC","PETRONET","NESTLEIND","TCS","MOTHERSUMI","GODREJPROP","BHEL","VEDL","HDFCLIFE","AXISBANK","MARUTI","NIITTECH","NAUKRI","SAIL","ICICIBANK","KOTAKBANK","CANBK","ASHOKLEY","LICHSGFIN","MCDOWELL-N","IDFCFIRSTB","NCC","JUBLFOOD","L&TFH","BAJAJFINSV","HDFC","PEL","BPCL","POWERGRID","HINDALCO","TATAMOTORS","SBIN","BANKBARODA","TATASTEEL","IBULHSGFIN","ADANIENT","M&M","EQUITAS","INDUSINDBK","FEDERALBNK","JSWSTEEL","BAJFINANCE","RBLBANK","HCLTECH","CHOLAFIN","PVR","BANDHANBNK","IDEA","M&MFIN","UBL","EICHERMOT"]
	traded_scripts = []

init()


nse_watchlist = ['NSE:' + name for name in watchlist]
bse_watchlist = ['BSE:' + name for name in watchlist]


while True:
	print()
	nse_data = kite.ltp(nse_watchlist)
	bse_data = kite.ltp(bse_watchlist)

	for name in watchlist:
		nse_name = 'NSE:' + name 
		bse_name = 'BSE:' + name 

		# pdb.set_trace()

		try:
			nse_ltp = nse_data[nse_name]['last_price']
			bse_ltp = bse_data[bse_name]['last_price']
			# pdb.set_trace()
			opp_pct = round((abs(nse_ltp - bse_ltp)/nse_ltp)*100, 1)

		except Exception as e:
			print(e)
			continue

		if opp_pct > 0.3:


			if (nse_ltp > bse_ltp) and (name not in traded_scripts):
				print("sell nse, buy bse")
				
				order_id = kite.place_order(tradingsymbol=name,exchange=kite.EXCHANGE_NSE,transaction_type=kite.TRANSACTION_TYPE_SELL,quantity=1,order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_NRML, variety = kite.VARIETY_REGULAR)
				order_id = kite.place_order(tradingsymbol=name,exchange=kite.EXCHANGE_BSE,transaction_type=kite.TRANSACTION_TYPE_BUY,quantity=1,order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_NRML, variety = kite.VARIETY_REGULAR)
				traded_scripts.append(name)


			if (bse_ltp > nse_ltp) and (name not in traded_scripts):
				print("sell bse, buy nse")


				order_id = kite.place_order(tradingsymbol=name,exchange=kite.EXCHANGE_BSE,transaction_type=kite.TRANSACTION_TYPE_SELL,quantity=1,order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_NRML, variety = kite.VARIETY_REGULAR)
				order_id = kite.place_order(tradingsymbol=name,exchange=kite.EXCHANGE_NSE,transaction_type=kite.TRANSACTION_TYPE_BUY,quantity=1,order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_NRML, variety = kite.VARIETY_REGULAR)
				traded_scripts.append(name)





	if (name in traded_scripts) and (opp_pct < 0.1):

			if (nse_ltp > bse_ltp) and (name not in traded_scripts):
				print("buy nse, sell bse")
				
				order_id = kite.place_order(tradingsymbol=name,exchange=kite.EXCHANGE_NSE,transaction_type=kite.TRANSACTION_TYPE_BUY,quantity=1,order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_NRML, variety = kite.VARIETY_REGULAR)
				order_id = kite.place_order(tradingsymbol=name,exchange=kite.EXCHANGE_BSE,transaction_type=kite.TRANSACTION_TYPE_SELL,quantity=1,order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_NRML, variety = kite.VARIETY_REGULAR)
				traded_scripts.append(name)


			if (bse_ltp > nse_ltp) and (name not in traded_scripts):
				print("buy bse, sell nse")


				order_id = kite.place_order(tradingsymbol=name,exchange=kite.EXCHANGE_BSE,transaction_type=kite.TRANSACTION_TYPE_BUY,quantity=1,order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_NRML, variety = kite.VARIETY_REGULAR)
				order_id = kite.place_order(tradingsymbol=name,exchange=kite.EXCHANGE_NSE,transaction_type=kite.TRANSACTION_TYPE_SELL,quantity=1,order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_NRML, variety = kite.VARIETY_REGULAR)
				traded_scripts.append(name)

	if time == 3:15:
		exit()