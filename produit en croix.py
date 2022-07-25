
continuer = True
while (continuer):
    jeu = input("tapez calcul pour caluer un produit en croix sinon tapez entrer pour arreter")

    if (jeu == "calcul"):

        valeur = int(input("donner un nombre :"))
        resultat = valeur * int(input("un nombre"))
        resultat = resultat / 100
        print("le resultat est :", resultat)

    else:
        continuer = False
