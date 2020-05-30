from time import time 

start_time = time()

def is_prime(n):
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

ratio_primes = 1
gap = 1
corner = 1
number_corners = 1
number_corner_primes = 0

while ratio_primes >= 0.1:
    for _ in range(4):
        number_corners += 1
        corner += gap + 1
        if is_prime(corner):
            number_corner_primes += 1
    ratio_primes = number_corner_primes/number_corners
    gap += 2

print(gap)
print(time() - start_time)    