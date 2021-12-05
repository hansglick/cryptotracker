# Applications

Il y a deux applications qui se chaînent afin de récupérer les commits d'un projet de crypto monnaie.

***

### STEP 1

L'application `get_commits_ids.py` permet dans un premier temps de récupérer toutes les urls des IDs des derniers commits

```
python get_commits_ids.py -ga solana-labs -gr solana -o 1638394946 > commits_ids.txt
```
 * *ga* : le github account
 * *gr* : le github repo
 * *o* : timestamp unix epoch, on récupère toutes les urls des commits dont la date est supérieure à o



### STEP 2

L'application `get_commits_data.py` permet de récupérer les informations relatives aux commits recherchés

```
python get_commits_data.py -f commits_ids.txt > commits_data.json
```
 * *f* : filename qui contient les urls des nouveaux commits