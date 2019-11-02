import sys
import random

while True:
    yourWeight = input('What is your weight ? ')
    conversion = input('Did you type this in (L)bs or (K)g : ')

    # Vérification de la saisie d'une valeur numérique
    try:
        yourWeight = int(yourWeight)
    except ValueError as erreurDeValeur:
        print("La conversion n'a pas eu lieu...",
              file=sys.stderr)
    else:
        if conversion == 'l' or conversion == "L":
            print(round(yourWeight / 2.205))
        elif conversion == "k" or conversion == "K":
            print(float(yourWeight) * 2.205)
        else:
            print(int(input('What is your weight ?')))