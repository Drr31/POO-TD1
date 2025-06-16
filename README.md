# 💸 Gestion Bancaire – Projet Python POO (ISTY / IATIC3)

Ce projet a été réalisé dans le cadre du TD3 de Programmation Orientée Objet (Python) à l'ISTY. Il simule une application bancaire permettant la gestion de comptes et d'opérations pour plusieurs clients.

## 🧠 Objectif du projet

Développer une application en Python respectant les principes de la programmation orientée objet, avec une interface graphique intuitive et une fonctionnalité d’export des relevés en PDF.

## ⚙️ Fonctionnalités principales

- Création de comptes bancaires (courants et livrets)
- Association de comptes à des clients (nom, adresse)
- Dépôts et retraits d’argent
- Virements entre comptes
- Crédit automatique d’intérêts pour les comptes sur livret
- Génération de relevés mensuels PDF
- Historique des opérations

## 🖥️ Interface utilisateur

L'application permet :

- L’identification du client (numéro de compte + mot de passe)
- La consultation du solde et de l’historique des 10 dernières opérations du mois en cours
- L’export d’un relevé de compte en format PDF

## 📌 Contraintes

- Les montants sont exprimés en euros (entiers)
- Aucun compte ne peut avoir un solde négatif
- Les intérêts sont calculés avec : `montant = solde * taux / 100`

## 🛠️ Technologies utilisées

- Python 3
- Interface graphique : `tkinter`
- Génération PDF : `fpdf2` *(ou `reportlab`)*
- Modules standards : `datetime`, `uuid`, `os`

## 👥  Dev@Drr31
