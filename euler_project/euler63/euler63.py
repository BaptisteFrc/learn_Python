from time import time 

start_time = time()

solution = 0
for n in range(1,10):
    is_same_length = True
    exponant = 0
    while is_same_length:
        exponant += 1  
        cube = n**exponant
        if len(str(cube)) == exponant:
            solution += 1
        else:
            is_same_length = False

print(solution)


print(time() - start_time)