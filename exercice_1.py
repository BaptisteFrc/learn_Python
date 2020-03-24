from math import sqrt

def list_primes(n):
    list_primes = []
    for i in range(2,n+1):
        a = False
        for j in range(2,int((sqrt(abs(i))+2))):
            if i != j:
                if i % j == 0:
                    a = True
                    break
        if a == False:
            if n != i: 
                list_primes.append(i)
    return list_primes

n = 1001
a = 0
while n != 2001:
    for prime in range(len(list_primes(n))):
        if a == 2:
            a = 3
            break
        prime = list_primes(n)[prime]
        for integer in range(int((sqrt(abs(n))))+2):
            if n == prime + 2*(integer**2):
                a = 2
                break
    if a == 0:
        a = 1
        print(n)
    else: 
        n = n + 2










