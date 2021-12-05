from bs4 import BeautifulSoup
import requests as r
import pandas as pd
import json
import re
from datetime import datetime
import os
import time

def Retrieve_Last_Commits(url):
    selector = ".f6.BtnGroup-item"
    response = r.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    data = soup.select(selector)
    cells = [item.attrs for item in data]
    commits_links = ["https://github.com" + item["href"] for item in cells]
    return commits_links


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



def Grab_Commits_Links_From_URL_List(urls):
    L = []
    for url in urls:
        temp = Retrieve_Last_Commits(url)
        L = L + temp
    return L




def Retrieve_Commits_Data_From_List(L,seconds=1):

    X = []
    for url in L:
        try:
            res = Extract_One_Commit_Data(url)
        except:
            repo_name,project_name,_,commit_id = url[len("https://github.com/"):].split("/")
            res = {"id":commit_id,
                   "repo" : repo_name,
                   "project":project_name,
                   "status":"KO"}
        time.sleep(seconds)
        X.append(res)

    return X



def Write_Json_File(saved_filename,python_object):
    
    with open(saved_filename, 'w') as outfile:
        json.dump(python_object, outfile,indent=4)
    return None





def Grab_Dates_Urls(author):
    
    
    url = "https://github.com" + "/" + author
    response = r.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    # search years links
    selector = ".small"
    data = soup.select(selector)
    dates_elements = data[0]
    dates_elements = dates_elements.find_all("li")
    dates_urls = ["https://github.com" + item.find("a")["href"] for item in dates_elements]
    
    return dates_urls




def Grab_All_Author_Contributions(dates_urls,author):
    
    res = [Grab_One_Year_Contribution(url,author) for url in dates_urls]
    
    return res



def Grab_One_Year_Contribution(url,author):

    #print(url)
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
    
    return {"author":author,"year":year,"contributions":n_contributions}



def Grab_Author_Contributions(author):
    dates_urls = Grab_Dates_Urls(author)
    contributions = Grab_All_Author_Contributions(dates_urls,author)
    return contributions
