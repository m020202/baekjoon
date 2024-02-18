n = int(input())
box = list(map(int,input().split()))
dp = [1] * n
ch = [[] for _ in range(n)]
for i in range(n):
    ch[i].append(box[i])

for i in range(1,n):
    mx = 0
    tmp = False
    for j in range(i):
        if box[i] > box[j]:
            if dp[j] >= dp[mx]:
                tmp = True
                mx = j
    if (tmp == True):
        dp[i] = dp[mx] + 1
        ch[i] = ch[mx].copy()
        ch[i].append(box[i])

mx = 0
for i in range(n):
    if dp[i] > dp[mx]:
        mx = i

print(len(ch[mx]))
for i in ch[mx]:
    print(i, end=' ')
