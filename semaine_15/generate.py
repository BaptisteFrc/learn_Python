from random import choice, randint

transactions = ["revenu", "dépense"]
revenus = ["location", "vente", "devis", "subvention", "réparation"]
dépenses = ["materiel", "nourritures", "transports", "loyer"]

print(1000)
for i in range(1000):
    t = choice(transactions)
    if t == "revenu":
        d = choice(revenus)
    else:
        d = choice(dépenses)
    print(t, d, randint(10, 1000))
