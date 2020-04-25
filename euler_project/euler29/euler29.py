list_power = []
for a in range(2,101):
    for b in range(2,101):
        power = a**b
        list_power.append(power)

print(len(list(set(list_power))))