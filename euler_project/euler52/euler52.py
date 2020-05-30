from time import time 

start_time = time()

solution = False
number = 1

while not solution:
    list_number = [digit for digit in str(number)]
    list_number.sort()
    for multiplier in range(2,7):
        list_multiplicated_number = [digit for digit in str(multiplier * number)]
        list_multiplicated_number.sort()
        if list_multiplicated_number != list_number:
            break
        if multiplier == 6:
            solution = True
            print("solution:", number)
    number += 1

print(time() - start_time)