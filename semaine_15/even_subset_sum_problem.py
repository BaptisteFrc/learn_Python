def even_subset_sum():
    nb_elements = int(input())
    List = list(map(int, input().split(" ")))
    for i in range(nb_elements):
        if List[i] % 2 == 0:
            print(1)
            return i+1
    for i in range(nb_elements):
        for j in range(i+1,nb_elements):
            if (List[i] + List[j]) % 2 == 0:
                print(2)
                return i+1, j+1
        return -1
                    
for _ in range (int(input())):
    print(even_subset_sum())
