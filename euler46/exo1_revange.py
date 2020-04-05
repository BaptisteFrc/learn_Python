from math import sqrt

def ératosthène(n):
    primes = [False, False] + [True for _ in range(2,n+1)]
    for i in range (int(sqrt(n+1)) + 1):
        if primes[i]:
            multiple = 2 * i
            while multiple < n:
                primes[multiple] = False
                multiple += i
    return [i for i in range (n) if primes[i]]

def calculator(n):
    primes = ératosthène(n)
    squares = [i**2 for i in range(int(sqrt(n))+1)]
    for k in range (5,n+1,2):
        Test = True
        for prime in primes:
            for square in squares:
                if k == prime + 2*square:
                    Test = False
                    break
                elif prime + 2*square > k:
                    break
            if prime > k or not Test:
                break
        if Test: 
            return k

n = int(input())
print("solution =", calculator(n))