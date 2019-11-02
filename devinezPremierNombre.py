import sys
import random

# Définition de constantes
MIN1 = 1
MAX1 = 5

MIN2 = 6
MAX2 = 20

# Génération du nombre aléatoire
nombre = random.randint(1, 5)
print(nombre)

# Création d'une fonction de niveau 1
def saisie_nombre_niveau1(consigne, minimum, maximum):
    # On complète la consigne avec les paramètres faisant référence aux valeurs des constantes
    # correspondant au niveau joué
    consigne += " entre " + str(minimum) + " et " + str(maximum) + " : "

    while True:
        essai = input(consigne)

    # Vérification de la saisie d'une valeur numérique
        try:
            essai = int(essai)
        except ValueError as erreurDeValeur:
            print("La conversion n'a pas eu lieu... Saisissez une valeur numérique",
                  file=sys.stderr)
        else:
            # Saisie se trouve bien entre les constantes MIN1 et MAX1
            if minimum <= essai <= maximum:
                break
    return essai

# Création d'une fonction de niveau 2
def saisie_nombre_niveau2(consigne, minimum, maximum):
    # On complète la consigne avec les valeurs des constantes correspondant au niveau joué
    consigne += " entre " + str(minimum) + " et " + str(maximum) + " : "

    while True:
        essai = input(consigne)

    # Vérification de la saisie d'une valeur numérique
        try:
            essai = int(essai)
        except ValueError as erreurDeValeur:
            print("La conversion n'a pas eu lieu... Saisissez une valeur numérique",
                  file=sys.stderr)
        else:
            # Saisie se trouve bien entre les constantes MIN1 et MAX1
            if minimum <= essai <= maximum:
                break
    return essai


minimum1 = MIN1
maximum1 = MAX1

#Lancement du niveau 1
print("Essayez de trouver le nombre à deviner")
while True:
    saisie = saisie_nombre_niveau1("Niv. 1. Saisissez un chiffre", minimum1, maximum1)

    if saisie == nombre:
        print("Bravo")
        encore = input("Souhaitez-vous recommencer ou accéder au niveau supérieur ? o = oui, n = non, s = supérieur : ")
        if encore.lower() == "o":
            print("HEY ! Essayez de trouver le nombre à deviner")
            nombre = random.randint(1, 5)
            print(nombre)
            saisie
        # Lancement du niveau 2
        elif encore.lower() == "s":
            nombre2 = random.randint(6, 20)
            print(nombre2)
            while True:
                saisie2 = saisie_nombre_niveau2("Niv. 2. Saisissez un chiffre", MIN2, MAX2)
                if saisie2 == nombre2:
                    print("Bravo")
                    break
                elif saisie2 < nombre2:
                    print("trop petit")
                elif saisie2 > nombre2:
                    print("trop grand")
                else:
                    saisie_nombre_niveau2("Niv. 2. Saisissez un chiffre", MIN2, MAX2)
        elif encore.lower() == "n":
            print("Bye bye...")
            break
    elif saisie < nombre:
        print("trop petit")
    elif saisie > nombre:
        print("trop grand")
    else:
        saisie = saisie_nombre_niveau1("Niv. 1. Saisissez un chiffre", minimum1, maximum1)
