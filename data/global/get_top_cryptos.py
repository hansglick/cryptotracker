# Loadding libs
from datetime import datetime
from bs4 import BeautifulSoup
import requests as r
import json
import re
import os, sys
import time
import argparse


class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


def Get_Tops_Crypto(n_pages):

    d = AutoVivification()
    urls_pages = ["https://coinranking.com/" + "?page=" + str(pageid) for pageid in list(range(1,n_pages+1))]

    for url in urls_pages:

        print(url)
        response = r.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        selector = ".profile__link"
        data = soup.select(selector)
        urls = ["https://coinranking.com" + item.attrs["href"] for item in data]
        names = [item.text.strip() for item in data]
        codes = [item.split("-",1)[1] for item in urls]
        splitted_words = [x.split(" ") for x in names]
        splitted_words = [[item.lower() for item in words if item[0]!="("] for words in splitted_words]
        url_suffix = ["-".join(words) for words in splitted_words]
        urls2 = ["https://coinmarketcap.com/fr/currencies/" + item for item in url_suffix]

        for n,c,u1,u2 in zip(names,codes,urls,urls2):
            d[n] = {"code":c,"url":{"coinranking":u1,"coinmarket":u2}}

        time.sleep(2)

    return d


def Save_Dic_To_Json(filename,dic_obj):
    with open(filename, 'w') as outfile:
        json.dump(dic_obj, outfile)
    print("file saved : " + filename)
    return None



def final(args):
	crypto_dic = Get_Tops_Crypto(args.n_pages)
	Save_Dic_To_Json(args.filename,crypto_dic)	
	return None

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='test arguments')
	parser.add_argument("-p", "--n_pages",type=int,required = True)
	parser.add_argument("-f", "--filename",required = True)
	args = parser.parse_args()
	final(args)


# python get_top_cryptos.py -p 2 -f crypto.json