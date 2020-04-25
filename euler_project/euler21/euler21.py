from math import sqrt

def transformer(n):
    l = []
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            l.append(i)
    for i in range(len(l)):
        if l[i]!=int(sqrt(n)):
            l.append(int(n/l[i]))
    l.append(1)
            
    return sum(l)

List = []
counter = 0
a = 1
b = 1
for i in range(1,10001):
    a = transformer(i)
    b = transformer(a)
    if a not in List:
        if a == transformer(b) and a != b and a <= 10000 and b <= 10000:
            counter += a + b
            List.append(a)
            List.append(b)


print(counter)         
#31626

"""
print(transformer(220))
print(transformer(transformer(220)))
"""