n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
ch = [0] * (n+1)
for i in range(n):
    cur = ch[i]
    t = box[i][0]
    p = box[i][1]
    
    if (i + t <= n):
        ch[i+t] = max(ch[i+t],cur + p)
    ch[i+1] = max(ch[i+1],ch[i])

print(max(ch))
