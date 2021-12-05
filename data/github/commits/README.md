# Applications

Il y a deux applications qui se chaînent afin de récupérer les commits d'un projet de crypto monnaie. On récupère d'abord les IDs des derniers commits (relativement à un timestamp unix renseigné) associé à un repo GitHub. Puis on récupère les méta données des commits dont on vient de récupérer l'id.


### Utilisation
```
# STEP 1 - permet dans un premier temps de récupérer toutes les urls des IDs des derniers commits
python get_commits_ids.py -ga solana-labs -gr solana -o 1638394946 > commits_ids.txt

# STEP 2 - permet de récupérer les informations relatives aux commits recherchés
python get_commits_data.py -f commits_ids.txt > commits_data.json
```
 * *ga* : le github account
 * *gr* : le github repo
 * *o* : timestamp unix epoch, on récupère toutes les urls des commits dont la date est supérieure à o
 * *f* : filename qui contient les urls des nouveaux commits

### Output

```
[
{
    "additions": 3,
    "contributor": "CriesofCarrots",
    "deletions": 3,
    "files": 1,
    "id": "3e5a5a834f2b1e1e80e65ec0e196c9db6cfbb2fa",
    "project": "solana",
    "repo": "solana-labs",
    "status": "OK",
    "ts": 1638654703
}
,
{
    "additions": 6,
    "contributor": "lijunwangs",
    "deletions": 1,
    "files": 1,
    "id": "f4ca87205f04e8e2cb0f9c13e52ea26fe782b20e",
    "project": "solana",
    "repo": "solana-labs",
    "status": "OK",
    "ts": 1638650848
}
,
...
```