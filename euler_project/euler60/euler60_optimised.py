from time import time 

start_time = time()


def ératosthène(n):
    primes = [False, False] + [True for _ in range(2, n+1)]
    for i in range(int((n+1)**(1/2)) + 1):
        if primes[i]:
            multiple = 2 * i
            while multiple < n:
                primes[multiple] = False
                multiple += i
    return [i for i in range(n) if primes[i]]

def is_prime(n, set_primes):
    if n in set_primes:
        return True
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    set_primes.add(n)
    return True

def test(L, set_primes):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            a, b = int(str(L[i]) + str(L[j])), int(str(L[j]) + str(L[i]))
            if not is_prime(a,set_primes) or not is_prime(b, set_primes):
                return False
    return True

list_primes = ératosthène(10000)
set_primes = set(list_primes)

def g(L, i=0):
    if len(L) == 5:
        return L
    for p in range(i, len(list_primes)):
        new_L = L + [list_primes[p]]
        if(test(new_L, set_primes)):
            new_L = g(new_L, p)
            if new_L is not None:
                return new_L
    return None

res = g([])
print(res, "->", sum(res))

print(time() - start_time)