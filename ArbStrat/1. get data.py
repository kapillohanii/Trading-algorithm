import zrd_login
import pdb
import pickle
import datetime

kite = zrd_login.kite


def init():
	global watchlist
	watchlist = ["SUNPHARMA","MARICO","LUPIN","BEL","TORNTPHARM","MINDTREE","APOLLOHOSP","MUTHOOTFIN","CIPLA","WIPRO","ITC","GLENMARK","TATACONSUM","JUSTDIAL","ULTRACEMCO","BATAINDIA","TORNTPOWER","CADILAHC","RELIANCE","TECHM","AMBUJACEM","ADANIPORTS","DRREDDY","ZEEL","AMARAJABAT","BOSCHLTD","GODREJCP","MANAPPURAM","BRITANNIA","BAJAJ-AUTO","DABUR","SHREECEM","TATAPOWER","MGL","BHARATFORG","RECLTD","UJJIVAN","VOLTAS","SIEMENS","COLPAL","BERGEPAINT","ASIANPAINT","CONCOR","GMRINFRA","NMDC","LT","HINDPETRO","GRASIM","MRF","HAVELLS","NTPC","IGL","ESCORTS","SRF","AUROPHARMA","DIVISLAB","MFSL","CUMMINSIND","INFRATEL","EXIDEIND","UPL","BHARTIARTL","INDIGO","TATACHEM","APOLLOTYRE","COALINDIA","PIDILITIND","IOC","NATIONALUM","SBILIFE","GAIL","RAMCOCEM","PAGEIND","TITAN","HINDUNILVR","INFY","DLF","PFC","BIOCON","PNB","JINDALSTEL","SRTRANSFIN","SUNTV","CENTURYTEX","HEROMOTOCO","HDFCBANK","ONGC","BALKRISIND","TVSMOTOR","ICICIPRULI","ACC","PETRONET","NESTLEIND","TCS","MOTHERSUMI","GODREJPROP","BHEL","VEDL","HDFCLIFE","AXISBANK","MARUTI","NIITTECH","NAUKRI","SAIL","ICICIBANK","KOTAKBANK","CANBK","ASHOKLEY","LICHSGFIN","MCDOWELL-N","IDFCFIRSTB","NCC","JUBLFOOD","L&TFH","BAJAJFINSV","HDFC","PEL","BPCL","POWERGRID","HINDALCO","TATAMOTORS","SBIN","BANKBARODA","TATASTEEL","IBULHSGFIN","ADANIENT","M&M","EQUITAS","INDUSINDBK","FEDERALBNK","JSWSTEEL","BAJFINANCE","RBLBANK","HCLTECH","CHOLAFIN","PVR","BANDHANBNK","IDEA","M&MFIN","UBL","EICHERMOT"]

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



			

		print(f"{name}, {opp_pct}")




