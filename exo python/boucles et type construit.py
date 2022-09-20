nbUser = int(input("Entrez un Nombre"))

for i in range(1, nbUser + 1, 1) :
    print(i*"#")

def somme (liste) :
    resultat = 0
    for i in liste:
        resultat = resultat + i
    return resultat
print(somme(liste = [5, 26, 30]))

def moyenne (liste) :
    resultat = 0
    for elt in liste:
        resultat = resultat + elt
    return resultat / len(liste)
print(moyenne(liste = [55, 26, 30]))

def afficher_nombre (nb) :

    for i in range(1, 101) :
        if i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Fuzz")
        else :
            print(i)

print(afficher_nombre(1))

def liste_afficher (liste) :
    print(liste)
    l = []
    for i in liste :
        l.insert(0, i)
    return l
print(liste_afficher(liste = [12, 487, "test"]))


mot = {
    "rpg": "Rôle Player Game",
    "mmorpg": "Massively Multiplayer Online Rôle Player Game",
    "fps": "First Person Shooter",
    "tps": "Third Person Shooter"
}

print(mot.get(input("Entrez un mot ")))