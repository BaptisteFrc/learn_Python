from math import sqrt

def list_primes_eratosthene(n):
    print("entering primes...")
    primes = [False, False] + [True for _ in range(2, n+1)] 
    for i in range(int(sqrt(n+1))):
        if i % 10000 == 0:
            print("primes turn ", i, "/", n)
        if primes[i]: 
            indice = 2*i # i = 2; Faux pour 2*2, 3*2 = 2*2 + 2, 4*2 = 3*2 + 2, 5*2, etc... 
            while indice < n:
                primes[indice] = False
                indice += i # indice = indice + i
    return [i for i in range(n) if primes[i]]

def counter_example(M):
    primes = list_primes_eratosthene(M)
    print("primes done !")
    squares = [i*i for i in range(int(sqrt(M)))]
    print("squares done !")
    print("entering loop...")
    for i in range(3, M+1, 2):
        if i % 10000 == 0:
            print("turn ", i, "/", M)
        counter_ex = True
        for prime in primes:
            for square in squares:
                if i == prime + 2*square:
                    counter_ex = False
                    break   
                elif i < prime + 2*square:
                    break
            if i < prime or not counter_ex: 
                break
        if counter_ex:
            return i
    return 0

#print("answer :", counter_example(10000000))

