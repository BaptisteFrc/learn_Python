def even_subset_sum():
    nb_elements = int(input())+1
    List = list(map(int, input().split(" ")))
    List.append(0)
    for i in range(nb_elements):
        if List[i] != 0:
            for j in range(i+1,nb_elements):
                if (List[i] + List[j]) % 2 == 0:
                    if List[j] == 0:
                        return i+1
                    else:
                        return i+1, j+1
    return -1

    def even_subset_sum():
    nb_elements = int(input())
    List = list(map(int, input().split(" ")))
    for i in range(nb_elements):
        if List[i] % 2 == 0:
            return i+1
        else:
            for j in range(i+1,nb_elements):
                if (List[i] + List[j]) % 2 == 0:
                        return i+1, j+1
    return -1