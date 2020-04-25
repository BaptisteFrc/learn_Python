solution = 0
for number in range(2,300000):
    sum_power = 0
    for digit in str(number):
        sum_power += int(digit)**5
    if sum_power == number:
        solution += number

print(solution)
#443839