T = int(input())

trans = {"revenu":{}, "dépense":{}}
for _ in range(T): 
    t, d, n = input().split(" ")
    if d in trans[t]:
        trans[t][d] += int(n)
    else:
        trans[t][d] = int(n)

print(trans)

R = 0
for revenu in trans["revenu"]:
    R +=  trans["revenu"][revenu]
    print("revenu", revenu, trans["revenu"][revenu])

D = 0
for revenu in trans["dépense"]:
    D += trans["dépense"][revenu]
    print("dépense", revenu, trans["dépense"][revenu])

print("balance", R - D)