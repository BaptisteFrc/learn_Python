s = int(input())

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        a = b
        b = c
    return b

print(fibo(s))
