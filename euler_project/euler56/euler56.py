from time import time

start_time = time()

solution = 0
for a in range(1,100):
    for b in range(1,100):
        Sum = sum([int(digit) for digit in str(a**b)])
        if Sum > solution:
            solution = Sum 

print(solution)
print(time()-start_time)