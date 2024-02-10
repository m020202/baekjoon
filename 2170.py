import heapq
n = int(input())
ans = 0
hp = []
for _ in range(n):
    x,y = map(int,input().split())
    heapq.heappush(hp,(x,y))

lt, rt = heapq.heappop(hp)

while hp:
    x,y = heapq.heappop(hp)
    if rt < x:
        ans += (rt-lt)
        lt = x
        rt = y
    else:
        rt = max(rt,y)

ans += (rt - lt)
print(ans)

