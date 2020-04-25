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


list_primes = ératosthène(10000000)
for primes in list_primes:
    list_digit = []
    for digit in str(primes):
        if int(digit) not in list_digit:
            list_digit.append(int(digit))
        else:
            break
    list_digit.sort()
    if list_digit == [i for i in range(1,len(list_digit)+1)]:
        solution = primes

print(solution)
print(time()-start_time)
