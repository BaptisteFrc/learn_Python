
list_expenditures = []
list_incomes = []
list_money_expenditures = []
list_money_incomes = []


for _ in range(int(input())):
    l = input().split(" ")
    print(l[0])
    if l[0] == "depense":
        if l[1] not in list_expenditures:
            list_expenditures.append(l[1])
            list_money_expenditures.append(int(l[2]))
        else:

            list_money_expenditures[list_expenditures.index(l[1])] += int(l[2])

print(list_expenditures)
print(list_money_expenditures)
print(list_incomes)
print(list_money_incomes)