import datetime


class Banque:
    def __init__(self, nom = "none", swift = "none"):
        self.nom = nom
        self.swift = swift



class Client:

    def __init__(self, idCient = None, nom = "none", adresse ="none", motDePasse=None):
        self.idClient = idCient
        self.nom = nom
        self.adresse = adresse
        self.motDePasse = motDePasse

    def identifier(self, motDePasse):
        if self.motDePasse == motDePasse:
            print("access garenteed")
        else:
            print("access denied")



class Operations:
    def __init__(self,somme,libelle):
        self.somme=somme
        self.libelle=libelle
        self.date=datetime.datetime.now

    def withdraw(self, amount):
        if self.compte['solde'] >= amount:
            self.compte['holdings'] -= amount
            print()
            print("le montant de retrait : {} .".format(amount))
            self.solde()
        else:
            print()
            print("Not enough funds!")
            self.solde()

    def deposit(self, amount):
        self.compte['holdings'] += amount
        print()
        print("The sum of {} has been added to your account balance.".format(amount))
        self.solde()

    def balance(self):
        print()
        print("Votre solde actuelle : {} ".format(self.compte['solde']))
        


class Compte:
    def __init__(self, Numero = None, Solde = 0):
        self.Numero = Numero
        self.Solde = Solde

