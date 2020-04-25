from math import prod


# limite supérieur = 2540160 car 7*9! = 2540160 < 9999999

solution = 0
for number in range(3,1500000):
    sum_factorial_digit = 0
    for digit in str(number):
        sum_factorial_digit += prod([i for i in range(1,int(digit)+1)])
    if sum_factorial_digit == number:
        solution += number

print(solution)
