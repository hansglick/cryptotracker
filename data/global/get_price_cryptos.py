from datetime import datetime
from bs4 import BeautifulSoup
import requests as r
import json
import re
import os, sys
import time
import argparse
import cryptocompare

def Save_Dic_To_Json(filename,dic_obj):
    with open(filename, 'w') as outfile:
        json.dump(dic_obj, outfile, indent = 4)
    return None


def Get_Crypto_Current_Price(crypto_dic,verbose=False):
    
    X = []
    now = datetime.now(tz=None)
    now = int(now.timestamp())
    
    for key,val in crypto_dic.items():
        code = val["code"]
        code = code.upper()
        if verbose:
            print(code)
        try:
            price = cryptocompare.get_price(code,currency='EUR')[code]["EUR"]
            if verbose:
                print("")
        except:
            
            if verbose:
                print("PROBLEM NO CURRENCY")
            continue
        
        X.append({"code":code,"ts":now,"price":price,"currency":"EUR"})
        time.sleep(1)
    
    return X


def Get_Suffix_Date():
    now = datetime.now(tz=None)
    year = str(now.year).zfill(4)
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    suffix = year + month + day + hour + minute
    return suffix


def final(args):
    with open(args.crypto_global_filename) as json_file:
        crypto_dic = json.load(json_file)
    current_crypto_prices = Get_Crypto_Current_Price(crypto_dic,verbose=True)
    suffix = Get_Suffix_Date()
    savedfilename = args.crypto_stocks_filename.split(".")[0] + "_" + suffix + ".json"
    Save_Dic_To_Json(savedfilename,current_crypto_prices)
    return None



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='test arguments')
    parser.add_argument("-g", "--crypto_global_filename",required = True)
    parser.add_argument("-s", "--crypto_stocks_filename",required = True)
    args = parser.parse_args()
    final(args)


# python get_price_cryptos.py -g crypto.json -s stocks.json