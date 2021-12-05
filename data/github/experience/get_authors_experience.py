# Loadding libs
from datetime import datetime
from bs4 import BeautifulSoup
import requests as r
import json
import re
import os, sys
import time
import argparse

def Grab_Dates_Urls(author):
    
    url = "https://github.com" + "/" + author
    response = r.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    selector = ".small"
    data = soup.select(selector)
    dates_elements = data[0]
    dates_elements = dates_elements.find_all("li")
    dates_urls = ["https://github.com" + item.find("a")["href"] for item in dates_elements]
    
    return dates_urls

def Grab_One_Year_Contribution(url):
    
    response = r.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    selector = ".js-yearly-contributions .mb-2"
    data = soup.select(selector)
    data = data[0]
    x = data.text
    n_contributions = x.split()[0]
    year = x.split()[-1]
    n_contributions = n_contributions.replace(",","")
    n_contributions = int(n_contributions)
    
    return (year,n_contributions)

def Grab_Author_Contributions(author):

    RES = []
    urls = Grab_Dates_Urls(author)
    for url in urls:
        year,n_contributions = Grab_One_Year_Contribution(url)
        RES.append({"author":author,"year":int(year),"contributions":n_contributions})

    return RES


def Read_Authors_File(filename):
    
    urls = []
    with open(filename) as file:
        for line in file:
            urls.append(line.rstrip())
    
    return urls



def final(args):

	authors = Read_Authors_File(args.filename)
	print("[")

	for idx_author,author in enumerate(authors):
		experience = Grab_Author_Contributions(author)
		for idx_year,item in enumerate(experience):
		    print(json.dumps(item, indent=4, sort_keys=True))
		    if (idx_year+1) == len(experience):
		        x = 1 + 1
		    else:
		        print(",")

	print("]")

	return None


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='test arguments')
	parser.add_argument("-f", "--filename",required = True)
	args = parser.parse_args()
	final(args)


# python get_authors_experience.py -f contributors.txt