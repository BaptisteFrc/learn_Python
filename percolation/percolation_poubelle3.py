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