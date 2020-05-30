from fractions import Fraction
import sys
from time import time 

start_time = time()
sys.setrecursionlimit(10000)


def square_root_two(n):
    if n == 0:
        return Fraction(1/2)
    else: 
        return Fraction(1/( 2 + square_root_two(n-1)))


solution = 0
for n in range(1000):
    square_root2 = 1 + square_root_two(n)
    if len(str(square_root2.numerator)) > len(str(square_root2.denominator)):
        solution += 1

print(solution)
print(time() - start_time)