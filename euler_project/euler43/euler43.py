from itertools import permutations
from time import time

start_time = time()

def number_convertor(l):
    number = 0
    lenght = len(l)
    for i in range(lenght):
        number += 10**(lenght-(i+1)) * int(l[i])
    return number


list_pandigital = list(permutations("0123456789"))

solution = 0
for pandigital in list_pandigital:
    if int(pandigital[3]) not in [0,2,4,6,8]:
        continue
    if sum([int(pandigital[i]) for i in range(2,5)]) % 3 != 0:
        continue
    if int(pandigital[5]) not in [0,5]:
        continue

    number_5_to_7 = [int(pandigital[i]) for i in range(4,7)]
    if number_convertor(number_5_to_7) % 7 != 0:
        continue

    number_6_to_8 = [int(pandigital[i]) for i in range(5,8)]
    if number_convertor(number_6_to_8) % 11 != 0:
        continue

    number_7_to_9 = [int(pandigital[i]) for i in range(6,9)]
    if number_convertor(number_7_to_9) % 13 != 0:
        continue

    number_8_to_10 = [int(pandigital[i]) for i in range(7,10)]
    if number_convertor(number_8_to_10) % 17 != 0:
        continue    
    else:
        solution += number_convertor(pandigital)

print(solution)
print(time() - start_time)

#16695334890