import sys

# Saisie d'un nombre avec son affichage dans la console
# saisie = input("Saisissez un nombre : ")
# print("Vous avez saisi :", saisie)
# Test d'un booléen
# print(3 > 2)

# #Exercice de saisie de deux valeurs et comparaison
# nombre1 = input("Saisissez un premier nombre: ")
# nombre1 = int(nombre1)
# nombre2 = int(input("Saisissez un second nombre: "))
# # Faire la comparaison
# comparaison = nombre1 < nombre2
#
# # Afficher le résultat
# print(nombre1, "<", nombre2, ":", comparaison)


# # Exercice du livre avec l'utilisation du module "sys"
# nombre1 = input("Saisissez un premier nombre: ")
# nombre2 = input("Saisissez un second nombre: ")
# try:
#     nombre1 = int(nombre1)
#     nombre2 = int(nombre2)
# except ValueError as erreurDeValeur :
#     print("La conversion de ce nombre s’est mal passée",
#           file=sys.stderr)
#     sys.exit()
#
# # Ajout d'une condition
# if nombre1 < nombre2:
#     print(nombre1, "est inférieur ou égal à", nombre2)
# elif nombre1 > nombre2:
#     print(nombre1, "est supérieur ou égal à", nombre2)
# else:
#     print(nombre1, "est égal à", nombre2)
#
# # Faire la comparaison
# if 0 < nombre1 < 10:
#     print("Par ailleurs, le nombre :", nombre1, "est bien compris entre 0 et 10")

# Redemander la saisie si le numéro saisi n'est pas compris entre 0 et 9
# nombre = input("Saisissez un numéro entre 0 et 9")
# try:
#     nombre = int(nombre)
# except:
#     nombre = 0
#
# while not 0 <= nombre <= 9:
#     # Le nombre n'est pas valide, donc on redemande la saisie valide
#     nombre = input("Ressaisissez un numéro entre 0 et 9")
#
#     try:
#         nombre = int(nombre)
#     except:
#         nombre = 0
# print("On est certain que", nombre,
#       "est un nombre et est compris entre 0 et 9 inclus.")

# La boucle infinie
while True:
    # On entre dans une boucle infinie

    # On demande la saisie d’un nombre
    nombre = input("Saisissez un nombre entre 1 et 10: ")
    try:
        nombre = int(nombre)
    except:
        pass
    else:
        # Faire la comparaison
        if 1 <= nombre <= 10:
            # On a ce que l’on veut, on quitte la boucle
            break

print("On est certain que", nombre,
      "est un nombre et est compris entre 1 et 10 inclus")

