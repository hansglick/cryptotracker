# Loadding libs
from datetime import datetime
from bs4 import BeautifulSoup
import requests as r
import json
import re
import os, sys
import time
import argparse

def Read_Commits_Ids_File(filename):
    
    urls = []
    with open(filename) as file:
        for line in file:
            urls.append(line.rstrip())
    
    return urls

def Extract_One_Commit_Data(url):
    
    response = r.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    
    # Recherche du timestamp
    selector = "#repo-content-pjax-container .flex-wrap"
    data = soup.select(selector)
    data = data[0]
    timestamp = data.find("relative-time")
    timestamp = timestamp.attrs["datetime"]
    date_obj = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    unix_epoch = (date_obj - datetime(1970, 1, 1)).total_seconds()
    unix_epoch = int(unix_epoch)
    
    # Recherche du contributor
    contributor = data.find("a").attrs["href"]
    contributor = contributor[1:]

    # Recherche des modifications
    selector = ".toc-diff-stats"
    data = soup.select(selector)
    data = data[0]
    files_changed = data.find("button")

    if files_changed is None:
        modifications = [item.text for item in data.find_all("strong")]
        n_files_changed,additions,deletions = [re.findall("[0-9,]+",item) for item in modifications]
        n_files_changed = int(n_files_changed[0].replace(",",""))
        additions = int(additions[0].replace(",",""))
        deletions = int(deletions[0].replace(",",""))
    else:
        files_changed = files_changed.text
        files_changed = files_changed.strip()
        n_files_changed = re.findall("[0-9,]+",files_changed)
        n_files_changed = int(n_files_changed[0].replace(",",""))
        modifications = data.find_all("strong")
        modifications = [item.text for item in modifications]
        additions,deletions = [re.findall('[0-9,]+', item) for item in modifications]
        additions = int(additions[0].replace(",",""))
        deletions = int(deletions[0].replace(",",""))
    
    # REecherche du commit id
    repo_name,project_name,_,commit_id = url[len("https://github.com/"):].split("/")
    
    # Concatenation des informations
    commit_data = {"id":commit_id,
                   "ts":unix_epoch,
                   "repo" : repo_name,
                   "project":project_name,
                   "contributor":contributor,
                   "additions":additions,
                   "deletions":deletions,
                   "files":n_files_changed,
                   "status":"OK"
                  }
    
    return commit_data


def final(args):
	
	urls = Read_Commits_Ids_File(args.filename)
	print("[")
	for idx,url in enumerate(urls):
		res = Extract_One_Commit_Data(url)
		print(json.dumps(res, indent=4, sort_keys=True))
		if (idx+1)!=len(urls):
			print(",")
	print("]")



	return None


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='test arguments')
	parser.add_argument("-f", "--filename",required = True)
	args = parser.parse_args()
	final(args)


# python get_commits_data.py -f commits_ids.txt >> commits_data.json