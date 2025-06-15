Projet Python - Gestion bancaire simplifiée

En Cadre de ma formation ISTY / IATIC3 / POO / Python / TD3

Ce projet a pour but d'analyser, concevoir et implémenter partiellement un système informatique de gestion bancaire, dans un cadre pédagogique, en utilisant Python (Programmation Orientée Objet) et une interface graphique.

📅 Objectif pédagogique

Réaliser un projet complet intégrant les compétences suivantes :

Conception UML (diagramme de classes)

Programmation orientée objet avec Python

Mise en oeuvre d'une interface graphique

Génération de documents PDF

🔹 Fonctionnalités

Gérer un ensemble de clients (nom, adresse)

Gérer un ensemble de comptes (courant ou sur livret)

Réaliser les opérations suivantes :

Ouverture de compte

Crédit et débit d’un compte

Virement d’un compte A vers un compte B

Calcul et crédit des intérêts (compte sur livret uniquement)

Génération d’un relevé mensuel

📑 Contraintes

Les montants manipulés sont des entiers (euros).

Aucun compte ne peut avoir un solde négatif.

Les intérêts sont calculés avec la formule : solde * taux / 100.

Un client peut posséder plusieurs comptes, mais un compte appartient à un seul client.

🔹 Interface graphique

L’interface graphique permet les actions suivantes :

Identification d’un client via son numéro de compte + mot de passe

Consultation des soldes et opérations d’un compte

Affichage des 10 dernières opérations du mois courant

Export des relevés de compte en PDF

📄 Structure technique

Langage : Python 3.x

Interface GUI : tkinter (ou PyQt5 selon la version)

PDF : fpdf2 ou reportlab


🎓 Auteurs

Projet réalisé dans le cadre du TD3 de Programmation Orientée Objet (IATIC3 ISTY).

Encadrant : [Nom de l’enseignant]Réalisé par : [Ton nom ici]

📊 Avancement



📅 Dépendances

fpdf2 (PDF)

tkinter (inclus avec Python)

datetime, uuid, os

🔗 Licence

Projet à but pédagogique - Tous droits réservés ISTY Université Paris-Saclay.
