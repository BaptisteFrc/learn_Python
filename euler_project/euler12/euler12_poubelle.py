from math import sqrt

def transformer(n):
    l = []
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            l.append(i)
    for i in range(len(l)):
        if l[i]!=int(sqrt(n)):
            l.append(int(n/l[i]))
    return len(l)
        
def nb_triangulaire(n):
    return sum([i for i in range(1,n+1)])


n = 1
while nb_triangulaire(n)<=76576500:
    n +=1 
    
print(transformer(nb_triangulaire(n)))



 #print(transformer(76576500))