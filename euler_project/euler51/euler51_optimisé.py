from itertools import permutations
from time import time 

start_time = time()

def number_convertor(l):
    number = 0
    lenght = len(l)
    for i in range(lenght):
        number += 10**(lenght-(i+1)) * int(l[i])
    return number

def ératosthène(n):
    primes = [False, False] + [True for _ in range(2,n+1)]
    for i in range (int((n+1)**(1/2)) + 1):
        if primes[i]:
            multiple = 2 * i
            while multiple < n:
                primes[multiple] = False
                multiple += i
    return [i for i in range(n) if primes[i]]


list_list_list_paterns = [[],[]]

for length in range(2,8):
    list_list_list_paterns.append([])
    for i in range(1, length):
        str_guinea_pig = ""
        guinea_pig = ["*" if j<i else "-" for j in range(length)]
        for element in guinea_pig:
            str_guinea_pig += element
        List_paterns = list(set(permutations(str_guinea_pig)))
        list_list_list_paterns[length].append(List_paterns)


set_primes = set(ératosthène(1000000))

def prime_digit_replacements():
    counter_max = 0
    Number = 11 

    while counter_max != 8:
        if Number % 5 != 0:

            if Number % 10000 == 1:
                print(Number)

            number = str(Number)
            len_number = len(number)

            for type_patern in range(len_number - 1):
                list_paterns = list_list_list_paterns[len_number][type_patern]

                #list_list_list_paterns est une liste contenant les listes contenants toutes les listes de patern possible pour une longueur de nombre donnée.
                #list_paterns est une liste des combinaisons possibles des chiffres à remplacer dans le nombre d'origine (ici Nombre), pour un certain nombre de chiffres à remplacer(type_patern + 1).
                #les "*" sont les chiffres à remplacer, les "-" restent tels qu'ils sont dans le nombre d'origine.
                #patern (ci-dessous) est donc l'une de ces combinaisons pour laquelle on remplace tous les "*" par les chiffres de 0 à 9.

                for patern in list_paterns:
                    #print("yes")
                    anti_counter = 0
                    counter = 0
                    smallest_number_transformed = 0
                    test = False
                    for i in range(10):
                        number_transformed = number_convertor([i if patern[j] == "*" else int(number[j]) for j in range(len_number)])
                        if number_transformed in set_primes and len(str(number_transformed)) == len_number:
                            counter += 1
                            if not test:
                                smallest_number_transformed = number_transformed
                                test = True
                        else:
                            anti_counter += 1
                        if anti_counter == 3:
                            break
                    if counter >= 8:
                        return smallest_number_transformed
        Number += 2


print("solution:", prime_digit_replacements())
print("temps:", time() - start_time)


"""
SOLUTION:
solution: 121313
trouvé à partir de: 120303
"""