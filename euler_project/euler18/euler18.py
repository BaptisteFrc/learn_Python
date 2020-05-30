from time import time 

start_time = time()

lines = {}
for i in range(15):
    lines[i+1] = list(map(int, input().split(" ")))

list_sum = []
Sum = 0
for a in range(2):
    for b in range(a,a+2):
        for c in range(b,b+2):
            for d in range(c,c+2):
                for e in range(d,d+2):
                    for f in range(e,e+2):
                        for g in range(f,f+2):
                            for h in range(g,g+2):
                                for i in range(h,h+2):
                                    for j in range(i,i+2):
                                        for k in range(j,j+2):
                                            for l in range(k,k+2):
                                                for m in range(l,l+2):
                                                    for n in range(m,m+2):
                                                        Sum = 75 + lines[2][a] + lines[3][b] + lines[4][c] + lines[5][d] + lines[6][e] + lines[7][f] + lines[8][g] + lines[9][h] + lines[10][i] + lines[11][j] + lines[12][k] + lines[13][l] + lines[14][m] + lines[15][n]
                                                        list_sum.append(Sum)

print(max(list_sum))
print(time() - start_time)