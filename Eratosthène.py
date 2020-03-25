from math import sqrt

def list_primes(n):
    n = int(n)
    list_integer = []
    list_boolean = []
    for i in range(n-1):
        list_integer.append(i+2)
        list_boolean.append(True)

    list_primes = list_integer
    for j in range(2,list_integer[n-2]+1):
        for l in range(1,n-1):
            if list_boolean[-l]:
                max_true = n-l+1
                break
        if j > sqrt(max_true):
            break
        if list_boolean[j-2]:
            for k in range(j+1, n+1):
                if list_boolean[k-2]:
                    if k % j == 0:
                        list_boolean[k-2] = False
                        list_primes.remove(k)
    return list_primes

print(list_primes(input()))