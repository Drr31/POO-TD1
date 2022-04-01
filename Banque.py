
from Client import Client 
from Operations import Operations 
from Compte import Compte



class Banque :
    nombre = 0
    def __init__(self, nom) :
        self.liste_clients = {}

    def ajout_client(self, client) :
        
        self.liste_clients[f"client{Banque.nombre}"] =  client
        Banque.nombre += 1

    def affiche_liste_clients(self) :
        for client in self.liste_clients.values() :
            print(client)

    def authentification(self, login, mot_de_passe):

        for client in self.liste_clients.values() :
            if(client.login == login and client.mot_de_passe == mot_de_passe) :
                return client
        
        return None
    
    def recherche_client(self, nom, numero) :
        for client in self.liste_clients.values() :
            if(client.nom == nom and client.liste_compte[1].numero_compte == numero) :
                return client.compte

        return None