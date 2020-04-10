transactions = {}

for _ in range(int(input())):
    l = input().split(" ")

    if l[0] not in transactions:
        transactions[l[0]] = {}
    
    if l[1] in transactions[l[0]]:
        transactions[l[0]][l[1]] += int(l[2])
    else:
        transactions[l[0]][l[1]] = int(l[2])

for key in transactions:
    for dep in transactions[key]:
        print(key, dep, transactions[key][dep])
