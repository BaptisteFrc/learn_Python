List = []
for _ in range (int(input())):
    List.append(list(map(int, input().split(" "))))

product_max = 0
product = 0
list_coordonates = []
for k in range(0,20):
    for i in range(0,20):
        list_coordonates.append([k,i])
        if i <= 16 and [k,i+3] not in list_coordonates:
            product = List[k][i]*List[k][i+1]*List[k][i+2]*List[k][i+3]
            if product > product_max:
                product_max = product 
        if i <= 16 and k <= 16 and [k+3,i+3] not in list_coordonates:
            product = List[k][i]*List[k+1][i+1]*List[k+2][i+2]*List[k+3][i+3]
            if product > product_max:
                product_max = product
        if k <= 16 and [k+3,i] not in list_coordonates:
            product = List[k][i]*List[k+1][i]*List[k+2][i]*List[k+3][i]
            if product > product_max:
                product_max = product
        if i >= 3 and k <= 16 and [k+3,i-3] not in list_coordonates:
            product = List[k][i]*List[k+1][i-1]*List[k+2][i-2]*List[k+3][i-3]
            if product > product_max:
                product_max = product
        if i >= 3 and [k,i-3] not in list_coordonates:
            product = List[k][i]*List[k][i-1]*List[k][i-2]*List[k][i-3]
            if product > product_max:
                product_max = product
        if i >= 3 and k >= 3 and [k-3,i-3] not in list_coordonates:
            product = List[k][i]*List[k-1][i-1]*List[k-2][i-2]*List[k-3][i-3]
            if product > product_max:
                product_max = product
        if k >= 3 and [k-3,i] not in list_coordonates:
            product = List[k][i]*List[k-1][i]*List[k-2][i]*List[k-3][i]
            if product > product_max:
                product_max = product
        if i <= 16 and k >= 3 and [k-3,i+3] not in list_coordonates:
            product = List[k][i]*List[k-1][i+1]*List[k-2][i+2]*List[k-3][i+3]
            if product > product_max:
                product_max = product
print(product_max)