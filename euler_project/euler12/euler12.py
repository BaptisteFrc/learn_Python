from math import sqrt

def transformer(n):
    l = []
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            l.append(i)
    for i in range(len(l)):
        if l[i]!=int(sqrt(n)):
            l.append(int(n/l[i]))
    return len(l)


n = 1
N = 1
while transformer(N)<500:
    n += 1
    N += n


print(N)