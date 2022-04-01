
from Compte import Compte
from CompteCourant import CompteCourant
from CompteLivret import CompteLivret


class Operations :

    def __init__(self, date_operation, montant, numero_operation, compte= None, libelle = "") :
        self.date_operation = date_operation
        self.montant = montant
        self. numero_operation = numero_operation
        self.compte = compte
        self.libelle = libelle

    def debiter_compte(self) :

        if self.compte !=None :
            Compte.id_operation += 1 
            self.compte.solde -= self.montant
            self.compte.liste_operation[f" op{Compte.id_operation}"] = Operations(self.date_operation, -self.montant, self.numero_operation, self.libelle)

    def crediter_compte(self) :

        if self.compte !=None :
            Compte.id_operation += 1 
            self.compte.solde += self.montant
            self.compte.liste_operation[f" op{Compte.id_operation}"] = Operations(self.date_operation, +self.montant, self.numero_operation, libelle = self.libelle)


    def virement(self, compte_credite) :

        #compte débité
        self.debiter_compte()

        #compte crédité
        operation_compte_credite = Operations(self.date_operation, self.montant, self.numero_operation, compte = compte_credite, libelle = "Virement")
        operation_compte_credite.crediter_compte()


    @classmethod
    def ouvrir_compte(cls, solde, client, date_de_creation, type_compte= "courant"):
        
        if type_compte == "courant" :
            compte_creer = CompteCourant(1, client, date_de_creation, solde)
        
        else :
            compte_creer =  CompteLivret(1, client, date_de_creation, solde, 0.2)
        
        return compte_creer

