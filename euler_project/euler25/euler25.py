F_minus2 = 1
F_minus1 = 1
F = 0
counter = 2
while len(str(F))< 1000:
    F = F_minus2 + F_minus1
    counter += 1
    F_minus2 = F_minus1
    F_minus1 = F

print(counter)