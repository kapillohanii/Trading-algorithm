#https://kite.trade/docs/pykiteconnect/v3/

# https://www.youtube.com/watch?v=wHLrMyzdgJw


from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import pdb
from pandas.io.json import json_normalize


api_k = "rhrwdzsi4bkww0i3"  # api_key
api_s = "o5rkkde0m8396tyxiwgwbermqql9dng6"  # api_secret
access_token = "s1jEQwqS28z21VxVME6LA2xudVET9BER"

def get_login(api_k, api_s):
    global kws, kite
    kite = KiteConnect(api_key=api_k)

    # print("[*] Generate Request Token : ", kite.login_url())
    # request_tkn = input("[*] Enter Your Request Token Here : ")
    # data = kite.generate_session(request_tkn, api_secret=api_s)
    # kite.set_access_token(data["access_token"])
    # kws = KiteTicker(api_k, data["access_token"])
    # print(data['access_token'])


    kite.set_access_token(access_token)
    kws = KiteTicker(api_k, access_token)


    return kite

kite = get_login(api_k, api_s)

