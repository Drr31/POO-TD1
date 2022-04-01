# En Cadre de ma formation ISTY IATIC3/POO/Python/TD3
Le but de ce TD est d'analyser, concevoir et réaliser partiellement le système
informatique d'une banque (simplifié)

Description du sujet :
Une banque gère un ensemble de comptes et un ensemble de clients. Un client
possède un nom et une adresse.
Un client peut posséder plusieurs comptes mais un compte n'appartient qu'à un
seul client.
Tout compte possède un numéro et un solde et est associé à des opérations.
Une opération peut être un débit ou un crédit, s'effectue à une date précise et
possède un libellé optionnel. Deux types de comptes sont à considérer : les
comptes courants et les comptes sur livret. Les comptes sur livret sont
rémunérés : une fois par an, des intérêts sont calculés et ajoutés au solde du
compte. Le taux d'intérêt en pourcentage d'un compte sur livret est précisé lors
de la création du compte.
Les opérations que l'on veut pouvoir réaliser sont les suivantes :
- Ouvrir un compte : Un client ouvre un compte courant ou sur livret et y
dépose une somme initiale.
- Débiter : Cette opération consiste à retirer une somme d'argent d'un
compte. Le débit doit être enregistré dans la liste des opérations
associées au compte.
- Créditer : Cette opération consiste à déposer une somme d'argent sur un
compte. Le crédit doit être enregistré dans la liste des opérations
associées au compte.
- Effectuer un virement : Dans cette opération, une somme d'argent est
transférée d'un compte source A vers un compte cible B. Le virement doit
être enregistré comme un débit au niveau de la source et comme un crédit
au niveau de la cible. Les libellés des opérations crédit et débit doivent
indiquer que ces opérations ont été réalisées dans le contexte d'un
virement.

- Créditer les intérêts : Cette opération calcule le montant des intérêts et
crédite cette somme sur le compte concerné. Le libellé de l'opération doit
indiquer ce type de crédit particulier.
- Envoyer un relevé : Cette opération permet l'envoi du relevé des
opérations du mois courant à un client donné.
Ce relevé comporte le solde ainsi que la liste chronologique des
opérations de chaque compte du client.
Remarques et contraintes
_ Les sommes sont des entiers.
_ Le solde d'un compte ne peut jamais être négatif.
_ Le montant des intérêts d'un compte sur livret est calculé par la formule
suivante : montant = solde _taux=100 (calcul en double précision puis
transformation du résultat en entier).

Questions
1. En utilisant le formalisme du diagramme de classes UML proposez un modèle
du domaine.
Vous ferez apparaître sur ce modèle les attributs et les méthodes qui vous
semblent pertinents. Afin de ne pas surcharger le modèle, ne représentez pas
les constructeurs et les méthodes get/set.
2. Traduisez le modèle précédent dans le langage python pour obtenir le
squelette des classes de l'application.
3. Ajouter une interface graphique permettant :
- - Identification de l’utilisateur avec un numéro de compte et un mot de
passe
- - Consultation d’un compte
- - Affichage de l’historique des 10 dernières transactions du mois en cours
- - Télécharger un relevé de compte en PDF
