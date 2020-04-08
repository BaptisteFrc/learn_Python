list_expenditures = []
list_incomes = []
list_money_expenditures = []
list_money_incomes = []

for _ in range(int(input())):
    l = input().split(" ")

    if l[0] == "depense":
        if l[1] not in list_expenditures:
            list_expenditures.append(l[1])
            list_money_expenditures.append(int(l[2]))
        else:
            list_money_expenditures[list_expenditures.index(l[1])] += int(l[2])
    
    else:
        if l[1] not in list_incomes:
            list_incomes.append(l[1])
            list_money_incomes.append(int(l[2]))
        else:
            list_money_incomes[list_incomes.index(l[1])] += int(l[2])


for i in range(len(list_expenditures)):
    print("dépense {}: {}".format(list_expenditures[i], list_money_expenditures[i]))
for i in range(len(list_incomes)):
    print("revenu {}: {}".format(list_incomes[i], list_money_incomes[i]))
print("balance:", sum(list_money_incomes)-sum(list_money_expenditures))





    
