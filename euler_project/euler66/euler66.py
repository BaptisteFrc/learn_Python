from time import time 

start_time = time()

set_squares = set([i**2 for i in range(1,1000001)])
upper_bound = 1000000**2 

def is_perfect_square(n):
    if n <= upper_bound:
        if n in set_squares:
            return True
        else:
            return False
    else:
        x = n // 2
        seen = set([x])
        while x * x != n:
            x = (x + (n // x)) // 2
            if x in seen: return False
            seen.add(x)
        return True



x_max = 0
for D in range(1,1001):
    print(D)
    if D not in set_squares:

        is_even = D % 2 == 0

        solution = False
        x = 1
        while not solution:
            
            if x > 100000:
                if x % 10000 == 0:
                    print(x)
                    
            y_square = (x**2 - 1)/D
            if int(y_square) == y_square:
                if is_perfect_square(y_square):
                    solution = True
                else:
                    if is_even:
                        x += 2
                    else:
                        x += 1
            else:
                if is_even:
                    x += 2
                else:
                    x += 1
        
        if x_max < x:
            x_max = x
            print("x_max:",x_max)
            D_max = D
            print("D_max:",D_max)


print(D_max)