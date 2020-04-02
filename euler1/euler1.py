somme = 0
for i in [i for i in range(1000) if i % 3 == 0 or i % 5 ==0]:
    somme += i
print(somme)

list1 = [i for i in range(1000) if i % 3 == 0 or i % 5 ==0]
print(list1)