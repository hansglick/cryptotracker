# Reference

MOOC sur la DeFi : https://www.coursera.org/specializations/decentralized-finance-duke


# History of decentralized finance

### Le troc

 * Première technologie DeFi, aucune autorité de nécessaire
 * Très contraignant pour des raisons évidentes de matching
 * L’argent a résolu le problème du matching


### L’objectif de l’argent

 * Comparer deux produits différents
 * Résoudre le problème du matching du troque
 * Possibilité d’accumuler de la valeur dans le temps, on peut pas accumuler des denrées alimentaires très longtemps car elles périssent
 * Transférer cette valeur et déférer cette valeur


### Caractéristiques de l’argent

 * Durabilité : l’argent est dépensable longtemps dans le futur, un billet est dépensable de multiple fois par différentes personnes
 * Portabilité : tu peux le prendre avec toi, facilité d’utilisation. L’or n’est pas réellement portable par exemple
 * Divisibilité : tu peux représenter n’importe quelle fraction de ta valeur
 * Uniformité : une même version d’une monnaie a la même valeur dans le temps (1$ today vaut 1 $ demain)
 * Acceptabilité : l’argent permet de régler des dettes et d’acheter des biens que ce soit dans le privée ou dans le public. De par la loi on doit accepter le dollar
 * Stabilité : contrairement aux crypto, les gens cherchent des valeurs stables
 

### Histoire des techno financières

 * En 600 avant JC, on utilisait des pièces d’or (valeur tangible)
 * En 1290, la chine introduit les billets de banques (valeur intangible)
 * 1871, 1er transfert d’argent via un coupon Western Union
 * 1950, carte de crédit
 * 1967, premier distributeur de billet
 * 1983, premier transfert éléctronique
 * 1994, premier transfert via internet
 * 1997, premier paiement sans contact
 * 2005, première carte chip and pin (carte à puce)
 * 2008, programmable money (premier bitcoin)
 * 2014, Apple Pay (réduit la fraude drastiquement)
 * 2021, toute les banques ont des R&D projects autour de la block chain, elles ont compris qu’elles doivent absolument réduire les coûts car la DeFi va les baiser inévitablement si elles ne bougent pas


### Transfert d’argent

 * Le coût du premier transfert d’argent en 1871 était de 3%
 * Le coût d’un transfert par carte bleue en 2021 est également de 3%
 * Il y a une porte ouverte pour la DeFi, on n’a pas été capable de réduire ce coût


### Valeur intangible de l’argent

On se doit de distinguer entre valeur tangible et inangible
 * Histoire du dollar suisse irakien encore utilisé par les kurdes au nord alors qu’il était devenu illégal dans le reste de l’irak (intangible)
 * Les pierres de l’île de Yap (intangible)
 * Pièces d’or (tangible)

***

# Les problèmes de la Centralized Finance

### Causes

 * Contrôle centralisé : le système bancaire est très concentré, les banques nationales contrôlent la monnaie, de même que les GAFAM qui ont des monopoles énormes dans leurs domaines. Elles ont intérêt à developper leur propres crypto pour économiser de l’argent sur les fameux 3% de fees
 * Accès limité : une large partie de la population mondiale n’a pas de banques ~1.7 Md. 
 * Inefficace : 3% de fees lors de transactions à la carte de crédit, 5-7% pour un virement bancaire, 2 jours de délai pour une transaction de stocks, fraude, insécurité, impossibilité de micro transactions, les fees sont apparemment élever afin de subvenir aux problèmes de fraudes du système, 
 * Peu d’intéropérabilité : très difficile de transférer de l’argent entre deux institutions financières. Plaid est une BaaS
 * Opacité : les clients ne savent rien de la santé de leur banques, ils doivent faire confiance aux régulateurs et espérer que l’Etat vienne les sauver en cas de souci

### Conséquences

 * Opportunités de croissance ratés : notamment pr les petits entrepreneurs qui se prennent des taux d’intérêt énormes dans la gueule ce qui rend le projet non viable


### Dettes et solutions

La dette des états atteint des records historiques, ca peut devenir un problème. Les solutions :
 * Augmenter les impôts
 * Imprimer de l’argent (risque d’inflation, ce qui revient à un impôt)
 * Augmenter la croissance (entre 1 et 2% dans les pays développés)

Donc ils reparlent du fait que les fintech dédiés au transfert d’argent ne font qu’apporter du user friendly service car elles utilisent toujours les banques comme backbone

***

# Cryptomonnaies, le bitcoin

### Introduction

Le bitcoin né de la fusion de deux idées relativement anciennes :
 * La block chain
 * Le concept de proof of work. En gros c’est un concept introduit au début de l’ère internet afin d’éviter l’envoi des spams, il a été imaginé de produire un petit effort pour une unité d’emails mais qui serait coûteux pour une large quantité d’emails, l’idée étant que vu le coût, les spammers seraient contraints d’arrêter


### Dapps

Une Dapp permet aux utilisateurs d’intéragir directement entre eux en mode peer to peer, plus d’autorité au-dessus. DeFi est un marché concurrentiel de Dapps. Ils fonctionnent comme des apps normales mais ces apps ne sont pas hebergées sur un central serveur. Mais ce sont les peers du système qui l’héberge eux-mêmes. Les DAO (decentralized autonomous organization), c’est une organisation qui est un algorithme. Un peu comme le bitcoin, les employés sont mes mineurs mais il n’y a pas de patrons, pas de board directors. 


### Blockchain, les quelques idées

 * Inventé en 1991 par Haber and Stormetta
 * Une espece de grand tableur Excel dans lequel on ne peut qu’ajouter des lignes et ne pas modifier les précédentes (Immuable)
 * Un tableur excel donc consultable par tout le monde en accès libre
 * Un tableur excel qui serait dupliqué sur un grand nombre de nodes
 * Les données peuvent être de n’importe quel format possible (addition, transaction, programme informatique, etc.)
 * Les données sont empaquetées dans des grands blocks
 * Chaque block pointe vers le block précédent
 * Ce chaînage permet de s’assurer de la cohérence et de la non corruption des données via une méthode de cryptographie
 * La fin de chaque block est un hash qui représente toutes les transactions du bloc
 * Ce hash est une espèce d’empreinte qui symbolise toutes les transactions
 * Si on modifie ne serait-ce qu’une seule des transactions l’empreinte s’en retrouve modifiée
 * Le hash d’un block représente les transactions du block ET le figure print du block précédent (la première ligne)
 * Le chaînage s’opère de la manière suivante, la première ligne du block t correspond au hash du block t-1
 * Si une modification se produit sur une ligne d’un block alors la chaîne est rompue car l’empreinte ne correspondra plus à la première ligne du bloc suivant, le réseau entier s’en rend compte et il doit corriger l’erreur de sorte à trouver le bon hash
 * Le premier block d’une blockchain s’appelle le block de la genèse


### Hashing

 * N’importe quel procédé qui permet de représenter des données par une autre donnée plus compacte
 * Par exemple, un hash très simple d’encryptage d’email serait de prendre le produit de la valeur numérique de chaque caractère du message
 * Collision : quand le hashing de deux inputs différents produit le même hash


### SHA-256

 * Function de hashing utilisé dans le bitcoin
 * Ne pas confrondre encryption et hashing. Encryption induit une fonction reverse ce qui n’est pas le cas du hashing
 * 256 représente le nombre de bits du message hashed (séquence de 0 et 1 de longueur 256), quelle que soit la taille du message
 * On représente le hashing en format hexadécimal, i.e. avec les caractères 0 à 9 plus les 6 premiers lettres de l’alphabet. La taille d’un hashing est de 64 caractères
 * Une des façons de comprendre que le reverse n’existe pas est par exemple si on hash un film de 8 Go, on aura 64 caractères. Quel sens cela a-t-il de penser qu’on peut retrouver 8 Go de data à partir de 64 caractères ?


### Keccack – 256

 * Fonction de hashing utilisée par ethereum


### Travail des miners

 * Ils prennent les transactions situées dans un memory pool. Ces transactions ne sont pas encore validées, elles ne sont pas dans la blockchain
 * Ils commencent par vérifier que ces transactions sont possibles, i.e. que celui qui envoie l’argent détient bien au moins le montant nécessaire dans son wallet
 * Ils tentent de hash l’ensemble des transactions du pool + le « nonce » aléatoire (number only once) de sorte à ce que le hashing commence par un nombre important de zéros
 * L’idée étant qu’il faut pas mal de computation power pour y arriver, a tel point qu’un individu seul ou bien même un état ne serait pas en mesure de propager une modification / corruption au sein de l’ensemble de la blockchain
 * Les miners testent donc un maximum de nonce et quand ils tombent sur le hash qui contient le bon nombre de leading zéros (nombre généré aléatoirement), ils sont récompensés par du bitcoin et par les transactions fees
 * Le montant de cette récompense décroît avec le temps. Tout les trois ans, la récompense est réduite de moitié. Le dernier bitcoin sera miné en 2140
 * La probabilité de trouver le bon hash est de 1/16 à la puissance 19, autrement dit l’équivalent du nombre de shuffle nécessaire de 13 decks de carte pour que la première carte des 13 decks soit par exemple le 2 de trèfle


### Consensus

 * La façon dont la validation des transactions est effecutée
 * Le consensus du bitcoin et de l’ethereum est le prof of work, chercher le hash qui renvoie un début de x zéros dans le hashing
 * Attention car certaines crypto ont un consensus faible ou attaquable
 * Le pow confère une très bonne sécurité
 * Le pow demande une énergie considérable, le coût électrique est fou


### Ecosystème Ethereum

 * Pour un smart contract nécessite du gas pour qu’il soit run par les nodes du système
 * Un programme informatique nécessite un certain volume de gas
 * Mais le gas a un certain coût qui peut fluctuer entre 50 et 700 gweis
 * 1,000,000 gweis = 1 Ether
 * Les smart contract s’arrêtent de tourner si l’auteur ne dispose plus de gas (attention aux boucles infinies)
 * Le système devient inneficient lorsque le prix du gas est trop haut
 * Apparemment, il va y avoir une espèce d’amendement dans le futur afin que le pric du gas reste relativement bas et stable mais j’ai pas exactement compris comment
 * Dans le futur, le gas ne sera pas obligatoire mais l’auteur d’un contract devra faire une donnation afin que son smart contract soit run, plus la donnation est élevé plus vite sera effectué son contrat
 * Apparemment le réseau ethereum possède un type de token standard dit ERC20, c’est une sorte de monnaie fungible, i.e. 10 tokens de 1 dollars équivaut à un token de 10 dollars. Ces tokens peuvent être créer via des smart contracts. Ils peuvent représenter tout un tas de choses, une nouvelle monnaie, de l’argent, des actions, des points de fidélité, etc. Ces tokens peuvent être échangeable sur une plateforme d’exchange
 * Le réseau ethereum a également la possibilité de créer des tokens dits non fungibles, i.e. uniques comme grâce à la catégorie ERC 721. Ces tokens ne sont donc pas interchangeables. ERC 721 est une sorte de norme de création. Les tokens alors crées intègrent la blockchain. Contrairement à ERC 20, ils ne sont échangeables que sur des places de marchés très spécialisés. Ce sont ce qu’on appelle un NFT
 * Les oracles sont des ponts vers des données situées à l’extérieur de la blockchain ethereum. Typiquement, dans le cadre de paris sportifs, le smart contract a besoin qu’un oracle rentre le score d’une rencontre afin de pouvoir rétribuer les parieurs. Cela ouvre beaucoup de probleme pour la blockchain puisque cela permet l’intrusion d’un tiers dans les données du système. Plusieur startups bossent sur la création d’oracle fiable comme chainlink


### Collatealized Stable coins

 * Le cours du bitcoin est 5x plus volatile que le cours du marché des actions
 * Il y a eu un besoin rapidement de stabilité dans le monde des crypto monnaies
 * Un stable coin est une crypto indexée sur la valeur d’une monnaire fiduciaire classique
 * Le stable coin le plus connu est tether
 * Apparemment pour qu’un stable coin fonctionne il doit certifier des garanties fortes
 * Un stable coin peut être collateralized ou non / decentralized ou non


### Aparté sur les collatérals

 * C’est une garantie qui sert à couvrir le risque en cas où quelqu’un ne pourrait pas satisfaire ces obligations de paiement
 * Par exemple lors d’un prêt à un particulier la banque peut prendre comme collateral la voiture de ce dernier
 * Des banques peuvent émettre leurs propres billets backés par une garantie quelconque comme des bons du trésor etc.


# Les problèmes résolus par la DeFi

### Ineffiency 

 * Les transactions ici vont vite et peuvent être volumineuses, en dehors de la defi cela pourrait constituer un fardeau import pour une grosse boîte
 * Les smart contract étant donné leur nature sont réutilisables facilement
 * Les smart contracts sont apparemment utilisables par quiconque cherchent le service proposé par un smart contract par exemple pour executer une option. Pas d’interview, pas de chèqe
 * Pas d’autorité
 * Pas de bâtiments
 * Pas de personnes intermédiaires
 * Les keepers sont des participants externes aux dapps, ils track par exemple les collateral/guaranties qu’on peut mettre dans un smart contract (un peu obscure). Apparemment ils sont très important dans l’écosystème pour que celui-ci devienne pérenne il faut des veilleurs qui garantissent certains trucs externes à la blockchain. Par exemple si vous ne payez plus, ils peuvent liquider votre garantie. C’est un service. 
 * Les forking : en gros on peut proposer une nouvelle version ou bien une amélioration d’un smart contract en forkant le code source et en le proposant. Donc on en tire alors les bénéfices. Ca fait un cercle vertueux ou chacun peut améliorer le service et celui devient à chaque fois meilleur. Ca crée une compétition saine. Il en va de même pour les dApps. Même si j’ai pas trop compris la différence entre une dApp et un smart contract. Les smart contract sont des éléments d’une dApp. Pour se voir octroyer un prêt il est nécessaire de donner des garanties en premier lieu. Pour ce faire je passe par un smart contract
 * Vampirisme : en gros c’est le fait de copier quasiment 100% une application et de proposer des incentives plus puissant afin de piquer tout les users de l’application originale. Grosse compétiton. Les clients sont contents. Il existe un risque cependant, le code peut être hijacked et modifié de sorte à créer des opportunités de vol.


### Limited access

 * Tout le monde peut avoir accès à la blockchain ethereum, c’est la finance democracy d’après le prof
 * Les yield farmers sont les acteurs qui permettent aux prêts de s’effectuer au sein de ce genre d’écosystème. Ils prêtent de l’argent et sont récompensés pour ça. Ils ont l’air de dire que le taux d’intérêt d’un deposit est plus avantageux dans un système de defi. Voir la platforme de Leonardo AAVE. Cela aurait a voir avec le fait que les coûts de maintien dans la CeFi sont très élevés. Dans la DeFi, on aurait des taux de prêts plus bas et des taux d’intérêt plus élevés
 * En gros tu déposes ta thune dans un pool et tu en es récompensé pour ça. Tu reçois un token qui représente la part que tu détiens dans le pool. C’est plus avantageux que les saving rates actuels des banques et c’est moins risqué que d’investir sur le bitcoin ou l’ether. Le but étant de contrer l’inflation naturel
 * Initial De Offering : le même principe qu’une IPO mais plus démocratisé, plus facile d’accès, beaucoup moins de contraintes. Ca fonctionnerait avec un token


### Opacité

 * Tout est consultable sur un smart contract, il n’y a pas de police plus petite qu’une autre pour endormir les potentiels clients
 * Si jamais, il y a une faille volontaire, on peut faire confiance à la wisdom crowd dans le sens où la collectivité aurait eu le temps de le voir et donc aurait probablement forker le smart contract et l’aurait modifié pour supprimer cette faille
 * Un contrat peut comporter des encouragements et des pénalités pour les utilisateurs, ce qui peut favoriser le bon comportement de tout le monde
 * Token contract : c’est un type de smart contract, on peut savoir combien de tokens sont en circulation, on ne peut pas le changer, aucune inflation possible contrairement à la CeFi. Il peut y avoir de l’apport ou de la suppression de tokens mais tout est inscrit dans le smart contract











