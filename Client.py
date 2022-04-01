

class Client :
    
    def __init__(self, nom, prenom, login, mot_de_passe, adresse) :
        self.nom = nom 
        self.prenom = prenom
        self.login = login
        self.mot_de_passe = mot_de_passe
        self.adresse = adresse
        self.liste_compte = {}
        self.nombre_compte = 0

    def __str__(self) :
        return f"Nom : {self.nom}, Prenom : {self.prenom}, Adresse : {self.adresse} "

    def ajout_compte(self, compte) :

        self.nombre_compte += 1
        self.liste_compte[self.nombre_compte] = compte


