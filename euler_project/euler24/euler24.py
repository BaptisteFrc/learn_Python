def number_convertor(l):
    number = 0
    for i in range(10):
        number += 10**(9-i) * l[i]
    return (number)

def fonction():
    list_number = []
    for a in range(10):
        list_index_b = [a]
        for b in range(10):
            if b not in list_index_b:
                list_index_c = [a,b]
                for c in range(10):
                    if c not in list_index_c:
                        list_index_d = [a,b,c]
                        for d in range(10):
                            if d not in list_index_d:
                                list_index_e = [a,b,c,d]
                                for e in range(10):
                                    if e not in list_index_e:
                                        list_index_f = [a,b,c,d,e]
                                        for f in range(10):
                                            if f not in list_index_f:
                                                list_index_g = [a,b,c,d,e,f]
                                                for g in range(10):
                                                    if g not in list_index_g:
                                                        list_index_h = [a,b,c,d,e,f,g]
                                                        for h in range(10):
                                                            if h not in list_index_h:
                                                                list_index_i = [a,b,c,d,e,f,g,h]
                                                                for i in range(10):
                                                                    if i not in list_index_i:
                                                                        list_index_j = [a,b,c,d,e,f,g,h,i]
                                                                        for j in range(10):
                                                                            if j not in list_index_j:
                                                                                Number = [0 for _ in range(10)]
                                                                                Number[a] = 0
                                                                                Number[b] = 1
                                                                                Number[c] = 2
                                                                                Number[d] = 3
                                                                                Number[e] = 4
                                                                                Number[f] = 5
                                                                                Number[g] = 6
                                                                                Number[h] = 7
                                                                                Number[i] = 8
                                                                                Number[j] = 9
                                                                                list_number.append(number_convertor(Number))                                                                             
    return list_number


l = fonction()
l.sort()
print(l[999999])

#2783915460