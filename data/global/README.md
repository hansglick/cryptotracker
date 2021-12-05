# Applications 

Les applications de ce repo permettent de récupérer des données globales des crypto currencies existantes

### STEP1 - Get Top Cryptos

Permet de récupérer les meilleurs crypto selon le site cryptorankings :
 * *-p* : le nombre de pages à visiter
 * *-f* : nom du json dans lequel stocker les informations des top cryptos
```
python get_top_cryptos.py -p 2 -f crypto.json
```


### STEP2 - Get Crypto's Meta Data

Permet de récupérer des données pour les top cryptos, en particulier les urls du livre banc, du compte twitter, du compte reddit, etc. Le fichier `-f` sera enrichi par les meta data récupérées

```
python get_metadata_cryptos.py -f crypto.json
```

### STEP3 - Get Crypto's Prices

Permet de récupérer le cours de chacune des crypto présents dans le fichier `-g`. Elle crée un `stocks.json` dont le nom comprend la date du run

```
python get_price_cryptos.py -g crypto.json -s stocks.json
```