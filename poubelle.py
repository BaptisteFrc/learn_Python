from math import sqrt


def is_prime(i):
    for k in range(2,int((sqrt(abs(i))+1))):
        
        if  i % k == 0:
            return False


m = 0
for n in range (100):
    t = n**2 + n + 41
    if is_prime(t):
        m = n
    else:
        break

print(m)

