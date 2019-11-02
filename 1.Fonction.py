import sys
import random
chiffreHasard = random.randint(1, 5)
print(chiffreHasard)
MAX = 1
MIN = 5
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

# Application de la méthode
while True:
    essai = demander_saisie_nombre("Trouvez le chiffre entre 1 et 5 : ")
    if essai < chiffreHasard and 1 <= essai <= 5:
        print("Trop petit")
    elif essai > chiffreHasard and 1 <= essai <= 5:
        print("Trop grand")
    elif essai == chiffreHasard and 1 <= essai <= 5:
        print("Gagné !")
        break
    else:
        print("Ressaisissez un nombre entre 1 et 5 : ")
