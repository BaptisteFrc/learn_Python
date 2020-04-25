counter = 0
for one_p in range(201):
    if one_p % 10 == 0:
        print(one_p)
    for two_p in range(101):
        if one_p >= 200:
            if one_p == 200:
                counter += 1
            break
        for five_p in range(41):
            Sum = one_p + 2*two_p
            if Sum >= 200:
                if Sum == 200:
                    counter += 1
                break
            for ten_p in range(21):
                Sum = one_p + 2*two_p + 5*five_p
                if Sum >= 200:
                    if Sum == 200:
                        counter += 1
                    break
                for twenty_p in range(11):
                    Sum = one_p + 2*two_p + 5*five_p + 10*ten_p
                    if Sum >= 200:
                        if Sum == 200:
                            counter += 1
                        break
                    for fifty_p in range(5):
                        Sum = one_p + 2*two_p + 5*five_p + 10*ten_p + 20*twenty_p
                        if Sum >= 200:
                            if Sum == 200:
                                counter += 1
                            break
                        for one in range(3):
                            Sum = one_p + 2*two_p + 5*five_p + 10*ten_p + 20*twenty_p + 50*fifty_p
                            if Sum >= 200:
                                if Sum == 200:
                                    counter += 1
                                break
                            for two in range(2):
                                if one_p + 2*two_p + 5*five_p + 10*ten_p + 20*twenty_p + 50*fifty_p + 100*one + 200*two == 200:
                                    counter += 1

print(counter)