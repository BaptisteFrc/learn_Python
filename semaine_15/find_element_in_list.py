from random import randint


l = []
for _ in range(10000):
    l.append(randint(-10000,10000))
l.sort()

print(l)

#I want to find the index of n in the list "l"

boucle = False

while not boucle:
    
    try:
        n = int(input("saisissez votre nombre dans la liste ci-dessus: "))

        if n in l:

            lenght_list = len(l) - 1
            target = int(lenght_list/2) + 1 
            target_inf = 0
            target_sup = lenght_list 
            test = 0

            while l[target] != n:
                if l[target] > n:
                    transitor = target
                    target = int((target_inf + target)/2) + 1
                    target_sup = transitor
                else: 
                    transitor = target
                    target = int((target + target_sup)/2) + 1 
                    target_inf = transitor   
                if test == target:
                    if l[target] > n:
                        transitor = target
                        target = int((target_inf + target)/2)
                        target_sup = transitor
                    else: 
                        transitor = target
                        target = int((target + target_sup)/2)  
                        target_inf = transitor
                test = target
        else:
            print("votre nombre doit se trouver dans la liste affichée!")
            continue
    except ValueError:
        print("votre entrée doit être un nombre entier!")
    except IndexError:
        print("votre nombre doit se trouver dans la liste affichée!")
    except:
        print("arrête de chercher la merde et rentre un nombre")
    else:
        print("votre nombre se trouve à l'indice {}.".format(target))
        boucle = True