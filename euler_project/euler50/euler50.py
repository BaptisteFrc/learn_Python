from time import time 

start_time = time()


def ératosthène(n):
    primes = [False, False] + [True for _ in range(2,n+1)]
    for i in range (int((n+1)**(1/2)) + 1):
        if primes[i]:
            multiple = 2 * i
            while multiple < n:
                primes[multiple] = False
                multiple += i
    return [i for i in range(n) if primes[i]]


list_primes = ératosthène(1000000)
set_primes = set(list_primes)
len_primes = len(list_primes)
solution = 0
max_counter = 0

for prime in range(len_primes):
    consecutive_sum = list_primes[prime]
    counter_consecutive = 0
    for added_prime in range(prime + 1, len_primes):
        added_prime = list_primes[added_prime]
        consecutive_sum += added_prime
        counter_consecutive += 1
        if consecutive_sum >= 1000000:
            break
        if consecutive_sum in set_primes and counter_consecutive > max_counter:
            max_counter = counter_consecutive
            solution = consecutive_sum

print(max_counter)
print(solution)
print(time() - start_time)

#997651