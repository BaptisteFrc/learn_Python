from math import sqrt


def is_prime(n):
    for k in range(2,int((sqrt(abs(n))+1))):
        if n % k == 0:
            return True



m = 0
n_max = 0
for a in range(-1000,1000):
    for b in range(-1000,1000):
        for n in range (100):
            if not is_prime(n**2 + a*n + b):
                m = n 
            else:
                break
        if n_max < m:
            n_max = m
            s_a = a
            s_b = b

print(n_max)
print(s_a)
print(s_b)
print("solution: ",s_a * s_b)