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

counter = 0
solution = 0
list_primes = ératosthène(1000000)
for number in range(11,1000000):
    if counter == 11:
        print("fin")
        break
    if list_primes[number]:
        number = str(number)
        list_digits = []
        test = True
        for digit in number:
            list_digits.append(digit)

        number_digit = list_digits
        for _ in range(len(number_digit)-1):
            del number_digit[0]

            number_normal = number_convertor(number_digit)
            if  not list_primes[number_normal]:
                test = False
                break

        if test:
            list_digits = []
            for digit in number:
                list_digits.append(digit)

            number_digit_reversed = list_digits
            for _ in range(len(number_digit_reversed)-1):
                del number_digit_reversed[-1]

                number_reversed = number_convertor(number_digit_reversed)
                if  not list_primes[number_reversed]:
                    test = False
                    break

        if test:
            print(number)
            counter += 1
            solution += int(number)

print(solution)
print(time()-start_time)

#748317