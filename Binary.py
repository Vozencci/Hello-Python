# Disclaimer: Ce code a été tapé par Vozencci aka Sarmeegan.
# Tout droit réservé, code Open Source.

# Ce code est une traduction en python de comment ecrire un nombre en base 10 en base 2 (la conversion binaire).
# Idée: Faire une succession de division euclidienne par 2 du nombre n choisi, puis lorsque la division euclidienne donne le chiffre 1 comme quotient: diviser une derniere fois ce quotient pour obtenir 1 comme reste. Finalement, on colle les reste ensembles en partant du reste situé vers la dernière division. (Exemple: 100101010)
# Amusez-vous bien !



def Binaire(n):
    b=str()
    while not(n//2==1):
        r=n%2
        b=str(r)+b
        n=n//2
    b='10'+b
    return b
