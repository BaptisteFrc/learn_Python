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



def calculator(max):
    max = int(max)
    a = 0
    list_primes_max = list_primes(max)
    for n in range(1,max,2):
        if not n in list_primes_max: 
            max_n = len(list_primes(n))
            for k in range(max_n):
                if a == 1:
                    a = 2
                    break
                prime = list_primes_max[k]
                for integer in range(1,int((sqrt(abs(n))))+2):
                    if n == prime + 2*(integer**2):
                        a = 1
                        break
                if k == (max_n)-1:
                    if a == 2:
                        return n

print(calculator(input()))