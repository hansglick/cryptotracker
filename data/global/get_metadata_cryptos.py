from datetime import datetime
from bs4 import BeautifulSoup
import requests as r
import json
import re
import os, sys
import time
import argparse

def Save_Dic_To_Json(filename,dic_obj):
	with open(filename, 'w') as outfile:
		json.dump(dic_obj, outfile)
	return None


def final(args):
	
	# 0. Read JSON Crypto
	with open(args.filename) as json_file:
		crypto_dic = json.load(json_file)
	
	# Browse JSON and Grab Data
	for key,val in crypto_dic.items():

		# Control
		time.sleep(2)
		print(key,val["url"]["coinmarket"])
		try:
			response = r.get(val["url"]["coinmarket"])
			soup = BeautifulSoup(response.text,"html.parser")
		except:
			continue

		# Grab Data
		selector = ".eMxKgr"
		data = soup.select(selector)
		if len(data)==0:
			print("PROBLEM URL NOT REACHED!!")
			continue
		print("")
		t = data[1]
		t = t.find_all("a",href=True)
		links = [(item.text,item.attrs["href"]) for item in t]

		# Rearrange Data
		d = {}
		for label,url in links:
			if "blanc" in label:
				d["livre_blanc"] = url
			if "t.me/" in url:
				d["telegram"] = url
			if "discord" in url:
				d["discord"] = url
			if "medium" in label:
				d["medium"] = url
			if "twitter" in url:
				d["twitter"] = url
			if "reddit" in url:
				d["reddit"] = url
			if "github" in url:
				d["github"] = url
		crypto_dic[key]["links"] = d
	
	# Save JSON
	Save_Dic_To_Json(args.filename,crypto_dic)
	
	return None



if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='test arguments')
	parser.add_argument("-f", "--filename",required = True)
	args = parser.parse_args()
	final(args)


# python get_metadata_cryptos.py -f crypto.json