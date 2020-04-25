from math import sqrt
from time import time

start_time = time()

def ératosthène(n):
    primes = [False, False] + [True for _ in range(2,n+1)]
    for i in range (int(sqrt(n+1)) + 1):
        if primes[i]:
            multiple = 2 * i
            while multiple < n:
                primes[multiple] = False
                multiple += i
    return primes

def number_convertor(l):
    number = 0
    lenght = len(l)
    for i in range(lenght):
        number += 10**(lenght-(i+1)) * int(l[i])
    return number

solution = 2
list_primes = ératosthène(1000000)

for number in range(len(list_primes)):
    if list_primes[number]:
        if "0" in str(number) or "2" in str(number) or "4" in str(number) or "6" in str(number) or "8" in str(number) or "5" in str(number):
            continue
        else:
            number_rotated = 0
            counter_rotated_primes = 0
            test = True
            enter = True
            while number_rotated != number:
                if enter:
                    number_rotated = number
                    enter = False
                if list_primes[number_rotated]:
                    list_primes[number_rotated] = False
                    counter_rotated_primes += 1
                else:
                    test = False
                    break 

                list_digits = []

                for digit in str(number_rotated):
                    list_digits.append(digit)

                l_0 = list_digits[0]
                del list_digits[0]
                list_digits.append(l_0)
                number_rotated = number_convertor(list_digits)
            if test:
                solution += counter_rotated_primes

print(solution)
print(time()-start_time)