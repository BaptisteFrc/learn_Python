from time import time 

start_time = time()


def ératosthène(n):
    primes = [False, False] + [True for _ in range(2,n+1)]
    for i in range (int((n+1)**(1/2)) + 1):
        if primes[i]:
            multiple = 2 * i
            while multiple < n:
                primes[multiple] = False
                multiple += i
    return [i for i in range(n) if primes[i]]

list_primes = ératosthène(100000)
set_primes = set(ératosthène(100000000))
len_list_primes = len(list_primes)

concatenator = lambda a , b:  [int(str(a) + str(b)), int(str(b) + str(a))]

def is_concatenated_primes(a, b):
    concatenated_ab = concatenator(a, b)
    if concatenated_ab[0] in set_primes and concatenated_ab[1] in set_primes:
        return True
    else:
         return False

start_time_programme = time()

def prime_pair_sets():
    set_not_concatenated_primes = set()

    for a in range(1,len_list_primes):
        prime_a = list_primes[a]
        for b in range(a+1, len_list_primes):
            prime_b = list_primes[b]
            if (a,b) not in set_not_concatenated_primes:
                if is_concatenated_primes(prime_a, prime_b):
                    for c in range(b+1, len_list_primes):         
                        prime_c = list_primes[c]
                        if (a,c) not in set_not_concatenated_primes and (b,c) not in set_not_concatenated_primes:
                            if is_concatenated_primes(prime_a, prime_c):
                                if is_concatenated_primes(prime_b, prime_c):
                                    for d in range(c+1, len_list_primes):                            
                                        prime_d = list_primes[d]
                                        if (a,d) not in set_not_concatenated_primes and (b,d) not in set_not_concatenated_primes and (c,d) not in set_not_concatenated_primes:
                                            if is_concatenated_primes(prime_a, prime_d):
                                                if is_concatenated_primes(prime_b, prime_d):
                                                    if is_concatenated_primes(prime_c, prime_d):
                                                        for e in range(d+1, len_list_primes):
                                                            prime_e = list_primes[e]
                                                            if (a,e) not in set_not_concatenated_primes and (b,e) not in set_not_concatenated_primes and (c,e) not in set_not_concatenated_primes and (d,e) not in set_not_concatenated_primes:
                                                                if is_concatenated_primes(prime_a, prime_e):
                                                                    if is_concatenated_primes(prime_b, prime_e):
                                                                        if is_concatenated_primes(prime_c,prime_e):
                                                                            if is_concatenated_primes(prime_d,prime_e):
                                                                                return[prime_a, prime_b, prime_c, prime_d, prime_e]

                                                                            else:
                                                                                set_not_concatenated_primes.add((d,e)) 
                                                                        else:
                                                                            set_not_concatenated_primes.add((c,e)) 
                                                                    else:
                                                                        set_not_concatenated_primes.add((b,e))  
                                                                else:     
                                                                    set_not_concatenated_primes.add((a,e))                                                        
                                                    else:
                                                        set_not_concatenated_primes.add((c,d))
                                                else:
                                                    set_not_concatenated_primes.add((b,d))
                                            else:
                                                set_not_concatenated_primes.add((a,d))
                                else:
                                    set_not_concatenated_primes.add((b,c))
                            else:
                                set_not_concatenated_primes.add((a,c))
                else:
                    set_not_concatenated_primes.add((a,b))

solution_primes = prime_pair_sets()
print(solution_primes)
print(sum(solution_primes))
print(time() - start_time_programme)
print(time() - start_time)