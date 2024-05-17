import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
D = [[-1] * n for _ in range(n)]

for _ in range(m):
    i,j,k = map(int,input().split())
    i -= 1
    j -= 1
    if D[i][j] == -1:
        D[i][j] = k
    else:
        D[i][j] = min(D[i][j],k)

for i in range(n):
    D[i][i] = 0

for k in range(n):
    for i in range(n):
        if D[i][k] == -1:
            continue
        for j in range(n):
            if D[k][j] != -1:
                if D[i][j] == -1:
                    D[i][j] = D[i][k] + D[k][j]
                else:
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])

for i in range(n):
    for j in range(n):
        if D[i][j] == -1:
            print(0,end=' ')
        else:
            print(D[i][j],end= ' ')
    print()
