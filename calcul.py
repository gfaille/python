
continuer = True
while (continuer):
    jeu = input("tapez jouer pou jouer sinon tapez entrer pour arreter")

    if (jeu == "jouer"):

        valeur = int(input("donner un nombre :"))
        resultat = valeur + 2
        resultat = resultat * 2
        print("le resultat est :", resultat)

    else:
        continuer = False
