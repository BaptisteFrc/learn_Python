l = []
for _ in range(int(input())):
    l.append(int(input()))

str_l = [str(sum(l))[i] for i in range(10)]
print("{}{}{}{}{}{}{}{}{}{}".format(str_l[0],str_l[1],str_l[2],str_l[3],str_l[4],str_l[5],str_l[6],str_l[7],str_l[8],str_l[9]))


