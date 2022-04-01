import datetime


class Banque:
    def __init__(self, nom = "none", swift = "none"):
        self.nom = nom
        self.swift = swift



class Client:
    clients = {}
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

    def Ouvrircompte(self, Numero):
        f = open("Database.txt", "a")
        f.write("\n")


    def debiter(self, amount, Numero):
        if self.compte['solde'] >= amount:
            self.compte['holdings'] -= amount
            print("\nle montant de retrait : {} .".format(amount))
        else:
            print("\nPas assez d'argent!")

    def crediter(self, Solde):
        Solde += self.somme
        print("\nnew montant : {} ".format(Solde))

   
    def EffectVir(self,dist,libelle):
        self.dist=
        pass
        
        

#from Operations import *
class Compte(Operations):
    def __init__(self, Numero = None, Solde = 0):
        self.Numero = Numero
        self.Solde = Solde

