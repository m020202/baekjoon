import sys
from collections import deque
input = sys.stdin.readline
n,d,k,c = map(int,input().split())
box = [int(input()) for _ in range(n)]
lt = 0
rt = (k-1) % n
ch = [0] * n
ans = 0
while (ch[lt] == 0):
    if lt < rt:
        cur = box[lt:rt+1]
    else:
        cur = box[lt:] + box[:rt+1]
    cur += [c]
    dist = set(cur)
    ans = max(ans, len(dist))
    ch[lt] = 1
    lt = (lt + 1) % n
    rt = (lt + k - 1) % n

print(ans)
