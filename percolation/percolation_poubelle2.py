from random import randint

size = 10
lenght = size * size
grid = []

def init():
    for _ in range(size):
        grid.append([False for _ in range(size)])

def randomShadow():
    test_white = False
    while not test_white:
        random_line = randint(0,size-1)
        random_column = randint(0,size-1)
        if not grid[random_line][random_column]:
            grid[random_line][random_column] = True
            test_white = True
    print(random_line)
    print(random_column)

init()
randomShadow()

for l in grid:
    for i in range(size):
        if l[i]:
            l[i] = "*"
        else:
            l[i] = "-"

    print(l)


