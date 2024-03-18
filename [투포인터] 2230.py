import sys, math
input = sys.stdin.readline
INF = math.inf
n, m = map(int,input().split())
box = [int(input()) for _ in range(n)]
box.sort()

ans = INF

lt = 0
rt = 0

while (lt <= rt and rt < n):
    cur = box[rt] - box[lt]
    if cur == m:
        ans = m
        break
    elif cur < m:
        rt += 1
    else:
        ans = min(ans, cur)
        lt += 1
    
print(ans)
