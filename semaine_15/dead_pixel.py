def calcul_area_max():
    l = list(map(int, input().split(" ")))
    area_max = max([(l[2])*(l[1]), (l[1]-(l[3]+1))*(l[0]), (l[0]-(l[2]+1))*(l[1]), (l[3])*(l[0])])
    print("the maximal area without the dead pixel is :",area_max)

for _ in range(int(input())):
    calcul_area_max()