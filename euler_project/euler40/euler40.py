from time import time

start_time = time()

list_decimal = [0]
counter = 0
number = 0
while counter <= 1000000:
    number += 1
    for digit in str(number):
        list_decimal.append(int(digit))
        counter += 1

solution = list_decimal[1]*list_decimal[10]*list_decimal[100]*list_decimal[1000]*list_decimal[10000]*list_decimal[100000]*list_decimal[1000000]

print(solution)
print(time()-start_time)