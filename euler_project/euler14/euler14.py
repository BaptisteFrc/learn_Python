len_max = 0
for i in range(1,1000001):
    counter = 0
    I = i
    while i != 1:
        if i % 2 == 0:
            i = i/2
        else:
            i = 3*i + 1
        counter += 1
    if counter > len_max:
        len_max = counter
        nbr_max = I

print(nbr_max) 