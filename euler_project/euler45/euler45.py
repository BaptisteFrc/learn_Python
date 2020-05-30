from time import time

start_time = time()

list_triangle = []
for n in range(286,100000):
    list_triangle.append(int(n*(n+1)/2))

list_pentagonal = []
for n in range(1,100000):
    list_pentagonal.append(int(n*(3*n-1)/2))

list_hexagonal = []
for n in range(1,100000):
    list_hexagonal.append(int(n*(2*n-1)))

set_triangle = set(list_triangle)
set_pentagonal = set(list_pentagonal)
set_hexagonal = set(list_hexagonal)

counter = 0
for triangle_number in list_triangle:
    if triangle_number in set_pentagonal and triangle_number in set_hexagonal:
        print("solution:", triangle_number)
        break

print(time() - start_time)