from fractions import Fraction
from time import time 

start_time = time()

list_e = [2,1]
n = 1
while len(list_e) != 100:
    list_e.append(2*n)
    if len(list_e) != 100:
        list_e.append(1)
    if len(list_e) != 100:
        list_e.append(1)
    n += 1 

approximation = 1
enter = True
for number in list_e[::-1]:
    if enter:
        approximation = number
        enter = False
    else:
        approximation = Fraction(number + (1/approximation))

print(sum([int(digit) for digit in str(approximation.numerator)]))

print(time() - start_time)