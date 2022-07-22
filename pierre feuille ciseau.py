from random import *

jeu = ["pierre" , "feuille" , "ciseau"]

ordinateur = jeu[randint(0 , 2)]

Pointsjoueur = 0
Pointscpu = 0

continuer = True

while(continuer) :
    joueur = input("pierre, feuille, ciseaux ? ou tapez Fin pour arrêter le jeu!\n")

    if (joueur == "Fin"):
        continuer = False
    elif(Pointsjoueur == 5):
        print("Vous avez gagner")
        continuer = False
    elif(Pointscpu == 5):
        print("Vous avez perdu")
        continuer = False
    elif(joueur == ordinateur):
        print("égalité!")
    elif(joueur == "pierre"):
        if(ordinateur == "feuille"):
            print("Perdu!", ordinateur, "recouvre", joueur)
            Pointscpu = Pointscpu + 1
        else:
            print("Gagner!", joueur, "écrase", ordinateur)
            Pointsjoueur = Pointsjoueur + 1
    elif(joueur == "feuille"):
        if(ordinateur == "ciseaux"):
            print("Perdu!", ordinateur, "coupe", joueur)
            Pointscpu = Pointscpu + 1
        else:
            print("Gagner", joueur, "recouvre", ordinateur)
            Pointsjoueur = Pointsjoueur + 1
    elif(joueur == "ciseaux"):
        if(ordinateur == "pierre"):
            print("Perdu", ordinateur, "écrase", joueur)
            Pointscpu = Pointscpu + 1
        else:
            print("Gagner!", joueur, "coupe", ordinateur)
            Pointsjoueur = Pointsjoueur + 1
    else:
        print("Votre choix n'est pas correct, vérifier l'orthographe!")

    ordinateur = jeu[randint(0 , 2)]
    print("******Tour suivant******")


print("********Points********")
print("joueur: ", Pointsjoueur)
print("ordinateur: ", Pointscpu)
input("Press ENTER to exit")
