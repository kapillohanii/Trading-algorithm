
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker

api_k = "twxmhe2qglswrwhm"  
api_s = "qntalzlw4df3iyzwy2i8d0fgxjxsamc4"  
access_token = "Oz9rUR7eo5psg2oTimIcS1hb3cXhRH29"


def get_login(api_k, api_s):
    global kws, kite
    kite = KiteConnect(api_key=api_k)
    kite.set_access_token(access_token)
    kws = KiteTicker(api_k, access_token)
    return kite

kite = get_login(api_k, api_s)

watchlistb =['RAMCOCEM','ICICIPRULI','COFORGE','ACC','GODREJCP','WIPRO','APOLLOHOSP']
pricelistb =[1047.15,453.25,3072.85,1925.05,736.45,433.15,3017]
tgtb=       [1060,457.25,3097,1942,743,438,3047]
slb=        [1040,450,3059,1918,733,430,3003]
qtyb=       [30,50,12,25,60,65,12]
i=0
j=[0,0,0,0,0,0,0] 
#here , put time constraint also, that trade should be after 9:20 only , and in last , put constraint that if time is 3:17 
watchlists = ['HDFCBANK','IOC','ICICIBANK','SBIN']
pricelists = [1430,89.8,563.1,348.5]
tgts=[1414,88.4,557,345]
sls=[1437,90.5,566,350.5]
qtys=[30,200,65,75]
l=0
k=[0,0,0,0]

while True:
  for name in watchlistb:
    data = kite.ltp("NSE:"+name)
    ltp = data['NSE:'+name]['last_price']
    print(ltp)
    if(ltp>=pricelistb[i]):
      if(j[i]==0):
        print("BOught",name,qtyb[i])
        kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol=name, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=qtyb[i], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET)
        j[i]=1

    if(ltp<=slb[i] and j[i]==1):
      kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol=name, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=qtyb[i], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET)
      j[i]=100      
    
    if((ltp>=tgtb[i]) and j[i]==1):
      kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol=name, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=qtyb[i], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET)
      j[i]=100
      print("achieved",name,qtyb[i])     
    i+=1
  i=0
  for game in watchlists:
    data = kite.ltp("NSE:"+game)
    ltp = data['NSE:'+game]['last_price']
    print(ltp)
    if(ltp<=pricelists[l]):
      if(k[l]==0):
        k[l]=1
        print("sold",game,qtys[l])
        kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol=game, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=qtys[l], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET)
        
    if(ltp>=sls[l] and k[l]==1):
      kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol=game, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=qtys[l], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET)
      k[l]=100
      print("sl",game,qtys[l])
    
    if((ltp<=tgts[l]) and k[l]==1):
      kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol=game, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=qtys[l], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET)      
      print("tgt",game,qtys[l])
      k[l]=100
    l+=1
  l=0