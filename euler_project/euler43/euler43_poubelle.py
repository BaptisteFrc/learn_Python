pandigital = [0,1,2,3,4,5,6,7,8,9]


def number_convertor(l):
    number = 0
    lenght = len(l)
    for i in range(lenght):
        number += 10**(lenght-(i+1)) * int(l[i])
    return number



number_3_to_5 = [pandigital[i] for i in range(2,5)]

if number_convertor(number_3_to_5) % 7 != 0:
    print("yes")
print(number_3_to_5)