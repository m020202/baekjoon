import sys
from collections import deque
input = sys.stdin.readline
n,d,k,c = map(int,input().split())
box = [int(input()) for _ in range(n)]
def checking(lt, rt):
    if lt > rt:
        for i in range(lt, n):
            if box[i] == c:
                return 0
        for i in range(0, rt + 1):
            if box[i] == c:
                return 0
    else:
        for i in range(lt, rt + 1):
            if box[i] == c:
                return 0
    return 1

cur = deque([])
for i in range(0,k):
    cur.append(box[i])
ans = (len(set(cur))) + checking(0,k-1)

lt = 1
rt = k % n
while (lt != 0):
    cur.popleft()
    cur.append(box[rt])
    dist = set(cur)
    cnt = (checking(lt, rt) + len(dist))
    ans = max(ans,cnt)
    lt  = (lt + 1) % n
    rt = (lt + k-1) % n

print(ans)
