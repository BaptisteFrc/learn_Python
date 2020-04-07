nombre_ligne = int(input())

ll = []
for _ in range(nombre_ligne):
    ll.append(list(map(int, input().split(","))))

for List in ll:
    n = 0
    for i in List:
        List[n] = i**2
        n += 1

for List in ll:
    for i in range(len(List)):
        List[i] **= 2

for List in ll:
    List.append(sum([i for i in List]))



print(ll)