valeur_alphabétique = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8, "I" : 9, "J" : 10, "K" : 11, "L" : 12, "M" : 13, "N" : 14, "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21, "V" : 22, "W" : 23, "X" : 24, "Y" : 25, "Z" : 26}

liste_noms = input().split(',')
liste_noms.sort()


valeur_liste_noms = 0
index = 0
for nom in liste_noms:
    index += 1
    valeur_lettres = 0
    for lettre in nom : 
        valeur_lettres += valeur_alphabétique[lettre]
    valeur_liste_noms += valeur_lettres * index

print(valeur_liste_noms)