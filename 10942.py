import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int,input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][0] = 1

# i 가 E, j 가 S
for i in range(1,n):
    for j in range(i,-1,-1):
        if i == j:
            dp[i][j] = 1
            continue
        
        if box[j] != box[i]:
            continue

        if j+1 == i:
            dp[j][i] = 1
            continue

        if dp[j+1][i-1] == 1:
            dp[j][i] = 1
        

for _ in range(m):
    s,e = map(int,input().split())
    s -= 1
    e -= 1

    print(dp[s][e])
