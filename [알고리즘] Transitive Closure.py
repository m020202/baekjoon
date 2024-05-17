# 플로이드 워샬 활용
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
D = [[0] * n for _ in range(n)]
for _ in range(m):
    i,j = map(int,input().split())
    D[i][j] = 1

for k in range(n):
    for i in range(n):
        if D[i][k] == 0:
            continue
        for j in range(n):
            if D[k][j] == 1:
                D[i][j] = 1
                
for i in D:
    print(i)
