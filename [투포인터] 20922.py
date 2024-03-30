import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
box = list(map(int,input().split()))
dic = {}
for i in box:
    dic[i] = 0

lt = 0
rt = 1
ans = 0
cur = [box[0]]
cur = deque(cur)
dic[box[0]] = 1
while (lt < n and rt < n):
    if dic[box[rt]] == k:
        ans = max(ans, len(cur))
        dic[box[lt]] -= 1
        lt += 1
        cur.popleft()
    else:
        cur.append(box[rt])
        dic[box[rt]] += 1
        rt += 1

ans = max(ans, len(cur))
print(ans)
