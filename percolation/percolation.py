from random import randint

size = 100
length = size * size
grid = []


def init():
    global grid
    grid = [False for _ in range(length)]

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
    if n < length - size and grid[n+size] and not seen[n + size]:
        if detectPath(seen, n + size, up):
            return True
    if n % size != 0 and grid[n - 1] and not seen[n -1]:
        if detectPath(seen, n - 1, up):
            return True
    if n % size != size - 1 and grid[n+1] and not seen[n + 1]:
        if detectPath(seen, n + 1, up):
            return True
    return False 

def isNaivePercolation(n):
    return detectPath([False for _ in range(length)], n, True) and detectPath([False for _ in range(length)], n, False)

def detectPathUp(seen_up, seen_path_up, n, up, left, right, list_test):
    if n in range(size):
        list_test.append(True)
        return
    if grid[up] and up not in seen_up and up not in seen_path_up:
        if up in range(size):
            list_test.append(True)
            return 
        else:
            seen_path_up.append(n)
            n = up 
            left = n - 1
            right = n + 1
            up = n - size
            detectPathUp(seen_up, seen_path_up, n, up, left, right, list_test)
    elif n % 10 != 0:
        if grid[left] and left not in seen_up and left not in seen_path_up:
            seen_path_up.append(n)
            n = left
            left = n - 1
            right = n + 1
            up = n - size
            detectPathUp(seen_up, seen_path_up, n, up, left, right, list_test)
    elif (n-9) % 10 != 0:
        if grid[right] and right not in seen_up and right not in seen_path_up: 
            seen_path_up.append(n)
            n = right 
            left = n - 1
            right = n + 1
            up = n - size
            detectPathUp(seen_up, seen_path_up, n, up, left, right, list_test)
     
    seen_up.append(n)
    return 

def detectPathDown(seen_down, seen_path_down, n, down, left, right, list_test):
    if n in range(length - size, length):
        list_test.append(True)
        return
    if grid[down] and down not in seen_down and down not in seen_path_down:
        if down in range(length - size, length):
            list_test.append(True)
            return 
        else:
            seen_path_down.append(n)
            n = down
            left = n - 1
            right = n + 1
            down = n + size
            detectPathDown(seen_down, seen_path_down, n, down, left, right, list_test)
    elif n % 10 != 0:
        if grid[left] and left not in seen_down and left not in seen_path_down :
            seen_path_down.append(n)
            n = left
            left = n - 1
            right = n + 1
            down = n + size
            detectPathDown(seen_down, seen_path_down, n, down, left, right, list_test)
    elif (n-9) % 10 != 0:
        if grid[right] and right not in seen_down and right not in seen_path_down: 
            seen_path_down.append(n)
            n = right 
            left = n - 1
            right = n + 1
            down = n + size
            detectPathDown(seen_down, seen_path_down, n, down, left, right, list_test)
    
    seen_down.append(n)
    return 

def  isNaivePercolationOld(n):
    N = n
    left = n - 1
    right = n + 1
    up = n - size
    down = n + size
    seen_up = []
    seen_down =[]
    list_test = []

    while N not in seen_up and list_test != [True]:
        n = N
        left = n - 1
        right = n + 1
        up = n - size
        seen_path_up = []
        detectPathUp(seen_up, seen_path_up, n, up, left, right, list_test)
    if list_test == [True]:
        solution = True
    else:
        solution = False
    
    if solution:
        while n not in seen_down and list_test != [True, True]:
            n = N
            left = n - 1
            right = n + 1
            down = n + size
            seen_path_down = []
            detectPathDown(seen_down, seen_path_down, n, down, left, right, list_test)
        if list_test == [True, True]:
            solution = True
        else:
            solution = False
    return solution

def isPercolation(n):
    return isNaivePercolation(n)

def percolation():
    init()
    counter = 0
    solution = False
    while not solution:
        solution = isPercolation(randomShadow())
        counter +=1
    
    return(counter/length)

def printer():
    for i in range(size):
        for j in range(size):
            if grid[i*size+j]:
                print("*", end="")
            else:
                print("-", end="")
        print()

print(percolation())
printer()