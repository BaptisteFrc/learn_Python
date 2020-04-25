a = 1
b = 1
resultat = 2
while len(str(b)) < 1000:
    a, b = b, a+b
    resultat += 1
print(resultat)