

class Compte :

    id_operation = 0

    def __init__(self, numero_compte,client, date_de_creation, solde) :
        self.numero_compte = numero_compte
        self.client = client
        self.date_de_creation = date_de_creation
        self.solde = solde
        self.liste_operation = {}

    
    def affiche_info_compte(self):
        print(f"Nom = {self.client.nom}, Numero = {self.numero_compte} , Solde = {self.solde} ")

    def afficher_liste_operation(self) :
        for info in self.liste_operation.values() :
             print(f"{info.libelle} - Date : {info.date_operation}, montant : {info.montant} , numero : {info.numero_operation}")

