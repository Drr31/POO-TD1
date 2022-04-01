
from Compte import Compte

class CompteCourant(Compte) :
    def __init__(self, numero_compte,client, date_de_creation, solde) :
        super().__init__(numero_compte, client, date_de_creation, solde)