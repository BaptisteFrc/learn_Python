from math import prod

for _ in range(int(input())):
    nb_elements = int(input())
    List = list(map(int, input().split(" ")))
    counter = 0
    test = True
    while sum(List) == 0 or prod(List) == 0:
        if not test:
            for j in range(nb_elements):
                if List[j] > 0:
                    List[j] += 1
                    counter += 1
                    break
        
        if test: 
            for i in range (nb_elements):
                if List[i] == 0:
                    List[i] += 1
                    counter += 1
            test = False

    print (counter)
    