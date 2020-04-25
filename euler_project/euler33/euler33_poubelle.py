def common_digit(numerator, denominator):
    for digit_numerator in str(numerator):
        for digit_denominator in str(denominator):
            if digit_denominator == digit_numerator:
                return int(digit_numerator)

def supressor(number, digit):
    number = str(number)
    number = [int(digit_test) for digit_test in number]
    number.remove(digit)
    number = number[0]
    return number

from fractions import Fraction

n = 798/458

print(Fraction(n).limit_denominator().denominator)


