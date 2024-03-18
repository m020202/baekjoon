import sys
input = sys.stdin.readline
n,m = map(int,input().split())
box = list(map(int,input().split()))

lt = 0
rt = max(box)
ans = 0
while (lt + 1< rt):
    cur = (lt + rt) // 2
    cnt = 0
    for i in box:
        if i > cur:
            cnt += i - cur
    if cnt < m:
        rt = cur 
    elif cnt > m:
        lt = cur 
        ans = max(ans,cur)
    else:
        ans = cur
        break

print(ans)
