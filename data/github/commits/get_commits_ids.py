from datetime import datetime
from bs4 import BeautifulSoup
import requests as r
import json
import re
import os, sys
import time
import argparse


# python get_commits_ids -ga solana-labs -gr solana -o 1638394946

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

def Get_Scrapped_Commits_Page(url):

    selector = "#repo-content-pjax-container .f6"
    response = r.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    data = soup.select(selector)
    
    return data


def Rearrange_Scrapped_Commits_Page(data):
    c = 0
    COUPLE = []
    COMMITS = []
    for item in data:
        COUPLE.append(item)
        c = c + 1
        if c%2==0:
            c = 0
            COMMITS.append(COUPLE)
            COUPLE = []
    return COMMITS

def Extract_Dates_And_Commits_Ids(BIG,older_than):
    COMMITS_INFO = []
    for data_date,data_url in BIG:
        rawts = data_date.find('relative-time').attrs["datetime"]
        date_obj = datetime.strptime(rawts, "%Y-%m-%dT%H:%M:%SZ")
        unix_epoch = (date_obj - datetime(1970, 1, 1)).total_seconds()
        unix_epoch = int(unix_epoch)
        relative_url = data_url.attrs["href"]
        COMMITS_INFO.append((unix_epoch,relative_url))
        if unix_epoch <= older_than:
            break
    return COMMITS_INFO

def Extract_Relevant_Commits_List(github_account,github_repo,older_than):
    
    url = "https://github.com/" + github_account + "/" + github_repo + "/commits/master"
    results = []
    next_page = True

    while next_page:
        scrapped_commits_page = Get_Scrapped_Commits_Page(url)
        scrapped_commits_page_list = Rearrange_Scrapped_Commits_Page(scrapped_commits_page)
        scrapped_dates_and_ids_commits = Extract_Dates_And_Commits_Ids(scrapped_commits_page_list,older_than)
        results = results + scrapped_dates_and_ids_commits
        next_page = len(scrapped_dates_and_ids_commits) == len(scrapped_commits_page_list)
        first_commit_id = os.path.basename(scrapped_dates_and_ids_commits[0][-1])
        n_others_commits = str(int(len(scrapped_commits_page_list) - 1))
        urla = "https://github.com/" + github_account + "/" + github_repo + "/commits/master?after="
        urlb = first_commit_id + "+" + n_others_commits + "&branch=master"
        url = urla + urlb

    solutions = ["https://github.com" + item[1] for item in results]


    return solutions



def final(args):
	solutions = Extract_Relevant_Commits_List(args.github_account,args.github_repo,args.older_than)
	for item in solutions:
		print(item)
	return None


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='test arguments')
	parser.add_argument("-ga", "--github_account",required = True)
	parser.add_argument("-gr", "--github_repo", required = True)
	parser.add_argument("-o", "--older_than",type=int,required = True)
	args = parser.parse_args()
	final(args)




# python get_commits_ids.py -ga solana-labs -gr solana -o 1638394946