from time import time

start_time = time()

def base2_convertissor(number):
    binar_number = ""
    if number == 0:
        return 0
    while number != 0:
        if number % 2 == 0:
            number = number/2
            binar_number = "0" + binar_number
        else:
            number = (number-1)/2
            binar_number = "1" + binar_number
    return binar_number

def base10_convertissor(number):
    base10_number = 0
    list_number = [int(digit) for digit in str(number)]
    for i in range(len(number)):
        if list_number[-(i+1)] == 1:
            base10_number += 2**i
    return base10_number


def is_palyndrome(N):
    N = str(N)
    if N == N[::-1]:
        return True
    else:
        return False
      
solution = 0
for number in range(1000001):
    if is_palyndrome(number) and is_palyndrome(base2_convertissor(number)):
        solution += number

print(solution)
print(time() - start_time)


