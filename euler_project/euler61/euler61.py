from time import time 

start_time = time()

def triangle_number(Min = 0, Max = 10000):
    n = 1
    Triangle_number = 1
    l = []
    if Min <= 1:
        l.append(Triangle_number)
    while Triangle_number < Max:
        n += 1
        Triangle_number = int(n*(n+1)/2)
        if Triangle_number >= Min:
            l.append(Triangle_number)
    return l    

def square_number(Min = 0, Max = 10000):
    n = 1
    Square_number = 1
    l = []
    if Min <= 1:
        l.append(Square_number)
    while Square_number < Max:
        n += 1
        Square_number = int(n**2)
        if Square_number >= Min:
            l.append(Square_number)
    return l    

def pentagonal_number(Min = 0, Max = 10000):
    n = 1
    Pentagonal_number = 1
    l = []
    if Min <= 1:
        l.append(Pentagonal_number)
    while Pentagonal_number < Max:
        n += 1
        Pentagonal_number = int(n*(3*n-1)/2)
        if Pentagonal_number >= Min:
            l.append(Pentagonal_number)
    return l  

def hexagonal_number(Min = 0, Max = 10000):
    n = 1
    Hexagonal_number = 1
    l = []
    if Min <= 1:
        l.append(Hexagonal_number)
    while Hexagonal_number < Max:
        n += 1
        Hexagonal_number = int(n*(2*n-1))
        if Hexagonal_number >= Min:
            l.append(Hexagonal_number)
    return l  

def heptagonal_number(Min = 0, Max = 10000):
    n = 1
    Heptagonal_number = 1
    l = []
    if Min <= 1:
        l.append(Heptagonal_number)
    while Heptagonal_number < Max:
        n += 1
        Heptagonal_number = int(n*(5*n-3)/2)
        if Heptagonal_number >= Min:
            l.append(Heptagonal_number)
    return l  

def hoctagonal_number(Min = 0, Max = 10000):
    n = 1
    Hoctagonal_number = 1
    l = []
    if Min <= 1:
        l.append(Hoctagonal_number)
    while Hoctagonal_number < Max:
        n += 1
        Hoctagonal_number = int(n*(3*n-2))
        if Hoctagonal_number >= Min:
            l.append(Hoctagonal_number)
    return l  

def comparator_last_first_two_digits(a, b):
    if str(a)[-2:] == str(b)[:2]:
        return True
    return False

list_triangle = triangle_number(1000,10000)[:-1]
list_square = square_number(1000,10000)[:-1]
list_pentagonal = pentagonal_number(1000,10000)[:-1]
list_hexagonal = hexagonal_number(1000,10000)[:-1]
list_heptagonal = heptagonal_number(1000,10000)[:-1]
list_hoctagonal = hoctagonal_number(1000,10000)[:-1]

list_list_polygonal = [list_triangle, list_square, list_pentagonal, list_hexagonal, list_heptagonal, list_hoctagonal]


def cyclical_figurate_number():
    for i in range(6):
        for j in range(6):
            if j not in [i]:
                for k in range(6):
                    if k not in [i,j]:
                        for l in range(6):
                            if l not in [i,j,k]:
                                for m in range(6):
                                    if m not in [i,j,k,l]:
                                        for n in range(6):
                                            if n not in [i,j,k,l,m]:
                                                I = list_list_polygonal[i]
                                                J = list_list_polygonal[j]
                                                K = list_list_polygonal[k]
                                                L = list_list_polygonal[l]
                                                M = list_list_polygonal[m]
                                                N = list_list_polygonal[n]

                                                for a in I:
                                                    for b in J:
                                                        if comparator_last_first_two_digits(a,b):
                                                            for c in K:
                                                                if comparator_last_first_two_digits(b,c):
                                                                    for d in L:
                                                                        if comparator_last_first_two_digits(c,d):
                                                                            for e in M:
                                                                                if comparator_last_first_two_digits(d,e):
                                                                                    for f in N:
                                                                                        if comparator_last_first_two_digits(e,f):
                                                                                            if comparator_last_first_two_digits(f,a):
                                                                                                return [a,b,c,d,e,f]


solution = cyclical_figurate_number()
print(solution)
print(sum(solution))
print(time() - start_time)