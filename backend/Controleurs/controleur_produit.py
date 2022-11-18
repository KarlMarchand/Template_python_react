import json
# from Dao.whatever import whaveter requêtes/fonction

class Controleur_produit:   
    # Tu peux utiliser des classes et instancier les controleurs à la place mais c'est pas nécessaires dans un REST API.
    # Tes fonctions s'attendent à X, savent ce qu'elles ont à faire et doivent retourner Y. Elles n'ont pas à connaitre le contexte dans lequel la vue l'utilise.
    @staticmethod
    def ajouter_produit(dataEnvoyeParFrontend):
        #Fais tes trucs et retourne les données au frontend
        return json.dumps("Ceci est un succès")