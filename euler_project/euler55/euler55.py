from time import time

start_time = time()


def is_palyndrome(N):
    N = str(N)
    if N == N[::-1]:
        return True
    else:
        return False

solution = 0
for number in range(1,10001):
    N = number
    number = str(number)
    counter = 0 
    Is_palyndrome = False
    while not Is_palyndrome:
        counter += 1
        number = str(int(number) + int(number[::-1]))
        if is_palyndrome(number):
            Is_palyndrome = True
        if counter >= 50:
            solution += 1
            break

print(solution)
print(time()-start_time)