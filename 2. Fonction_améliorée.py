import sys
import random
chiffreHasard = random.randint(1, 5)
print(chiffreHasard)
MAX = 1
MIN = 5
# Fonction 1
def demander_saisie_nombre(invite):
    while True:
        saisie = input(invite)
        try:
            saisie = int(saisie)
        except ValueError as erreurDeValeur:
            print("Veuillez saisir une valeur numérique entre 1 et 5",
                  file=sys.stderr)
            sys.exit()
        else:
            if MIN <= saisie <= MAX:
                break
        return saisie

# Fonction 2
def demander_nombre_borne(invite, minimum=MIN, maximum=MAX):
    while True:
        invite = "{} entre les valeurs {} et {} : ".format(invite, minimum, maximum)
        saisie = demander_nombre_borne(invite)
        if minimum <= saisie <= maximum:
            return saisie

# PARTIE 1
minimum = maximum = 0
while True:
    minimum = demander_saisie_nombre("Choisissez le minimum : ")
    maximum = demander_saisie_nombre("Choisissez le maximum : ")
    if maximum > minimum:
        break

nombre = demander_saisie_nombre("Devinez le nombre", minimum, maximum)

# Application de la méthode
while True:
    essai = demander_saisie_nombre_borne("Devinez le nombre", minimum, maximum)
    if essai < chiffreHasard and 1 <= essai <= 5:
        print("Trop petit")
    elif essai > chiffreHasard and 1 <= essai <= 5:
        print("Trop grand")
    elif essai == chiffreHasard and 1 <= essai <= 5:
        print("Gagné !")
        break
    else:
        print("Ressaisissez un nombre entre 1 et 5 : ")
