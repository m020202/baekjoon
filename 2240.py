t,w = map(int,input().split())
box = [int(input()) for _ in range(t)]

# 1에서 시작
dp = [[[0]*2 for _ in range(t)] for _ in range(w+1)]

cur = 0
for i in range(t):
    if box[i] == 1:
        cur += 1
        dp[0][i][0] = cur

for i in range(1,w+1):
    if box[0] == 1:
        dp[i][0][0] = 1


for i in range(1,w+1):
    for j in range(1,t):
        if box[j] == 1:
            dp[i][j][0] = max(dp[i][j-1][0] + 1, dp[i-1][j-1][1] + 1)
            dp[i][j][1] = max(dp[i][j-1][1], dp[i-1][j-1][0] + 1)
        else:
            dp[i][j][1] = max(dp[i][j-1][1] + 1, dp[i-1][j-1][0] + 1)
            dp[i][j][0] = max(dp[i][j-1][0], dp[i-1][j-1][1] + 1)


mx = 0
for i in range(w+1):
    for j in range(t):
        mx = max(mx,max(dp[i][j]))

# 2에서 시작
dp = [[[0]*2 for _ in range(t)] for _ in range(w)]

cur = 0
for i in range(t):
    if box[i] == 2:
        cur += 1
        dp[0][i][1] = cur

for i in range(1,w):
    if box[0] == 2:
        dp[i][0][1] = 1


for i in range(1,w):
    for j in range(1,t):
        if box[j] == 1:
            dp[i][j][0] = max(dp[i][j-1][0] + 1, dp[i-1][j-1][1] + 1)
            dp[i][j][1] = max(dp[i][j-1][1], dp[i-1][j-1][0] + 1)
        else:
            dp[i][j][1] = max(dp[i][j-1][1] + 1, dp[i-1][j-1][0] + 1)
            dp[i][j][0] = max(dp[i][j-1][0], dp[i-1][j-1][1] + 1)

for i in range(w):
    for j in range(t):
        mx = max(mx,max(dp[i][j]))

print(mx)
