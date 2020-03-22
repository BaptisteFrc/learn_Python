n = int(input())

def f(x):
    return 1/x

S = 0
T = 0
for k in range(1,n+1):
    S = S + f(1+k/n)/n

T = S + (f(1)-f(2))/n

print(S)
print(T)
print(T-S)


