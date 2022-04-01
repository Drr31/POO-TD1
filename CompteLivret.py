
from Compte import Compte

class CompteLivret(Compte) :

    def __init__(self, numero_compte,client, date_de_creation, solde, taux_interet) :
       
        super().__init__(numero_compte, client, date_de_creation, solde)
        self.taux_interet = taux_interet

    def calcul_taux_interet(self) :
        return (self.solde*self.taux_interet)/100

    


