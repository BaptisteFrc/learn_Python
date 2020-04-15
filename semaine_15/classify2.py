from random import randint


l = []
for _ in range(500000):
    l.append(randint(-10000,10000))

print("la liste est créée")

longueur_liste = len(l)
intervalle_réel = longueur_liste/1.3
intervalle = int(intervalle_réel) + 1
test = 2
while intervalle > 1 or test == 1:
    for i in range(longueur_liste):
        élément_comparé = i + intervalle
        if élément_comparé <= longueur_liste - 1:
            if l[i]>l[i + intervalle]:
                grand_élément = l[i]
                petit_élément = l[i + intervalle]
                l[i] = petit_élément
                l[i + intervalle] = grand_élément
    intervalle_réel /= 1.3
    intervalle = int(intervalle_réel) + 1
    if intervalle == 1:
        test -= 1

#l.sort()
print(l)