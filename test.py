N = int(input("N= "))

def affiche(S):
    a = input("a= ")
    A = a
    print(a)
    for i in range(S):
        A = A+a
        print(A)

affiche(N-1)
