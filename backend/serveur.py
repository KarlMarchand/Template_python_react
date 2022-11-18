from flask import Flask,request
from flask_cors import CORS, cross_origin
from werkzeug.wrappers import Response
from Controleurs.controleur_produit import Controleur_produit
from Controleurs.controleur_utilisateur import Controleur_utilisateur

class Serveur:
    __app = Flask(__name__)
    CORS(__app)
    __app.secret_key = "merciKarl"
    
    @staticmethod
    def lancer(hote, port):
        Serveur.__app.run(debug=True, host=hote, port=port)

    # Ici tu crée environ une route par fonctions que ton backend offre au frontend (pense à magix avec /api/whatever)
    # Tu peux par contre en regrouper ensemble comme dans l'exemple ici avec get, post, delete et put ensemble.
    # Pour les types tu peux allez lire la doc sur les http requests: https://developer.mozilla.org/fr/docs/Web/HTTP/Methods
    # https://flask.palletsprojects.com/en/2.2.x/quickstart/
    
    @__app.route('/api/produit', methods=["GET", "POST", "PUT", "DELETE"])
    @cross_origin()
    def ajouter_produit():
        if request.method == "POST":
            #Appeler la fonction qui crée un produit dans le controleur_produits par exemple
            dataEnvoyeParFrontend = request.form #JSON envoyé par le frontend
            dataRenvoyeParBackend = Controleur_produit.ajouter_produit(dataEnvoyeParFrontend) # Fonction dans le controleur à appeler
            return Response(dataRenvoyeParBackend, mimetype='application/json') #Reponse renvoyé au frontend, on lui indique que c'est du JSON.
        elif request.method == "GET":
            pass
        elif request.method == "PUT":
            pass
        elif request.method == "DELETE":
            pass
        else:
            return "403 FORBIDDEN" #Ici tu renvoi un message d'erreur custom mais regarde si flask a pas des méthodes plus officielles que juste une string.

    @__app.route('/api/user', methods=["POST"]) #Pas obligé de spécifier les méthodes si tu veux qu'elle passe toutes par ici, tu les spécifie si tu veux que selon la méthode ça aille sur une autre fonction.
    def connexion_user():
        dataEnvoyeParFrontend = request.form #JSON envoyé par le frontend
        dataRenvoyeParBackend = Controleur_utilisateur.connexion(dataEnvoyeParFrontend) # Fonction dans le controleur à appeler
        return Response(dataRenvoyeParBackend, mimetype='application/json') #Reponse renvoyé au frontend, on lui indique que c'est du JSON.
    
    # ...