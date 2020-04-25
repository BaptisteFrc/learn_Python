corner = 1
gap = 1
sum_corner = 1
    
while (gap + 2) <= 1001:
    for _ in range(4):
        corner += gap + 1 
        sum_corner += corner
    gap += 2

print(sum_corner)