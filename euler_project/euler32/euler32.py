from math import sqrt

def transformer(n):
    l = []
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            l.append(i)
    for i in range(len(l)):
        if l[i]!=(sqrt(n)):
            l.append(int(n/l[i])) 
    return l


list_pandigital = [i for i in range(1,10)]
counter = 0
for number in range(999,10000):
    list_divisors = transformer(number)
    for divisor in list_divisors:
        list_test = []
        if divisor > 99:
            divisor2 = int(number/divisor)
            for digit in str(number):
                list_test.append(int(digit))
            for digit in str(divisor):
                list_test.append(int(digit))
            for digit in str(divisor2):
                list_test.append(int(digit))
            list_test.sort()
            if list_test == list_pandigital:
                counter += number
                break


print(counter)
#45228
            
