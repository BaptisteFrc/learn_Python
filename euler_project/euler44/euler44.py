from time import time

start_time = time()

list_pentagonal = []
for n in range(1,2501):
    list_pentagonal.append(int(n*(3*n-1)/2))


solution = []
solution_difference = 100000000
counter = 0
print(len(list_pentagonal))
for number1 in range(2500):
    counter += 1
    if counter % 10 == 0:
        print(counter)
    for number2 in range(number1 + 1, 2500):
        number_1 = list_pentagonal[number1]
        number_2 = list_pentagonal[number2]
        
        if number2 != 2499:
            if number_1 + number_2 < list_pentagonal[number2 + 1]:
                break
        
        number_difference = number_2 - number_1
        if number_difference in list_pentagonal and (number_1 + number_2) in list_pentagonal:
            if solution_difference > number_difference:
                if number_difference != 0:
                    solution_difference = number_difference
                    solution = [number_1 , number_2]

print(solution)
print(solution_difference)
print(time() - start_time)