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

list_primes = ératosthène(10000)
set_primes = set(list_primes)

def primes_arithmetic_sequences():
    for primes in list_primes:
        if primes > 1487:
            list_permutated_primes = list(permutations(str(primes)))
            for permutated_primes1 in list_permutated_primes:
                permutated_primes1 = number_convertor(permutated_primes1)
                if permutated_primes1 in set_primes and permutated_primes1 != primes and permutated_primes1 >= 1000:
                    for permutated_primes2 in list_permutated_primes:
                        permutated_primes2 = number_convertor(permutated_primes2)
                        if permutated_primes2 in set_primes and permutated_primes2 != primes and permutated_primes2 >= 1000 and permutated_primes2 - permutated_primes1 == permutated_primes1 - primes:
                            return [primes, permutated_primes1, permutated_primes2]


solution = primes_arithmetic_sequences()
solution.sort()
concatenated_number = ""
for number in solution:
    concatenated_number += str(number)

print(concatenated_number)
print(time() - start_time)

#296962999629
#296962999629