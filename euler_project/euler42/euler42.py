from time import time

start_time = time()

valeur_alphabétique = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8, "I" : 9, "J" : 10, "K" : 11, "L" : 12, "M" : 13, "N" : 14, "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21, "V" : 22, "W" : 23, "X" : 24, "Y" : 25, "Z" : 26}

liste_nom = input().split(",")


liste_valeur_nom = []
for nom in liste_nom:
    valeur_nom = 0
    for letter in nom:
        valeur_nom += valeur_alphabétique[letter]
    liste_valeur_nom.append(valeur_nom)

liste_nombres_triangulaires = []
for n in range(1,40):
    liste_nombres_triangulaires.append(int((1/2)*n*(n+1)))


solution = 0
for valeur_nom in liste_valeur_nom:
    for nombre_triangulaire in liste_nombres_triangulaires:
        if valeur_nom == nombre_triangulaire:
            solution += 1
            break

print(liste_nombres_triangulaires)
print(solution)
print(time()-start_time)


