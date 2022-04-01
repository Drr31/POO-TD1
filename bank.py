class Banque:
    def init(self, nom = "none", swift = "none"):
        self.nom = nom
        self.swift = swift

class Client:
    def init(self, idCient = NULL, nom = "none", adresse ="none", motDePasse=NULL):
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
    def init(self, Numero = NULL, Solde = 0):
        self.Numero = Numero
        self.Solde = Solde
