from fractions import Fraction

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

product_numerator = 1
product_denominator = 1
for denominator in range(11,100):
    if denominator % 10 != 0:
        for numerator in range(11,denominator):
            Common_digit = common_digit(numerator,denominator)
            if numerator % 10 != 0 and Common_digit != None:
                new_numerator = supressor(numerator, Common_digit)
                new_denominator = supressor(denominator, Common_digit)
                if numerator/denominator == new_numerator/new_denominator:
                    print(numerator, denominator)
                    product_numerator *= new_numerator
                    product_denominator *= new_denominator 

solution = Fraction(product_numerator/product_denominator).limit_denominator()
print(solution.denominator)