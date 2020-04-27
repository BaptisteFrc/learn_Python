list_pentagonal = []
for n in range(1,3001):
    list_pentagonal.append(int(n*(3*n-1)/2))


solution = []
solution_difference = 100000000
counter = 0
print(len(list_pentagonal))
for number1 in range(3000):
    counter += 1
    if counter % 10 == 0:
        print(counter)
    for k in range(1, 3000 - number1):
        number_1 = list_pentagonal[number1]
        number_difference = (k*(3*k+6*(number1+1)-1))/2
        number_2 = number_1 + number_difference
        number_sum = number_1 + number_2


        if number_sum < number_2 + 3*(k+number1) + 1:
            break
       
        if number_difference in list_pentagonal and number_sum in list_pentagonal:
            if solution_difference > number_difference:
                if number_difference != 0:
                    solution_difference = number_difference
                    solution = [number_1 , number_2]
           
print(solution)
print(solution_difference)

Sum = 0
Dif = 0
for number in range(3000):
    k = number + 2 
    counter = 0 
    while counter != 3000-number:
        """
        Sum = 3*(number)**2 + 2*number +1
        Dif = 3*number + 1 
        """ 
        #calculer Dn+1 en fonction de Dn, pareil pour somme