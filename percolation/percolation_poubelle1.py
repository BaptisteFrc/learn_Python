from random import randint

size = 10
lenght = size * size
grid = []


def init():
    for _ in range(lenght):
        grid.append(False)

#grid = [False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False]


def randomShadow():
    test_white = False
    while not test_white:
        random_line = randint(0,size-1)
        random_column = randint(0,size-1)
        random_index = random_line * size + random_column
        if not grid[random_index]:
            grid[random_index] = True
            test_white = True
    return random_index





def detectPathUp(seen_up, seen_path_up, n, up, left, right, N, list_test):
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
            #print("haut")
            detectPathUp(seen_up, seen_path_up, n, up, left, right, N, list_test)
    elif n % 10 != 0:
        if grid[left] and left not in seen_up and left not in seen_path_up:
            seen_path_up.append(n)
            n = left
            left = n - 1
            right = n + 1
            up = n - size
            #print("gauche")
            detectPathUp(seen_up, seen_path_up, n, up, left, right, N, list_test)
    elif (n-9) % 10 != 0:
        if grid[right] and right not in seen_up and right not in seen_path_up: 
            seen_path_up.append(n)
            n = right 
            left = n - 1
            right = n + 1
            up = n - size
            #print("droit")
            detectPathUp(seen_up, seen_path_up, n, up, left, right, N, list_test)
     
    seen_up.append(n)
    #print("stoppé à:", n)
    return 


def detectPathDown(seen_down, seen_path_down, n, down, left, right, N, list_test):
    if n in range(lenght - size, lenght):
        list_test.append(True)
        return
    if grid[down] and down not in seen_down and down not in seen_path_down:
        if down in range(lenght - size, lenght):
            list_test.append(True)
            return 
        else:
            seen_path_down.append(n)
            n = down
            left = n - 1
            right = n + 1
            down = n + size
            #print("bas")
            detectPathDown(seen_down, seen_path_down, n, down, left, right, N, list_test)
    elif n % 10 != 0:
        if grid[left] and left not in seen_down and left not in seen_path_down :
            seen_path_down.append(n)
            n = left
            left = n - 1
            right = n + 1
            down = n + size
            #print("gauche")
            detectPathDown(seen_down, seen_path_down, n, down, left, right, N, list_test)
    elif (n-9) % 10 != 0:
        if grid[right] and right not in seen_down and right not in seen_path_down: 
            seen_path_down.append(n)
            n = right 
            left = n - 1
            right = n + 1
            down = n + size
            #print("droit")
            detectPathDown(seen_down, seen_path_down, n, down, left, right, N, list_test)
    
    seen_down.append(n)
    #print("stoppé à:", n)
    return 


init()


counter = 0
solution = False
while not solution:

    n = randomShadow()
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
        detectPathUp(seen_up, seen_path_up, n, up, left, right, N, list_test)
    if list_test == [True]:
        solution = True
    else:
        solution = False

    
    #print("HAUT FAIT")
    #print("solution haut:", solution)
    

    if solution:
        while n not in seen_down and list_test != [True, True]:
            n = N
            left = n - 1
            right = n + 1
            down = n + size
            seen_path_down = []
            detectPathDown(seen_down, seen_path_down, n, down, left, right, N, list_test)
        if list_test == [True, True]:
            solution = True
        else:
            solution = False
    counter += 1
    

print(counter/100)
#print(n)



for line in range(size):
    l = []
    for column in range(size):
        index = line * size + column
        if grid[index]:
            index = "*"
        else:
            index = "-"
        l.append(index)
    print(l)

