from math import sqrt


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

list_primes = ératosthène(100000)
number = 233
number = str(number)
list_digits = []
test = True
for digit in number:
    list_digits.append(digit)
print(list_digits)

number_digit = list_digits
for _ in range(len(number_digit)-1):
    del number_digit[0]

    number_normal = number_convertor(number_digit)
    print(number_normal)
    if  not list_primes[number_normal]:
        test = False
        break



list_digits = []
for digit in number:
    list_digits.append(digit)
print(list_digits)

number_digit_reversed = list_digits
for _ in range(len(number_digit_reversed)-1):
    del number_digit_reversed[-1]

    number_reversed = number_convertor(number_digit_reversed)
    print(number_reversed)
    if  not list_primes[number_reversed]:
        test = False
        break

if test:
    print("yes")