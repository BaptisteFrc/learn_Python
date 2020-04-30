from random import randint
from time import time
import sys

start_time = time()

size = int(sys.argv[2])
length = size * size
grid = []
equiv = []

def init():
    global grid
    global equiv
    grid = [False for _ in range(length)]
    equiv = [i for i in range(length)]


def randomShadow():
    test_white = False
    while not test_white:
        random_index = randint(0, length - 1)
        if not grid[random_index]:
            grid[random_index] = True
            test_white = True
    return random_index

def detectPath(seen, n, up):
    seen[n] = True
    if up and n < size:
        return True
    elif not up and n >= length - size:
        return True
    if n >= size and grid[n - size] and not seen[n - size]:
        if detectPath(seen, n - size, up):
            return True
    if n < length - size and grid[n + size] and not seen[n + size]:
        if detectPath(seen, n + size, up):
            return True
    if n % size != 0 and grid[n - 1] and not seen[n -1]:
        if detectPath(seen, n - 1, up):
            return True
    if n % size != size - 1 and grid[n + 1] and not seen[n + 1]:
        if detectPath(seen, n + 1, up):
            return True
    return False 

def isNaivePercolation(n):
    return detectPath([False for _ in range(length)], n, True) and detectPath([False for _ in range(length)], n, False)

def isPercolation(n):
    return isNaivePercolation(n)

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