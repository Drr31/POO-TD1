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
        


class Compte:
    def __init__(self, Numero = None, Solde = 0):
        self.Numero = Numero
        self.Solde = Solde

