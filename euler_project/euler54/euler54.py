from time import time

start_time = time()


def counter_duplicates(List, Element):
    counter = 0
    for element in List:
        if element == Element:
            counter += 1
    return counter


def force_main(liste_type_carte, liste_couleur_carte):
    liste_force_main = []
    plusieurs_memes_cartes = False
    suite_ou_couleur = False
    paire = False
    brelan = False

    for type_carte in liste_type_carte:
        nombre_memes_cartes = counter_duplicates(liste_type_carte, type_carte)
        if nombre_memes_cartes >= 2:
            plusieurs_memes_cartes = True
        #Paire
        if nombre_memes_cartes == 2 and not paire and not brelan:
            liste_force_main.append([dico_valeur_main["Paire"], [dico_valeur_carte[type_carte]]])
            paire = True
            type_paire = type_carte
            for _ in range(nombre_memes_cartes):
                liste_type_carte.remove(type_carte)
        #Double Paire
        elif nombre_memes_cartes == 2 and paire:
            liste_force_main[0] = [dico_valeur_main["Deux Paires"], [dico_valeur_carte[type_paire], dico_valeur_carte[type_carte]]]
            for _ in range(nombre_memes_cartes):
                liste_type_carte.remove(type_carte)
        #Full (brelan trouvé en premier)
        elif nombre_memes_cartes == 2 and brelan: 
            liste_force_main[0] = [dico_valeur_main["Full"], [dico_valeur_carte[type_brelan], dico_valeur_carte[type_carte]]]
            for _ in range(nombre_memes_cartes):
                liste_type_carte.remove(type_carte)
        #Brelan
        if nombre_memes_cartes == 3 and not paire:
            liste_force_main.append([dico_valeur_main["Brelan"], [dico_valeur_carte[type_carte]]])
            brelan = True
            type_brelan = type_carte
            for _ in range(nombre_memes_cartes):
                liste_type_carte.remove(type_carte)
        #Full (paire trouvée en premier)
        elif nombre_memes_cartes == 3 and paire:
            liste_force_main[0] = [dico_valeur_main["Full"], [dico_valeur_carte[type_carte], dico_valeur_carte[type_paire]]]
            for _ in range(nombre_memes_cartes):
                liste_type_carte.remove(type_carte)
        #Carré
        if nombre_memes_cartes == 4:
            liste_force_main.append([dico_valeur_main["Carré"], [dico_valeur_carte[type_carte]]])
            for _ in range(nombre_memes_cartes):
                liste_type_carte.remove(type_carte)
    
    if not plusieurs_memes_cartes:
        liste_force_type_carte = []
        suite = False
        suite_blanche = False
        couleur = False
        for type_carte in liste_type_carte:
            liste_force_type_carte.append(dico_valeur_carte[type_carte])

        max_valeur_carte = max(liste_force_type_carte)
        min_valeur_carte = min(liste_force_type_carte)
        #Test Suite
        if max_valeur_carte - min_valeur_carte == 4:
            suite = True

        #Test Suite blanche
        if set(liste_type_carte) == set(["A", "2", "3", "4", "5"]):
            suite_blanche = True

        #Test Couleur
        if len(set(liste_couleur_carte)) == 1:
            couleur = True
            

        if suite or suite_blanche or couleur:
            suite_ou_couleur = True

            #Suite
        if suite and not couleur:
            liste_force_main.append([dico_valeur_main["Suite"], [max_valeur_carte]])   
            #Suite blanche 
        elif suite_blanche and not couleur:
            liste_force_main.append([dico_valeur_main["Suite"], [5]])
            #Couleur    
        elif couleur and not suite:    
            liste_force_main.append([dico_valeur_main["Couleur"], [max_valeur_carte]])
            #Quinte Flush
        elif couleur and suite and max_valeur_carte != 14:
            liste_force_main.append([dico_valeur_main["Quinte Flush"], [max_valeur_carte]])
            #Quinte Flush blanche
        elif couleur and suite_blanche:
            liste_force_main.append([dico_valeur_main["Quinte Flush"], [5]])
            #Quinte Flush Royale
        elif couleur and suite and max_valeur_carte == 14:
            liste_force_main.append([dico_valeur_main["Quinte Flush Royale"], [max_valeur_carte]])
            

    if not plusieurs_memes_cartes and not suite_ou_couleur:
        return [[dico_valeur_main["Carte Haute"], [0]], liste_force_type_carte]
    
    elif suite_ou_couleur:
        return liste_force_main

    elif plusieurs_memes_cartes:
        return liste_force_main + [[dico_valeur_carte[Type_carte] for Type_carte in liste_type_carte]]




dico_valeur_carte = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14}
dico_valeur_main = {"Carte Haute" : 1, "Paire" : 2, "Deux Paires" : 3, "Brelan" : 4, "Suite" : 5, "Couleur" : 6, "Full" : 7, "Carré" : 8, "Quinte Flush" : 9, "Quinte Flush Royale" : 10}

compteur_victoires_joueur1 = 0
compteur_victoires_joueur2 = 0
compteur_de_partie = 0

for _ in range(int(input())):
    compteur_de_partie += 1
    liste_mains_partie = input().split(" ")
    liste_main_joueur1 = liste_mains_partie[:5]
    liste_main_joueur2 = liste_mains_partie[5:]
    liste_type_carte_joueur1 = []
    liste_type_carte_joueur2 = []
    liste_couleur_carte_joueur1 = []
    liste_couleur_carte_joueur2 = []
    for ensemble1 in liste_main_joueur1:
        liste_ensemble1 = [element for element in ensemble1]
        liste_type_carte_joueur1.append(liste_ensemble1[0])
        liste_couleur_carte_joueur1.append(liste_ensemble1[1])
    for ensemble2 in liste_main_joueur2:
        liste_ensemble2 = [element for element in ensemble2]
        liste_type_carte_joueur2.append(liste_ensemble2[0])
        liste_couleur_carte_joueur2.append(liste_ensemble2[1])
    
    """
    print(liste_type_carte_joueur1)
    print(liste_couleur_carte_joueur1)
    print(liste_type_carte_joueur2)
    print(liste_couleur_carte_joueur2)
    """

    valeur_main_joueur1 = force_main(liste_type_carte_joueur1, liste_couleur_carte_joueur1)
    valeur_main_joueur2 = force_main(liste_type_carte_joueur2, liste_couleur_carte_joueur2)
    vainqueur = False

    if valeur_main_joueur1[0][0] > valeur_main_joueur2[0][0]:
        compteur_victoires_joueur1 += 1
        vainqueur = True
    elif valeur_main_joueur1[0][0] < valeur_main_joueur2[0][0]:
        compteur_victoires_joueur2 += 1
        vainqueur = True
    else: 
        for _ in range(len(valeur_main_joueur1[0][1])):
            valeur_carte_speciale_joueur1 = max(valeur_main_joueur1[0][1])
            valeur_carte_speciale_joueur2 = max(valeur_main_joueur2[0][1])

            valeur_main_joueur1[0][1].remove(valeur_carte_speciale_joueur1)
            valeur_main_joueur2[0][1].remove(valeur_carte_speciale_joueur2)

            if valeur_carte_speciale_joueur1 > valeur_carte_speciale_joueur2:
                compteur_victoires_joueur1 += 1
                vainqueur = True
                break
            elif valeur_carte_speciale_joueur1 < valeur_carte_speciale_joueur2:
                compteur_victoires_joueur2 += 1
                vainqueur = True
                break
    if not vainqueur: 
        for _ in range(len(valeur_main_joueur1[1])):
            valeur_carte_normale_joueur1 = max(valeur_main_joueur1[1])
            valeur_carte_normale_joueur2 = max(valeur_main_joueur2[1])

            valeur_main_joueur1[1].remove(valeur_carte_normale_joueur1)
            valeur_main_joueur2[1].remove(valeur_carte_normale_joueur2)

            if valeur_carte_normale_joueur1 > valeur_carte_normale_joueur2:
                compteur_victoires_joueur1 += 1
                break
            elif valeur_carte_normale_joueur1 < valeur_carte_normale_joueur2:
                compteur_victoires_joueur2 += 1
                break

    """
    print(valeur_main_joueur1)
    print(valeur_main_joueur2)
    print()

    print("à la partie", compteur_de_partie)
    print("le joueur 1 a gagné", compteur_victoires_joueur1, "parties")
    print("le joueur 2 a gagné", compteur_victoires_joueur2, "parties")
    print("------------------------------")
    """

print("le joueur 1 a gagné", compteur_victoires_joueur1, "fois sur les 1000 parties")
print("le joueur 2 a gagné", compteur_victoires_joueur2, "fois sur les 1000 parties")

print(time()-start_time)