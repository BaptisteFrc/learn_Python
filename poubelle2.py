from math import sqrt


def is_prime(n):
    for k in range(2,int((sqrt(abs(n))+1))):
        if  n % k == 0:
            return False

if not is_prime(8):
    print("oui")



