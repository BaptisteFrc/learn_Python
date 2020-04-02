list1 = [n for n in range(101)]

list2 = [n for n in range(10,21)]

list3 = [n**2 for n in range(101)]

list4 = [n**2 for n in range (101) if n**2<=100]

list5 = [n**3 for n in range (101) if n**2<=1000 and n % 3 != 0]

i = int(input())
POWER = [i**k for k in range(11)]
print(POWER)