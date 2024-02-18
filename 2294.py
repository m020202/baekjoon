n, k = map(int,input().split())
box = [int(input()) for _ in range(n)]
box.sort()
dp = [-1] * (k+1)
dp[0] = 0
for i in box:
    if i <= k:
        dp[i] = 1

for i in box:
    for j in range(i,k+1):
        if dp[j-i] == -1:
            continue
        
        if dp[j] == -1:
            dp[j] = dp[j-i] + 1
        else:
            dp[j] = min(dp[j-i]+1, dp[j])


print(dp[-1])
