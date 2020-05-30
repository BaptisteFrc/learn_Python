from time import time

start_time = time()

def divisors(n):
    l = []
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            l.append(i)
    for i in range(len(l)):
        if l[i]!=(n**(1/2)):
            l.append(int(n/l[i]))
    return l

def ératosthène(n):
    primes = [False, False] + [True for _ in range(2,n+1)]
    for i in range (int((n+1)**(1/2)) + 1):
        if primes[i]:
            multiple = 2 * i
            while multiple < n:
                primes[multiple] = False
                multiple += i
    return [i for i in range(n) if primes[i]]



list_primes = ératosthène(100000)
set_primes = set(list_primes)

solution = False
number = 2
counter_consecutive_number = 0
while not solution:
    counter_primes_divisors = 0
    list_divisors = divisors(number)
    for Divisors in list_divisors:
        if Divisors in set_primes:
            counter_primes_divisors += 1
    if counter_primes_divisors != 4:
        counter_consecutive_number = 0
    else:
        counter_consecutive_number += 1 
    
    if counter_consecutive_number == 4:
        solution = True
        break
     
    number += 1

print(number - 3)
print(time() - start_time)
