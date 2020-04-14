from random import randint


def random_list(s,m):
    l = []
    for _ in range(randint(0,s)):
        l.append(randint(0,m))
    return l


def list_calculator(s,m):
    l_1 = random_list(s,m)
    l_2 = random_list(s,m)
    l = []
    for _ in range(m+1):
        l.append(False)

    for i in range(len(l_1)):
        for j in range(len(l_2)):
            if l_1[i] == l_2[j]:
                if not l[l_1[i]]: 
                    l[l_1[i]] = True

    listas = []
    for k in range(m+1):
        if l[k]:
            listas.append(k)
    return listas,l_1,l_2

print(list_calculator(10,10))