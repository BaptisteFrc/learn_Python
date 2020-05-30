from time import time 

start_time = time()

set_sqare = set([i**2 for i in range(101)])
solution = 0

for n in range(2,10001):
    if n not in set_sqare:
        m = 0 
        d = 1
        a = int(n**(1/2))
        A = a
        
        counter = 0
        while a != 2 * A:
            m = d * a - m
            d = (n - m**2)/d
            a = int((A + m)/d)
            counter += 1

        if counter % 2 == 1:
            solution += 1


print(solution)
print(time() - start_time)