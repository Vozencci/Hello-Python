# Disclaimer: Ce code a été tapé par Vozencci aka Sarmeegan.
# Tout droit réservé, code Open Source.

# C'est un code (simplifié ici) permettant d'acheter un article présent dans le distributeur de snacks et de boissons.
# Remarque: Le distributeur ne propose 9 articles différents.
# Remarque: Chaque article est affect par un chiffre type entier naturel.

# Ce code est présent sur mon Github et n'hésitez pas à aller faire un tour: << https://github.com/Vozencci/hello-world >>
# Amusez-vous bien !



print("Bonjour! Selectionner l'article voulu en tapant un seul chiffre allant de 1 à 9:")
time.sleep(2)
print("Attention: Seuls les pièces de 1 et 2 Euros sont acceptés.")


n = input() #remarque: Ici n est de type "str".

time.sleep(2)

if float(n) < 1 or float(n) > 9 or len(str(n)) > 1:
    print("Erreur, vous n'avez pas selectionnez un chiffre entre 1 et 9. Veuillez recommencer s'il vout plaît.")


elif int(n) == 1:
    print("Kinder Bueno, excellent choix !")
    time.sleep(2)
    print("Insérez 2 Euros s'il vout plaît.")
    x = input()
    time.sleep(2)

    if int(x) == 0:
        print("Erreur, montant inssufisant. Au revoir !")

    elif int(x) > 2:
        print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")

    elif int(x) == 2:
        print("Restant à payer: " + str(2 - int(x)) + " Euros.")
        time.sleep(2)
        print("Transaction terminée !")
        time.sleep(2)
        print("Veuillez patientez, l'article vous parviendra sous peu...")
        time.sleep(10)
        print("L'article vous est arrivé.")
        time.sleep(2)
        print("Merci et au revoir !")

    else:
        print("Restant à payer: " + str(2 - int(x)) + " Euros.")
        x = 2 - int(x)
        y = input()

        if int(y) == int(x) and len(str(y)) == 1:
            print("Restant à payer: " + str(int(x) - int(y)) + " Euros.")
            time.sleep(2)
            print("Transaction terminée !")
            time.sleep(2)
            print("Veuillez patientez, l'article vous parviendra sous peu...")
            time.sleep(10)
            print("L'article vous est arrivé.")
            time.sleep(2)
            print("Merci et au revoir !")

        else:
            print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")


elif int(n) == 2:
    print("Twix, excellent choix !")
    time.sleep(2)
    print("Insérez 2 Euros s'il vout plaît.")
    x = input()
    time.sleep(2)

    if int(x) == 0:
        print("Erreur, montant inssufisant. Au revoir !")

    elif int(x) > 2:
        print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")

    elif int(x) == 2:
        print("Restant à payer: " + str(2 - int(x)) + " Euros.")
        time.sleep(2)
        print("Transaction terminée !")
        time.sleep(2)
        print("Veuillez patientez, l'article vous parviendra sous peu...")
        time.sleep(10)
        print("L'article vous est arrivé.")
        time.sleep(2)
        print("Merci et au revoir !")

    else:
        print("Restant à payer: " + str(2 - int(x)) + " Euros.")
        x = 2 - int(x)
        y = input()

        if int(y) == int(x) and len(str(y)) == 1:
            print("Restant à payer: " + str(int(x) - int(y)) + " Euros.")
            time.sleep(2)
            print("Transaction terminée !")
            time.sleep(2)
            print("Veuillez patientez, l'article vous parviendra sous peu...")
            time.sleep(10)
            print("L'article vous est arrivé.")
            time.sleep(2)
            print("Merci et au revoir !")

        else:
            print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")


elif int(n) == 3:
    print("Madeleine LU, excellent choix !")
    time.sleep(2)
    print("Insérez 1 Euros s'il vout plaît.")
    x = input()
    time.sleep(2)

    if int(x) == 0:
        print("Erreur, montant inssufisant. Au revoir !")

    elif int(x) > 1:
        print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")

    elif int(x) == 1:
        print("Restant à payer: " + str(1 - int(x)) + " Euros.")
        time.sleep(2)
        print("Transaction terminée !")
        time.sleep(2)
        print("Veuillez patientez, l'article vous parviendra sous peu...")
        time.sleep(10)
        print("L'article vous est arrivé.")
        time.sleep(2)
        print("Merci et au revoir !")


elif int(n) == 4:
    print("Mentos Menthe, excellent choix !")
    time.sleep(2)
    print("Insérez 1 Euros s'il vout plaît.")
    x = input()
    time.sleep(2)

    if int(x) == 0:
        print("Erreur, montant inssufisant. Au revoir !")

    elif int(x) > 1:
        print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")

    elif int(x) == 1:
        print("Restant à payer: " + str(1 - int(x)) + " Euros.")
        time.sleep(2)
        print("Transaction terminée !")
        time.sleep(2)
        print("Veuillez patientez, l'article vous parviendra sous peu...")
        time.sleep(10)
        print("L'article vous est arrivé.")
        time.sleep(2)
        print("Merci et au revoir !")


elif int(n) == 5:
    print("Granola chocolat, excellent choix !")
    time.sleep(2)
    print("Insérez 1 Euros s'il vout plaît.")
    x = input()
    time.sleep(2)

    if int(x) == 0:
        print("Erreur, montant inssufisant. Au revoir !")

    elif int(x) > 1:
        print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")

    elif int(x) == 1:
        print("Restant à payer: " + str(1 - int(x)) + " Euros.")
        time.sleep(2)
        print("Transaction terminée !")
        time.sleep(2)
        print("Veuillez patientez, l'article vous parviendra sous peu...")
        time.sleep(10)
        print("L'article vous est arrivé.")
        time.sleep(2)
        print("Merci et au revoir !")


elif int(n) == 6:
    print("Coca Cola, excellent choix !")
    time.sleep(2)
    print("Insérez 1 Euros s'il vout plaît.")
    x = input()
    time.sleep(2)

    if int(x) == 0:
        print("Erreur, montant inssufisant. Au revoir !")

    elif int(x) > 1:
        print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")

    elif int(x) == 1:
        print("Restant à payer: " + str(1 - int(x)) + " Euros.")
        time.sleep(2)
        print("Transaction terminée !")
        time.sleep(2)
        print("Veuillez patientez, l'article vous parviendra sous peu...")
        time.sleep(10)
        print("L'article vous est arrivé.")
        time.sleep(2)
        print("Merci et au revoir !")


elif int(n) == 7:
    print("Fanta, excellent choix !")
    time.sleep(2)
    print("Insérez 1 Euros s'il vout plaît.")
    x = input()
    time.sleep(2)

    if int(x) == 0:
        print("Erreur, montant inssufisant. Au revoir !")

    elif int(x) > 1:
        print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")

    elif int(x) == 1:
        print("Restant à payer: " + str(1 - int(x)) + " Euros.")
        time.sleep(2)
        print("Transaction terminée !")
        time.sleep(2)
        print("Veuillez patientez, l'article vous parviendra sous peu...")
        time.sleep(10)
        print("L'article vous est arrivé.")
        time.sleep(2)
        print("Merci et au revoir !")


elif int(n) == 8:
    print("Sprite, excellent choix !")
    time.sleep(2)
    print("Insérez 1 Euros s'il vout plaît.")
    x = input()
    time.sleep(2)

    if int(x) == 0:
        print("Erreur, montant inssufisant. Au revoir !")

    elif int(x) > 1:
        print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")

    elif int(x) == 1:
        print("Restant à payer: " + str(1 - int(x)) + " Euros.")
        time.sleep(2)
        print("Transaction terminée !")
        time.sleep(2)
        print("Veuillez patientez, l'article vous parviendra sous peu...")
        time.sleep(10)
        print("L'article vous est arrivé.")
        time.sleep(2)
        print("Merci et au revoir !")


elif int(n) == 9:
    print("BLOXXY COLA BABY, Wohooo super méga choix !!!")
    time.sleep(2)
    print("Insérez 1 Euros s'il vout plaît.'")
    x = input()
    time.sleep(2)

    if int(x) == 0:
        print("Erreur, montant inssufisant. Au revoir !")

    elif int(x) > 1:
        print("Erreur, montant non adapté. Récupérez vos pièces et veuillez recommencez s'il vout plaît.")

    elif int(x) == 1:
        print("Restant à payer: " + str(1 - int(x)) + " Euros.")
        time.sleep(2)
        print("Transaction terminée !")
        time.sleep(2)
        print("Veuillez patientez, l'article vous parviendra sous peu...")
        time.sleep(10)
        print("MDR TU AS REVE OU QUOI ?!")
        time.sleep(2)
        print("ERROR 404, Machine non opérationnel...")