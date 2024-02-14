t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    box = list(map(int,input().split()))
    m = int(input())
    dp = [[0] * (m+1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1
    
    for i in range(n):
        for j in range(box[i],m+1):
            dp[i][j] += dp[i][j-box[i]]
        
        if i != n-1:
            for j in range(m+1):
                dp[i+1][j] = dp[i][j]

    print(dp[-1][-1])
