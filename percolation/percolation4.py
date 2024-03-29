from random import randint
from time import time
import sys

start_time = time()

size = int(sys.argv[2])
length = size * size
grid = []
equiv = []
height = []


def init():
    global grid
    global equiv
    global height
    grid = [False for _ in range(length)]
    equiv = [0 if i < size else length - 1 if i >= length - size else i for i in range(length)]
    height = [1 for i in range(length)]


def fastFind(n):
    while equiv[n] != n:
        equiv[n] = equiv[equiv[n]]
        n = equiv[n]

    return n


def logUnion(n, m):
    if height[find(n)] == height[find(m)]:
        equiv[find(n)] = find(m)
        height[find(m)] += 1
    elif height[find(n)] < height[find(m)]:
        equiv[find(n)] = find(m)
    else:
        equiv[find(m)] = find(n)
    return find(m)


# quand un arbre s'accroche a un autre de meme taille, l'arbre resultant gagne 1 en taille.
# si les deux arbres ont une taille differente, l'arbre resultant garde la meme taille.

def find(n):
    return fastFind(n)


def union(n, m):
    return logUnion(n, m)


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
    if find(0) == find(length - 1):
        return True
    return False


def isPercolation(n):
    return isFastPercolation(n)


def percolation():
    init()
    counter = 0
    solution = False
    while not solution:
        solution = isPercolation(randomShadow())
        counter += 1
        """
        if counter % 1000 == 0:
            print(counter)
        """
    return (counter/length)


def printer():
    for i in range(size):
        for j in range(size):
            if grid[i * size + j]:
                print("*", end="")
            else:
                print("-", end="")
        print()


def monteCarlo(n):
    mean = 0
    for _ in range(n):
        mean += percolation()
    return (mean/n)


print(monteCarlo(int(sys.argv[1])))
print(time() - start_time)