def is_palyndrome(N):
    N = str(N)
    if N == N[::-1]:
        return True
    else:
        return False

def produit_palyndrome(n):
    maximum = 0
    for i in range(n+1):
        for j in range(n+1):
            h = i*j
            if is_palyndrome(h):
                if h > maximum:
                    maximum = h
    return maximum

print(produit_palyndrome(int(input("valeur maximale des facteurs: "))))