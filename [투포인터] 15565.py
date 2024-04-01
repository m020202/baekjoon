import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
box = list(map(int,input().split()))
lt = 0
rt = 1
cnt = k
ch = deque()
ch.append(box[0])
ans = n + 1
if box[0] == 1:
    cnt -= 1

while (lt < n):
    if rt == n and cnt != 0:
        break
    if cnt == 0:
        ans = min(ans, len(ch))
        if box[lt] == 1:
            cnt += 1
        ch.popleft()
        lt += 1
    else:
        ch.append(box[rt])
        if box[rt] == 1:
            cnt -= 1
        rt += 1

if ans == n+1:
    print(-1)
else:
    print(ans)
