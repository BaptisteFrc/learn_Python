from time import time

start_time = time()

#p = (a**2 + b**2)**(1/2) + a + b


list_solution = [0 for _ in range(1001)]
solution = 0
for a in range(1,501):
    for b in range(1,501):
        p = (a**2 + b**2)**(1/2) + a + b
        if p == int(p) and p <= 1000:
            list_solution[int(p)] += 1


counter_max = 0
for  counter in list_solution:
    if counter > counter_max:
        counter_max = counter
        solution = list_solution.index(counter)

print(solution)
print(time()-start_time)