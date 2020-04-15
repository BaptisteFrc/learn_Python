from math import sqrt

def transformer(n):
    l = []
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            l.append(i)
    for i in range(len(l)):
        if l[i]!=(sqrt(n)):
            l.append(int(n/l[i]))
    l.append(1)   
    return sum(l)

"""
je fais une liste contenant tous les nombres de 0 à 28123,
puis je lui enlève les nombres de 0 à 218123 pouvant être écrits sous la forme de la somme de deux nombres abondants.
"""

list_non_abundant = [True for _ in range(28124)]
for i in range(24,28124):
    if list_non_abundant[i]:
        for j in range(12,int(i/2)+1):
            k = i-j
            if transformer(j) > j and transformer(k) > k:
                list_non_abundant[i] = False
                I = 2*i
                J = i + j
                while I < 28124:
                    if list_non_abundant[I]:
                        list_non_abundant[I] = False
                    I += i
                while J < 28124:
                    if list_non_abundant[J]:
                        list_non_abundant[J] = False
                    J += j
                break

"""
je fais la somme de tous les nombres de 0 à 218123 ne pouvant pas être écrits sous la forme de la somme de deux nombres abondants.
"""
l = [i for i in range(28124) if list_non_abundant[i]]
print(sum(l))

#solution: 4179871