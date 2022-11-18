import subprocess
from serveur import Serveur
from Utils import utils


# Cette fonction construis ton arborescence   
def buildFileTree():
    process = subprocess.run(["pip","install","-e","."])
    if process.returncode == 0:
        print("Installation des dépendances complétées.")
        success = True
    else:
        print("Une erreur s'est produite lors de l'installation des dépendances.")
        success = False
    return success

def main():
    if buildFileTree():
        print('serveur en cours de démarrage')
        Serveur.lancer(utils.HOTE, utils.PORT)
        return 0

if __name__== '__main__':
    quit(main())