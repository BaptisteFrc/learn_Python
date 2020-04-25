from time import time

start_time = time()


def number_convertor(l):
    number = 0
    lenght = len(l)
    for i in range(lenght):
        number += 10**(lenght-(i+1)) * int(l[i])
    return number

list_pandigital = [i for i in range(1,10)]
solution = 0
for number in range(2,10000):
    list_concatenated_number = []
    counter = 0
    test = True
    for multiplier in range(1,9):
        if counter == 9:
            break
        elif counter > 9:
            test = False
            break
        else:
            part_concatenated_number = str(number * multiplier)
            for digit in part_concatenated_number:
                list_concatenated_number.append(int(digit))
                counter += 1

    if test:
        concatenated_number = number_convertor(list_concatenated_number)
        list_concatenated_number.sort()
        if list_concatenated_number == list_pandigital:
            if solution < concatenated_number:
                solution = concatenated_number

print(solution)
print(time()-start_time)        
            


