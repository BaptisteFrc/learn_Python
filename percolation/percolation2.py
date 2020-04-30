from random import randint
from time import time
import sys

start_time = time()

size = int(sys.argv[2])
length = size * size
grid = []
equiv = []

"""
grid = [False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False]
equiv = [i for i in range(length)]
for i in range(length):
    if grid[i]:
        equiv[i] = 6
"""




def init():
    global grid
    global equiv
    grid = [False for _ in range(length)]
    equiv = [i for i in range(length)]

def naiveFind(n):
    return equiv[n]

def naiveUnion(n, m):
    global equiv
    corresponding_classe_n = find(n)
    corresponding_classe_m = find(m)
    equiv = [corresponding_classe_m if i == corresponding_classe_n else i   for i in equiv]
    return corresponding_classe_m

def find(n):
    return naiveFind(n)

def union(n, m):
    return naiveUnion(n, m)

def randomShadow():
    test_white = False
    while not test_white:
        random_index = randint(0, length - 1)
        if not grid[random_index]:
            grid[random_index] = True
            test_white = True
    propagateUnion(random_index)
    return random_index

def propagateUnion(n):
    if n >= size and grid[n - size]:
        union(n - size, n)
    if n < length - size and grid[n + size]:
        union(n + size, n)
    if n % size != 0 and grid[n - 1]:
        union(n - 1, n)
    if n % size != size - 1 and grid[n + 1]:
        union(n + 1, n)





def isFastPercolation(n):
    solution = False
    for first_line in range(size):
        if find(n) == find(first_line):
            solution = True
            break
    if solution:
        solution = False
        for last_line in range(length - size, length):
            if find(n) == find(last_line):
                solution = True
    return solution




def isPercolation(n):
    return isFastPercolation(n)

def percolation():
    init()
    counter = 0
    solution = False
    while not solution:
        solution = isPercolation(randomShadow())
        counter +=1
    
    return (counter/length)

def printer():
    for i in range(size):
        for j in range(size):
            if grid[i * size + j]:
                print("*", end = "")
            else:
                print("-", end = "")
        print()


def monteCarlo(n):
    mean = 0
    for _ in range(n):
        mean += percolation()
    return (mean/n)

print(monteCarlo(int(sys.argv[1])))
print(time() - start_time)