from time import time 

start_time = time()

def number_convertor(l):
    s = ''.join(map(str, l))
    return s

list_cubes = [i**3 for i in range(1,10000)]
dict_cubes = {}
set_cubes = set()

for cube in list_cubes:
    Cube = [int(digit) for digit in str(cube)]
    Cube.sort()
    int_Cube = number_convertor(Cube)
    if int_Cube in set_cubes: 
        dict_cubes[int_Cube] += [cube]
        if len(dict_cubes[int_Cube]) == 5:
            list_solution = dict_cubes[int_Cube]
            solution = min(list_solution)
            print(solution)
            break
    else:
        set_cubes.add(int_Cube)
        dict_cubes[int_Cube] = [cube]

print(time() - start_time)