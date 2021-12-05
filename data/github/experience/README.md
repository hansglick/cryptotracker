# Application

L'application `get_authors_experience.py` permet de récupérer l'expérience des contributeurs de GitHub, i.e. le nombre de commits effectués chaque année.

### Utilisation

```
python get_authors_experience.py -f contributors.txt > contributors_experience.json
```

 * *f* : filename qui contient la liste des contributeurs pour lesquels on souhaite récupérer l'expérience sur GitHub


```
[
{
    "author": "chevdor",
    "contributions": 1480,
    "year": 2021
}
,
{
    "author": "chevdor",
    "contributions": 188,
    "year": 2020
}
,
{
    "author": "chevdor",
    "contributions": 64,
    "year": 2019
}
,
...
```