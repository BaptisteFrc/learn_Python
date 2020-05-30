from math import prod
from time import time 

start_time = time()


factorial = lambda n : prod([i for i in range(1, n+1)])

solution = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if factorial(n)/(factorial(r)*factorial(n-r)) >= 1000000:
            solution += 1


print(solution)
print(time() - start_time)