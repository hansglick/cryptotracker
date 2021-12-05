# References

MOOC de l'université de Michigan : https://www.coursera.org/specializations/financialtechnology#courses


# Introduction

Les métiers de la Finance tenus habituellement par les banques sont concurrencés récemment par tout un tas de compagnies spécialisées dans la technologie :
 * Transfert d’argent :
   * Ally
   * N26
   * Monzo
   * Paypal
   * Venmo
   * AliPay
   * Libra
   * Bitcoin
 * Lever de fonds :
   * Lending Club
   * Kabbage
   * KickStarter
   * ICO, STO, IEO
 * Investissement : 
   * Vanguard
   * Quantopian
   * Betterment
   * Robinhood
   * Credit Karma
   * Nerd Wallet
   * Mint

Différents types de paiements : 
•	C2C : consumer to consumer
•	C2B : consumer to business
•	B2B : business to business

Deux grandes manieres de transférer de l’argent :
•	Centralisée : la manière classique qui nécessite un tiers. 
•	Décentralisée : crypto currencies et smart contract, ici le tiers est la communauté toute entière

Paiemant par chèque
 Les désavantages :
•	De nombreux acteurs / intermédiaires
•	Des possibilités de fraudes (catch me if you can)
•	Une latence très longue pour une transaction

Rôle des banques :
•	Elles sont là pour fournir une certaine confiance entre deux acteurs
•	Cette confiance permet au système de fonctionner
•	Cette confiance est un service de la banque, c’est en partie pour ça qu’on paie

Rôles des acteurs de la fintech dans ce bordel :
•	Ils veulent pouvoir cutter les intermédiaires et les temps de réponses et les authentifications, etc.


ACH
C’est le réseau par lequel transite la majeur partie des transferts d’argents aux USA, c’est une version éléctronique du transfert par chèque, en voici les avantages :
•	Réduction des coûts, envoyer un email est moins cher qu’envoyer un courrier
•	Réduction des coûts, les demandes de transferts ne sont pas envoyés en temps réel mais par batch, deux fois par jour
•	Le transfert d’argent est plus rapide puisqu’il se cale sur le transfert d’informations qui est un message éléctronique. Ca met environ deux jours maximum versus parfois deux semaines pour un transfert via chèque
•	Il y a moins d’espaces pour la fraude vu la rapiditié du transfert
En voici les défauts :
•	Pas du tout user friendly, il faut se rappeler d’un nombre important d’identifiants complexes et non normalisés pour une transaction

Les digital wallets
Le principal défaut de ACH, a favorisé l’essor des companies digital wallets :
•	L’app est user friendly
•	Les identifiants sont des numéros de télphone ou bien des emails (plus facile à retenir)
•	Les systèmes d’authentification sont basés sur les technologies disponibles sur un smartphone comme la caméra ou bien le finger print
•	Ils convertissent ces données en données compatibles et se plug sur l’ACH
On distingue différents types de digital wallets : 
•	Les pures players comme paypal
•	Les hybrides comme alipay
•	Les social : venmo, wechat, facebook

Le cas du pure player (PayPal)
Il joue l’intermédiaire entre deux parties :
•	La bank du sender
•	La bank du receiver
•	La bank de paypal
•	Le sender crédite son compte paypal de 100 dollars
•	En fait il envoie 100 dollars sur le compte de paypal
•	Paypal garde l’argent sur son compte
•	Mais crédite le compte paypal virtuel du reciever, l’argent n’a en réalité pas bouger
•	L’argent ne bouge que lorsqu’un des users veut faire un withdrawal 
•	Dans ce cas la paypal envoie l’argent de son compte sur celui qui withdraw

Le cas de l’ecosystem player (alipay)
C’est un pure player qui a deux révolutions :
•	qui au lieu de stocker l’argent des sender et receiver dans un compte, ils le font fructifier, ainsi les utilisateurs ont intérêt à laisser leur argent sur le compte alipay plutôt qu’à faire des withdrawal.
•	Facilite les paiement avec les partenaires brick and mortar via le QR code. Les users quand ils achetent un sandwich, ils ouvrent leur app alipay, scanne le QR code du marchand, le marchant leur envoie la note, il la valde et c’est terminé

 Le cas du social player (wetchat, venmo)
Tout pareil que les autres a part que leur data ont un peu plus de valeur étant donné qu’on peut les corréler avec les data sociales, on peut ainsi trouver et comprendre les raisons sous jacentes des transactions. On a le contexte social des transactions











Les cartes de crédit
Les cartes de crédit naissent du problème suivant : un acheteur et un vendeur se mette d’accord. Le vendeur a besoin de confiance envers l’acheteur qu’il ne connait pas. Il y a un problème car l’acheteur ne possède pas la somme d’argent demandée. La carte de crédit permet de dire au vendeur, je suis la banque de l’acheteur, ne t’inquiète pas, l’acheteur a suffisament d’argent pour te payer, moi sa banque je vais t’avancer l’argent, je te le garantie, sûrement dans quelques jours. VISA et MASTERCARD sont deux réseaux bancaires capables d’approuver ou pas cette confiance. Lors d’une transaction par carte de crédit on dénombre 5 acteurs : 
•	L’acheteur
o	Il a une carte de crédit qui contient toutes les informations de son compte en banque
•	Le marchand
o	Il possède l’équipement qui permet de lire la carte de crédit de ses acheteurs
o	Rassuré par la banque de l’acheteur qui lui promet d’avancer l’argent, il est satisfait du service rendu. Il paye ce service environ 2.5% du prix de l’article
•	La bank de l’acheteur
o	Elle recoit la requête via le réseau VISA, elle s’assure que 
	l’acheteur a bien de quoi lui rembourser son prêt temporaire,
	qu’il ne s’agit pas d’une fraude
	quand tout est ok, elle renvoie l’information au marchand qu’elle lui avancera l’argent
	et elle avance l’argent à la banque du marchand quelques instants plus tard
o	c’est elle qui prend le plus de risques puisqu’elle prête l’argent et qu’elle est responsable en cas de fraude, elle se doit de rembourser. Elle se paye donc grassement entre 2 et 3% du montant de l’article
•	La bank du marchand
o	Elle recoit l’argent quelque temps après la transaction
o	Pour le service de récupérer l’argent elle prend tout de meme une commission à hauteur de 0.15% de prix de l’article
•	Le réseau VISA par exemple
o	Il est les rails qui permettent aux informations de transiter
o	Il se doit d’avoir un réseau performant afin d’être robuste aux cyber attaques et de fournir une latence rapide
o	Il prend environ 0.15% du montant de la transaction
o	Son système est complexe et coûteux car il doit supporter les transactions en temps réel
•	L’équipement qui envoie les informations au réseau VISA et qui les recoit
o	Il envoie et recoit les informations relatives à la banque de l’acheteur
o	Il ne prend qu’un risque limité et donc prend environ 0.05% du montant de la transaction





Les avantages de la carte de crédit :
•	Permet la detection de fraude de la part de issuer
•	Permet une grosse rapiditié
•	Service comme avancer un prêt
•	Augmente la fidélité
•	Permet de vendre d’autres services

Les défauts de la carte de crédit
•	Fraude copie de la piste magnétique
•	Fraude sur les transactions online, les marchands stockent les informations de la manière qu’ils veulent sans aucun crptage, qu’ils peuvent ensuite envoyer 
•	Le coût pour les marchants, les fameux 2,3% plus les infrastuctures en hardware
•	Ils ne sont pas récompensés les données récoltés sont en général pour eux difficilement exploitable, pas de CRM, pas de facilité de préparation de l’impôts à payer, etc.
•	Elles n’existent pour le moment que pour ceux qui disposent d’un compte en banque, il y a une floppée de population qui n’en ont pas, les jeunes et les populations de certains pays

Rôle des Fintech dans le business des cartes de crédit
La faille dans laquelle s’implante la fintech dans les cartes de crédit. La fintech s’implante essentiellement pour limiter les cas de fraude. On distingue environ trois types de fraude : 
•	Physical point of sale fraud, en gros les fraude sur les points physique, ça consiste à pirater une carte de crédit qu’on aurait dans les mains en copiant la piste magnétique d’une manière ou d’une autre. EMV est une technologie qui lutte contre ça :
o	EMV en clair encrypte les informations lues sur la carte de crédit puis l’envoie
•	Online point of sale fraud, en gros les fraudes qui consistent à voler les informations des cartes de crédits sur les sites marchands ou bien des particuliers vers les sites marchands ou bien des sites marchands vers les banques. La méthode de la tokénisation permet de lutter conte ce type de fraude
o	Tokenization permet là aussi d’encrypter les informations bancaires des clients avant de les envoyer
•	Client side fraud  qui consiste à voler informations bancaires d’un user directemnt depuis son mobile ou bien son ordinateur. Les services mobile comme Apple Pay et Google Pay permettent de lutter contre ce type de fraude. Apple Pay :
o	Au moment où l’on s’inscrit, on enregistre sa carte
o	A ce moment là, la banque renvoie un token spécial directement lié aux informations bancaires
o	Une fois arrivé dans le téléphone, ce token n’est manipulable qu’à l’aide de données biométrique
o	Pour un achat, le user délivre ses données biométriques, alors le token est encrypté dans un nouveau token et envoyé via un truc NFC de son smartphone
o	Le nouveau token est envoyé alors a la banque issuer, il est decrypté, les vérifications sont faites, puis la banque renvoie sa confirmation ou pas

Les actors de la finetech concernant les cartes de crédit se focusent sur le hardware, software et les services rendus aux marchants qui utilisent leur techno comme par exemple du crm, etc. Square est le leader sur le marché : 
•	Il comprend tout de suite que les informations peuvent transiter par le réseau internet plutôt que par le réseau téléphonique
•	Il comprend également qu’un terminal de paiement possède autant sinon moins de puissance de calcul et de processeur que n’importe quel smartphone
•	Il comprend enfin que pour la lecture d’une carte, il suffit juste d’inventer un badge connecté à un smartphone pour faire l’affaire
Stripe fait la même chose pour les paiement en ligne : 
•	Ils mettent a la disposition des marchands qui ne disposent pas des moyens nécessaires une api qui prend tout en compte
•	Ils prennent une com aux marchands évidemment pour chaque transaction
•	En revanche, ils ont un souci avec les bank issuers qui va leur prendre une grosse part du gateau si le prêt est considéré comme risqué, raison pour laquelle, ils proposent en plus comme servicesà leur client marchands, des analyses de données pour être simple

MPESA
Un système d’envoi et de paiement adapté aux endroits dans le monde où la population n’a pas accès aux banques :
•	Les agents sont disposés un peu partout sur le territoire. Dans les commerces, les pompes à essence, etc. 
•	Les agents peuvent déposer de l’argent à la banque MPESA en échange d’argent éléctronique. Ou bien ils peuvent déposer de l’argent éléctronique en échange d’argent physique. Ce qu’ils vendent c’est de l’argent éléctronique utilisable par un téléphone portable classique non smartphone. 
•	Un utilisateur peut ouvrir un compte MPESA à l’aide d’un télphone et de sa carte d’identité. Il peut dès lors recevoir de l’argent et/ou en envoyer en créditant son compte via un des nombreux agents qui maillent le pays
•	Les agents sont confrontés au problème du vendeur de journaux (en gros c’est un problème de stockage), il doit décider de combien d’argent éléctronique et de cash il doit détenir chaque jour. S’il n’a plus d’argent, il ne peut plus servir ses clients, s’il en a trop, il prend un risque en terme de sécurité et d’investissement (l’argent pourrait être plus utile autre part)






Blockchains


Introduction
En gros, la blockchain c’est une base de données décentralisée, ce qui veut dire que plusieurs copies sont disponibles par l’ensemble de la communauté. La différence qui existe entre deux blockchains repose principalement sur deux choses :
•	Que peut on uploader dans cette base de données ? des coins dans le cas du bitcoin
•	Le consensus, i.e. le processus qui permet d’uploader quelque chose dans cette base de données
Vue de haut, ça donne ça :
•	Un client qui permet de générer la data à uploader
•	Un network un peu particulier de style peer to peer va recevoir la data,	 et va la processer via le consensus. Les acteurs de ce networks sont appelés les nodes/minors/validators
•	puis la data va être stockée dans la database, i.e. la block chain


Différents types de données
Les blockchains peuvent uploader différents types de données :
•	des transactions monétaires comme le bitcoin, il se trouve que c’est néanmoins pas très efficace, les gens s’en servent plus comme de l’or 2.0. MOSTLY COINS (utilise sa propre blockchain)
•	des programmes, la block chain est dite programmable et ses programmes sont ce qu’on appelle des smart contracts. Il se trouve que pour le moment on ne peut pas héberger des programmes trop complexes. . MOSTLY COINS (utilise sa propre blockchain)
•	enterprise blockchain comme le ripple. MOSTLY COINS (utilise sa propre blockchain) &&  TOKENS, i.e. se branche sur d’autres blockchains
•	utility and security tokens, utilisé apparemment pour le crédit et la levée de fonds. MOSTLY TOKENS, i.e. se branche sur d’autres blockchains
•	stablecoins, qui s’index sur les monnaies classiques. MOSTLY TOKENS, i.e. se branche sur d’autres blockchains







Public vs Private
Les blockchains ont également des caractéristiques différentes concernant le caractère publique ou non des informations enregistrées dans leur base de données :
•	le bitcoin est par exemple entièrement public, tout le monde peut consulter la base et ou devenir un node/miner. C’est la version la plus décentralisée de la blockchain qui existe
•	PRIVATE blockchain, les nodes se connaissent tous, et pr etre un nouveau node, il faut une permission, on peut imaginer une blockchain entre un fournisseur et ses clients par exemple. Le consensus est généralemnt moins complexe
•	Permissioned blockchains, entre les deux. L’identité est vérifiée. Le ripple en est un très bon exemple. 

Les clés de sécurité dans la Blockchain
Pour s’authentifier dans une public blockchain, on a deux clés : 
•	La clé publique : elle sert à indiquer à la communauté le numéro du compte du user
•	La clé privée : elle sert à utiliser le compte en question (i.e. envoyer de l’argent)
•	Cela pose un problème car si on perd la clé privée, on a plus accès à notre compte, et si quelqu’un l’utilise il peut laver le compte immédiatement, personne ne pourra rien faire
•	On peut créer autant de comptes que l’on souhaite, tant qu’il n’y pas eu de virement, on n’existe pas dans la block chain puisqu’elle ne fait qu’enregistrer les transactions

La Chaîne
Chaque bloc contenant les enregistrement de milliers de transactions est hashé vers un code de 256 caractères. Le prochain block pointera vers le hash du block précédent. Les avantages sont les suivants :
•	Facilité la recherche dans la base de données, en ne recherchant qu’un seul block puis en cherchant à l’intérieur de ce block plutôt que dans toute la base entière
•	En permettant un contrôle sur la cohérence des données. Comme chaque block pointe sur le hash du block précédent, il devient plus compliqué de modifier frauduleusement les transactions d’un block. En effet, en modifier les transactions du block 0, le hash de ce block modifié sera différent du hash vers lequel pointe le block 1. Autrement dit, on peut savoir directement, qu’il y a eu une tentative de fraude






Business model de la block chain
Donc la block chain est une base de données. Chaque transaction est enregistrée dans la base. Etant donné que le système est décentralisé, il faut trouver une méthode pour récompenser les nodes qui participent à la survie du système. Ils ont donc trouvé la méthode suivante pour forcer les gens à participer aux enregistrements :
•	Idée : récompenser ceux qui ont la plus grosse puissance de calcul (car il faut qu’être récompensé soit corrélé à un coût)
•	La façon de faire est de résoudre un problème dit hash problem qui nécessite une certaine puissance de calcul. La complexité de ce problème est défini par le système de sorte à ce que les nodes mettent en moyenne 10 minutes à le résoudre
•	Le vainqueur du problème a le droit de valider le block et prend une récompense en bitcoins, i.e. il a miné du bitcoin
•	Les autres font des tâches simples comme vérifier la cohérence des transactions, ils recoivent donc des récompenses faibles

Bitcoin Mining
Concernant le mining du bitcoin, plusieurs chosesà savoir en vrac :
•	Ni le CPU, ni le GPU sont efficaces pour miner du bitcoin, car ces éléments ne sont pas focus à 100% dans le calcul de hash. Il existe des cartes spécifiquement conçues pour cette seule tâche appelé IAUSC
•	Il y a très peu de chances d’être rentable sur du mining en individuel, il faut construire une ferme de mining ou bien intégrer un mining pool dans lequel toutesles cartes travaillent ensemble à la résolution du problème. Si le pool trouve la solution, la récompense est distribué en fonction de la puissance de chacun.
•	Aujourd’hui, une transaction nécessite une quantité énorme d’énergie, comparable à ce qu’une maison a besoin pour 3 semaines . En comparaison, la carte VISA avec le tiers d’energie permet 1 millions de transaction











Ethereum

Introduction
Ethereum se voit pas comme une base de données chargée d’enregistrer des transactions financières mais se voit plus comme une sorte de cloud qui stocke des programmes. Ceux-ci sont executés par les nodes au moment de la validation. Leur execution est récompensé par du « gaz », a savoir l’éther, la crypto monnaie du système. Ethereum a son propre langage de programmation, semblable à Python, Solidity. La principale fonction de la blockchain éthereum n’est pas le payment peer to peer. Tu ne peux pas acheter des trucs dans ton épiceries avec de l’ether. L’ether est une sorte d’utility coin, tu achetes de l’éther afin de payer les nodes ethereum qui executeront ton programme. L’ether ne peut pas être miné avec des chips bitcoin mais avec du GPU. Le nombre d’ether produit n’est pas limité comme le bitcoin. Pour l’instant c’est du proof of work mais ils ont l’intention de passer sur du proof of stake. Ethereum est structuré comme un business, piloté par la Ethereum foundation. Les premiers ethers ont été vendu publiquement comme une introduction en bourse dans la monnaie de Bitcoin. Les nodes dans la blockchain ethereum run les applications et mettent à jour les états de la blockchain, ils sont retribués en contrepartie en ether via le proof of work.



















Cryptocurrencies en tant qu’actifs
Sans surprise les crypto sont beaucoup plus volatiles que les actions classiques. Leur évolution semblent décoréller des autres stocks et monnaies. En revanche la valeur des crypto en général semblent corrélées les unes aux autres. Autrement dit, quand le bitcoin monte, les autres crypto montent et réciproquement. Deux facons d’acheter des crypto currencies : 
•	Sur la blockchain : quelqu’un t’envoie des bitcoins sur ton compte et tu lui envoie des dollars sur un compte paypal par exemple
•	Sur une plateforme d’échange : on charge un wallet virtuel avec soit des dollars ou soit des crypto, puis comme sur paypal, les comptes virtuellement mis à jour, les inscriptions dans la blockchain ne surviennent que l’acheteur veut mettre ses crypto dans une wallet. En fait, la plateforme recoit les déposits des utilisateurs, qui peuvent soit déposer des dollars soit des crypto. Déposer un dollar sur un exchange revient à créditer de 1 dollar le compte en banque de l’exchanger. Déposer un bitcoin sur un exchange revient à envoyer un bitcoin sur le wallet de l’exchanger. Toutes les opérations sont donc virtualisés par l’exchanger, i.e. on peut trader du bitcoin et du dollar quasiment instantanément. Les choses deviennent réelles lorsqu’on souhaite withdraw. Si on withdraw du bitcoin alors, la blockchain se met en marche le wallet de l’exchangeur nous envoie les bitcoins sur notre wallet, si on withdraw nos dollars, alors la bank de l’exchanger envoie des dollars sur notre compte en bank. Il est à noter que l’exchangeur joue différents rôles et donc qu’il concentre de multiples risques. Il n’est soumis à aucune institution financière réglementée et on se doit de lui faire entierement confiance. 
•	Création d’un wallet : pour pouvoir acheter et vendre des crypto il faut une identité sur la block chain autrement dit, il faut générer une paire de clés privés et publiques. Un wallet peut avoir une forme physique impression sur un papier, ou bien electronique à l’aide d’un soft. Pour rappel, la public key sert à recevoir des bitcoins (adresse), la private keys sert à les envoyer (signature pour les transactions). La façon de garder les clés en tête est crucial, il existe grosso modo trois façons :
o	Ecriture dans un fichier de son téléphone/ordinateur
o	Impression sur papier puis mise dans un coffre fort
o	Cloud storage, certaines platforme d’exchange propose ce genre de service ou les clés sont stockés dans un cloud numérique sécurisé
•	La bonne pratique serait d’utiliser différents jeux de clés pour différents wallets. Les wallets contenant bcp de bitcoins se doivent d’avoir leur clés sécurisés de manière forte. Les wallets contenant de petites sommes peuvent voir leur clés faiblement sécurisées








Les risques liés au trading de crypto currencies :
•	L’exchanger n’est généralement pas soumis à des instiutions financières. Il peut à tout moment se faire la malle avec notre thune. Il n’y a que très peu de recours possibles
•	L’exchanger n’étant pas soumis à des règles, on ne sait rien de sa capacité à pouvoir sécuriser ses différentes wallets qui contiennent les bitcoins qu’on déposé leur clients. S’ils se font hacker, les recours sont quasi impossible, il n’y a aucune réglementation
•	L’exchanger peut également manipuler les cours du bitcoin en simulant de faux achats avec de faux comptes puisqu’ils jouent le rôle du broker, ils peuvent prétendre que tant de bitcoins ont été vendus à tant de dollars alors que l’argent n’a jamais circulé entre des personnes physiques mais seulement entre des faux comptes sur l’exchangeur
•	L’exchanger n’étant sousmis à aucune règle, il peut se retrouver en défaut de liquidité si tout le monde vient à retirer ses biens de ses comptes. Chose assez fréquente étant donnée la volatilité des crypto, on observe beaucoup de panic withdrawal

Risques liés au bitcoin
•	Attention, car on peut créer autant de bitcoin qu’on veut une fois qu’on a le code open source. Il n’est pas certain qu’on puisse dire que le bitcoin sera de moins en moins produit (pas vmt compris)
•	Il préconise de n’investir que dans les projets concrets qui ont une utilité dans le monde de la finance plutôt que dans des trucs qui n’ont à priori pas d’impact dans le monde réel
•	Le côté irréversible ou bien immuable de certaines crypto ne jouent pas en leurs faveur car le risque de fraude est tel qu’elle peut empêcher les sites marchands de les utiliser


 
CreditTech

Introduction
Le métier du crédit est assez simple. Quand on prête de l’argent. Il faut s’assurer que le prêt te rapporte de l’argent, i.e. que ça te rapporte plus que :
•	Ce qu’il gagnerait en prêtant à la banque américaine
•	Ce qu’il perdrait si le prêteur lui ferait défaut
•	Du salaire qu’il doit se verser

En détails
•	Probabilité que la personne lui fasse défaut : DEFAUT ; 0.1 = 10%
•	Intérêt du prêt : INTEREST ; 0.1 = 10 %
•	Intérêt de la trésorie americaine : TREASURE ; 0.1 = 10%
•	Argent preté : MONEY ; $1,000
•	Rentrée : (1-DEFAULT) * VOLUME * INTEREST
•	Sortie : DEFAUT * VOLUME 
•	Expected Volume = (1-DEFAULT) * VOLUME * INTEREST - DEFAUT * VOLUME
•	Expected Volume = VOLUME * ((1-DEFAULT) * INTEREST – DEFAULT)
•	Expected Volume > VOLUME * TREASURE * PREMIUM
•	Interest Rate = Risk Free Rate + Expected Loss + Risk Premium

Business Model
Afin d’accroître son profit, un prêteur ne peut agir que  sur un levier 
•	Le taux d’intérêt des banks (NON)
•	Le premium (NON)
•	Le taux de défault (OUI) 
o	Demander un collatéral, en gros un gage, par exemple une voiture, i.e. si la personne ne rembourse pas le prêt, la banque vendra la voiture
o	Reduction l’exposition du défaut de paiement, en gros créer des échelons, i.e. demander un remboursement tout les mois par exemple. Si il ne paie pas le dernier mois, il a quand même payer les mois précédents
o	Estimer la probabilité de défaut de paiement via la data science, le métier des Fintech






Raise money

On peut lever des fonds de plusieurs manières
•	Créer de la dette
o	Aller voir les banques en demandant un prêt
o	Aller voir les investisseurs en créant des bonds
o	Nouveaux métiers de la Fintech :
	Plateform Lending
•	Vendre des biens
o	Public Equity : IPO (vendre des stocs par ex), SEO
o	Private Equity : VC, private placements
o	Nouveaux métiers de la Fintech :
	Equity & Crowdfundings
	ICO / IEO


Plateforme Lending (P2P Lending)
En fait un prêt bancaire nécessite trois grandes étapes. Lire les informations du candidat, faire de la data pour évaluer le risque de défaut, puis écrire le contrat et suivre l’évolution du remboursement. Les nouveaux acteurs de la Finetech s’intègrent dans les deux premiers steps, là où ils sont naturellement meilleurs que les banques. C’est ce que font les plateforme Lending. Ils passent ensuite la balle aux banques qui font ce qu’ils savent faire puis ils se partagent les gains. Donc en pratique ils ne renvoient pas une probabilité de défaut mais des buckets de loans en fonction de la probabilité de défaut, plus t’es solvable plus tu tombes dans un bucket avec des taux d’intérêt faible. En pratique la suite en détails : 
•	Processus de sécurisation du prêt : un prêt de 10,000 dollars à un taux de 7.3% est par exemple divisé en plusieurs prêts appelés notes. 400 notes de 25 dollars par exemples. Ca permet en fait aux investisseurs de réduire les risques en prenant des notes de différentes personnes. Risque est dilué via la diversification.
•	Puis, le user attend que toutes les notes de leur prêt soient prises par un ensemble d’investisseurs, c’est pourquoi ça peut mettre plusieurs semaines d’attente
•	A noter que ni la plateforme lending ni la banque ne prenne de risques ici, ce sont juste lesinvestisseurs qui achetent les notes qui en prennent
Différents types de plateformes lending : 
•	P2c : peer to consumer (Lending Club par ex), les investisseurs sont des particuliers de même que les bénéficiaires
•	P2b : peer to business (Kabbage par ex), les bénéficiaire sont généralement des entreprises petites ou moyennes et les investisseurs sont des particuliers ou des institutions
•	Leur business se résument a faire matcher des vendeurs (de prêt) et des acteurs (de prêt)
•	Ils sont censés faire des modèles plus précis en incorporant des data auxquelles les banques n’ont tradionnellement pas accès comme les données des réseaux sociaux, les derniers achats, etc. 
Les risques du business :
•	Macroeconomic : les notes ne suffisent pas à réduire tout les risques. Par exemple si un événement frappe tout les users en mm temps, ils sont niqués car c’est un risque macro
•	Microeconomic : beaucoup de fraudes possibles car les barrieres sont basses pour attrapper un maximum de connards car le monde des plateformes lending est très concurentiel. Que ce soit pour les prêteurs ou les users, certains prêteurs ont tendance à abuser en mettant en place des pyramides de ponzzi, pour attirer un max de monde mais tout peut vite s’écrouler



Crowdfunding
Raison d’être
Quand une idée est trop novatrice elle se heure au problème suivant. Les Venture Capitals ne savent pas évaluer le risque d’un projet nouveau, d’une boîte qui n’a aucun historique et dont ils ne connaissent pas les fondateurs. L’idée des plateformes de crowdfunding intervient ici. Au lieu de rechercher quelques grosses VC pour financer un projet, on peut rechercher plein de micro investisseurs. Le business des plateformes de crowdfunding est de matcher des projets et ds investisseurs. Si le projet fonctionne les fondateurs s’engagent à reverser des dividendes aux micro investisseurs, ces dividendes peuvent être de différents formats : 
•	Produits, un peu comme KickStarter
o	L’entrepreneur cherche en réalité à pré vendre ses produits et les micro investisseurs ne cherchent pas forcément le profit mais le produit
o	S’il rate l’entrepreneur ne perd rien mis à part sa réputation auprès des investisseur mais aussi et surtout auprès des VC car c’est en général le plus souvent un tremplin vers eux plutôt qu’une fin en soi
o	Si le funding goal (montant a partir duquel l’entrepreneur est engagé à commencé le projet) n’est pas atteint alors la plateforme renvoie l’argent aux investisseurs
o	La plupart du temps, ces campagnes de crowdfunding sont utilisés comme un moyen marketing de se faire connaître pour pas cher
o	Le problème de ces plateformes est que rien n’oblige les entrepreneurs à fournir toutes les informations qui peuvent servir à estimer le risque du projet 
•	Argent, un peu comme des actions
•	Tokens, basé sur la plateforme blockchain, donc ca s’adresse aux inventeurs de projets crypto qui veulent financer leur projet, ils vont donc lever des fonds et récompenser les investisseurs par leur crypto monnaire, on distingue deux types de récompenses :
o	ICO : les tokens fournis sont des smart contract, et ca peut donc etre soit des crypto soit des objets en nature. C’est une sorte de prévente de l’accès à des produits ou des services futurs. Ces tokens sont achetables par les investisseurs en monnaie crypto ou classique. La différence avec le produit comme kickstarter c’est que tu peux déjà échanger tes tokens, voire même les trader. Les ICO attirent donc différents types d’investisseurs : les spéculateurs et ceux qui croient en l’idée
o	STO : plus de l’equity, plus de contraintes pour y participer

Différence IPO vs ICO
Une company veut entrer en bourse
•	IPO :
o	Recruter un investisseur bancaire, ce sera ton conseiller financier en gros. Puis il rédigera les contrats
o	La commission des usa des exchange et securities (ICC) examinera le dossier et produira  un rapport. S’il est approuvé ou pas
o	RoadShow/primary market : a ce moment que se décide leprix de l’action à l’aide d’investisseurs
o	Seoncdary market : les actions sont  ouvertes au marché
•	ICO : 
o	Tout pareil sauf que tu ne détiens pas une part de la compagnie mais un accès a ses services grâce aux tokens
o	Il n’y a pas de SEC commission ici
o	Va directement au secondary market
o	Pas de négociation de prix, la compagnie fixe ce qu’elle veut comme prix comme utility token
o	Les utility tokens sont ensuite tradés comme n’importe crypto sur une plateforme d’exchange

Signes et décisions concernant l’évaluation d’une ICO :
•	Le Soft CAP : seuil de fonds récupéré au-delà duquel le ICO va commencer, i.e. ils lancent le projet. Si ce seuil n’est pas atteint alors ils rembourseront les donateurs.
•	Le Hard CAP : seuil de fonds récupéré au_delà duquel plus aucun investisseur ne peut prendre part. C’est terminé
•	Faire attention aux ICO dont le soft CAP est à 0 et le HARD CAP est infini. Ca ressemble à une arnaque, ils peuvent partir avec la caisse sans problème. Si le hard cap ne fait que de se déplacer, alorsc’est pas bon signe
•	Attention car lorsque les fonds se levés, contrairement à une IPO, lors d’une ICO il y a très peu de contraintes sur ceux qui récoltent la thune
•	Attention également car contrairement à une IPO, rien n’empêche les types de faire autant d’ICO qu’ils le veulent, auquel cas les jetons que tu as acheté à un certain prix, leur valeur peut potentiellement être dilué par des mises sur le marché de tokens sur plusieurs campagnes
•	Les crypto non ICO sont moins volatiles et moins rentables que les crypto ICO
•	Tips pour évaluer la qualité d’une ICO :
o	Durée du projet, plus le temps est long pour lever des fonds moins c’est bon signe
o	Ambition du projet, trop grande et trop petite sont des mauvais signaux
o	Qualité du code sur github
o	Nombre de contributeurs sur github
o	Fréquence des push sur github
o	Expérience des plus gros contributeurs sur github
•	Tips pour évaluer la sociologie du pool d’investisseurs d’une ICO :
o	Les tokens bon marché sont pris souvent par des petits investisseurs qui rêvent d’une multiplication énorme
o	Hype trop grosse du papier blanc attirera les investisseurs irrationnels qui n’ont pas les pieds sur terre

Le futur des banques traditionnelles 
Les banques traditionnelles sont faceà un dilemme versus les nouveaux acteurs de la FinTech :
•	Se battre contre eux (à l’aide des régulateurs, en créant des grosses barrières à l’entrée, en définissant des licenses plus contraignantes, etc.)
•	Les acheter (afin de les shut down ou du tout simplement utiliser leurs compétences)
•	Coopérer avec eux comme dans l’exemple d’amazon :
o	Amazon au milieu des années 2000 est face à un dilemme, il a beaucoup de concurrents sur le créneau des ventes sur internet
o	Il se demande ce qu’il fait mieux que ses concurrents que seul lui peut faire et pas les autres :
	Ce n’est pas son site internet, tout le monde peut le faire
	Ce n’est pas sa logistique, tout le monde peut se payer les services d’ups
	Ce n’est pas son machine learning tout le monde peut sous traiter
	C’est son ingénieurie informatique fabuleuse qui lui permet de régler des milliers de transactions à la seconde, de faire tourner des milliers d’algorithmes sur des centaines de serveurs différents en parrallèle etc
o	C’est pourquoi il crée AWS en 2006, offrant ainsi à leur concurrent une pateforme grâce à laquelle leurs concurrents enrichisserait Amazon s’ils grossissaient et qu’ils n’auraient pas envie de quitter vu le coût de recherche et développement que ca demanderait
•	Le concept de Bank As A Service vient de cette volonté de coopérer avec les acteurs de la FnTech plutôt qu’autre chose. Les banques sont surtout douées pour leur réputation de sécurité et de confiance qu’elles ont su construire, chose très difficile à acquérir pour les nouveau acteurs de la FinTech
o	En gros les métiers de la finance c’est les banques et les fintech. BAAS viennent s’insérer entre les deux pour faire le pont, pour faciliter les solutions afin que les fintech n’aient pas à construire a chaque fois des api pour communiquer avec les différentes banques, ici avec les baas c’est fourni clés en main, les fintech ne s’occupent que de ce qu’elles savent faire de mieux







Artificial Intelligence

Asset allocation
En gros où est ce que tu fous ta thune, dans les grands types d’assets par exemple : domestic stocks, bonds, emerging market stock, real state. C’est délicat car on doit le faire en fonction d’un objectif, i.e. quel est le return on veut avoir. Par exemple 
•	On peut économiser 500 dollars par mois
•	On veut 1,000,000 au bout de 40 ans
•	Quel est le taux d’intérêt ?
•	Réponse : 0.5%
•	Garder à l’idée que plus le return est élevé plus le risque est grand
•	Pour un return donné, est toujours associé un niveau de risque (ou une standard deviation)
Le tableau ci-dessous donne une idée du retour et du risque des types d’assets possible
 

Diversification
Bon là l’idée est simple quand on diversifie on réduit le risque. Pour étuider la diversification, il faut utiliser les corrélations, utiliser des assets décorélés pour avoir un portfolio diversifié. C’est pourquoi on veut un portfolio qui aille dans tout les sens des assets possibles. Le tableau ci-dessous expose les différentes corrélations existantes entre les types d’assets possibles
 

Efficient Portfolio
Alors si on ne considère que les assets. Le portfolio dit efficient est celui qui pour le return désiré offre la standard deviation minimum. Si on n’a pas de return objectif alors ca dépend de notre risque tolérance et du risque de ruine

Utility
Fonction qui représente le lien entre le return et le risque. C’est la fonction qu’on cherche à maximiser pour designer notre portfolio.

Robo Advisor
Un algorithme qui va lui-même définir un portfolio efficient en fonction de critères d’entrée comme le return désiré et le risque toléré. Le portfolio trouvé est appelé Exchange Traded Funds ETFs.
•	C’est une sorte de FinTech dans la mesure où c’est défini de manière mathématique
•	Ca peut contenir plusieurs entités d’une même asset
•	Les frais sont généralement petit car peu de management sont nécessaires
•	S&P 500
o	500 plus gros stocks des US
o	Chaque stock est associé à un poids égal au ratio Company market Capitalization / market Capitalization des 500 companies
o	Market Capitalization  = Price per Share * shares outstanding
•	Ok, donc comme on ne peut jamais acheter une fraction d’une action sur le stock market, il est difficile pour un investisseur d’avoir un portefeuille diversifié, c’est là que rentre dans le game les ETFs grace auxquels tu peux posséder une fraction de l’index

ETFs
Pour créer un ETF il faut être un participant autorisé , c’est en gros les banques et les fonds d’investissements. Puis il livre des actions ou des dollars en masse à un trust () qui en retour lui envoie des petites fractions de ce qu’il a acheté. Ces petites actions (des millions) représentent les stocks ETFs. Le participant peut alors soit les garder en guise d’investissement, soit les vendre comme n’importe quelle autre action. Le gros intérêt sont les frais vraiment ridicules Entre 0.03 et 0.3% contrairement aux fees classiques managed funds (1-2%). La taille des fees dépend apparemment du volume de liquidité en question (les stocks dans les emerging markets sont apparemment plus difficile d’accès et donc les fees dans cette catégorie sont plus chers) Voir ci-dessous : 

 

Les impacts des fees sur la performance

•	Financial Advisor Fees : 1.0-1.5% / an
•	Mutual actively manage funds : 0.75%-1%
•	Total Fees : 2.0 - 2.75% de fees
•	L’impact des fees sur le long terme est énorme comme le montre le graph en dessous sur 400 mois
•	En conséquence de quoi les robo advisor font leur apparition

 
Types de Robot Advisor

•	Hybrid : presque entièrement automatisé, parfois une intervention humaine. Les fees sont évidemment plus élevés
•	Pure : tout est automatisé. Des fees très faibles. Un minimum de volume très bas pour débuter. Les exemples de pure robo advisors sont WealthFront et Betterment

Mécanisme
•	Un questionnaire est soumis au potentiel user afin d’estimer son risque qui est d’après la plupart des modèles une moyenne entre le risque objectif (age, salaire, assets) et le risque subjectif (psychologie du user)
•	Choix du portfolio sur la frontière markowitz, i.e. les portfolio qui ont le return le plus élevé selon un risque fixe. Cette frontière efficiente est calculée selon le Modèle Black Litterman chez Wealthfront par exemple.
 
Le tableau ci-dessous est un example de proposition de Wealthfront en fonction du questionnaire soumis
 

Les avantages des Robo
•	Fees faibles (0.1% vers 1% pour les conseillers classiques)
•	Confort (rien à faire en vérité, pas de rendez-vous physique)
•	Process régulièrement des data nombreuses et complexes afin d’estimer les portfolio optimaux (difficilement réalisables par un être humain) :
o	Les return
o	Les variance
o	Les corrélations
•	Recalibrage régulier du portfolio pour coller aux tendances les plus intéressantes
•	Apparamment tu peux réduire tes impôts avec le mécanisme de la Tax Loss Harvesting expliqué ci-dessous (le principe est de retarder le paiement d’un impôts à un taux plus avantageux) : 
 


Les fonds d’investissement sont-ils bons ?
On mesure la performance d’un manager de funds à la plus value qu’il rapporte par rapport à une valeur seuil dépendant des paramètres suivants :
•	Le treasure bill (en gros ce qu’on est censé gagner sans prendre aucun risques)
•	La valeur des benchmarks (en gros, les indices les plus classiques comme le S&P 500)
•	Le risque qu’on est prêt à prendre
Il s’avère qu’il n’y a que très peu de fonds d’investissements qui font mieux que le benchmark S&P 500 sur 2 ans et encore moins sur 4 ans. Les chercheurs sont même incapables de se mettre d’accord pour dire que les fonds d’investissement sont d’une manière générale garant d’une plus value comparé à un investissement plutôt passif.





Les signals
Il se trouve qu’il existe des multitudes de features pour caractériser une entreprises. Des chercheurs en ont isolé 500 qu’ils ont appelé « signals ». Le trick le plus simple consiste à observer le return sur une dimension d’un signal (par exemple la market capitalization) . Si une corrélation net s’observe alors on séléctionne le top X% des stocks et on les fout dans un portefeuille. Ce portefeuille le plus souvent fait mieux que le S&P 500. On peut également faire la même expérience avec deux signals et ainsi de suite.

Recherche des signals
En gros, on modélise à l’aide d’une régression linéaire le rendement d’un stock à la date t via les signals à la date t-1. Bon alors, ça a forcément des limitations puisqu’il y a une densité d’informations faibles et que le rendement n’est sûrement pas lié linéairement aux signals. C’est sûrement plus compliqué que ça. Bon y’a un speech un peu baclé sur les réseaux de neurones. Vu que je suis un master aucun souci bwaa. 

Smart Beta ETFS
Ce sont tout simlement des ETFs, i.e. des portefeuilles d’actions, construit grâce aux signals. On distingue deux types de smart ETFS :
•	Absolute  : les stocks sont d’abord triés selon un ou plusieurs signals, on prend les meilleurs et ils constituent l’ETF, le top 20% en général. Les stocks sélectionnés sont pondérés par leur capitalisation
•	Tilt : tout les stocks associés à un même index (par exemple le S&P 500) sont inclus dans le portefeuille, seulement les poids associés à chacun d’eux sont différents. C’est un calcul sacrément bricorama qui permet de construire ce genre de ETFs	

AI and Finance
Bon alors, ça marche pas tant que ça pour ce qu’on sait de ce qui sort publiquement même si on suppose que les plus grosses banques ont des résultats plutôt bons mais qu’ils préfèrent garder secret. Un inconvénient majeur de l’IA c’est qu’il est difficilement interprétable par les êtres humains et que de ce fait, ils ne lui font pas confiance. 
