assignator = {}
assignator["unité"] = {0 : 0, 1 : 3, 2 : 3, 3 : 5, 4 : 4, 5 : 4, 6 : 3, 7 : 5, 8 : 5, 9 : 4}
assignator["dizaine"] = {0 : 0, 2 : 6, 3 : 6, 4 : 5, 5 : 5, 6 : 5, 7 : 7, 8 : 6, 9 : 6}
assignator["10-19"] = {10 : 3, 11 : 6, 12 : 6, 13 :8, 14 : 8, 15 : 7, 16 : 7, 17 : 9, 18 : 8, 19 : 8}

counter_letters = 11
for i in range(1,1000):
    I = str(i)
    if i <= 9 :
        counter_letters += assignator["unité"][i]
        continue

    elif 10 <= i <= 99:
        if 10 <= i <=19:
            counter_letters += assignator["10-19"][i]
        else:
            counter_letters += assignator["dizaine"][int(I[0])] + assignator["unité"][int(I[1])]
        continue

    elif i >= 100:
        test = i - int(I[0])*100
        if 10 <= test <= 19:
            counter_letters += 10 + assignator["unité"][int(I[0])] + assignator["10-19"][test]
        elif test == 0:
            counter_letters += 7 + assignator["unité"][int(I[0])]
        else:
            counter_letters += 10 + assignator["unité"][int(I[0])] + assignator["dizaine"][int(I[1])] + assignator["unité"][int(I[2])]

print(counter_letters)