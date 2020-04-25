max_decimal_cycle = 0
number_max = 0
for i in range(1,1001):
    if i % 100 == 0:
        print(i)
    list_rest = []
    decimal_cycle = 0
    counter = 0
    rest = -1
    while rest not in list_rest and rest != 0:
        list_rest.append(rest)
        if rest ==-1:
            rest = 1
        rest *= 10
        while rest < i:
            rest *= 10
            counter += 1
            list_rest.append(0)
        rest %= i
        counter += 1
    
    if rest == 0:
        decimal_cycle = 0
    else:
        decimal_cycle = counter - list_rest.index(rest)

    if decimal_cycle > max_decimal_cycle:
        max_decimal_cycle = decimal_cycle
        number_max = i
    
print(number_max)