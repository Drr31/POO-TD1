class Banque:
    def init(self, nom = "none", swift = "none"):
        self.nom = nom
        self.swift = swift



class Client:

    def init(self, idCient = None, nom = "none", adresse ="none", motDePasse=None):
        self.idClient = idCient
        self.nom = nom
        self.adresse = adresse
        self.motDePasse = motDePasse

    def identifier(self, motDePasse):
        if self.motDePasse == motDePasse:
            print("access garenteed")
        else:
            print("access denied")



class Compte:
    def __init__(self, Numero = None, Solde = 0):
        self.Numero = Numero
        self.Solde = Solde
