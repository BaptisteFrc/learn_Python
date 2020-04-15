from random import randint


l = []
for _ in range(30000):
    l.append(randint(-10000,10000))


l_classified = []
for i in range(len(l)):
    Min = min(l)
    l_classified.append(Min)
    l.remove(Min)

print(l_classified)