import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
box = [[0] * n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cur = 0
ansX = 0
ansY = 0

box[n//2][n//2] = 1

dQ = deque()
dQ.append((n//2-1, n//2, 0, 2))
while dQ:
    x,y,dir,cnt = dQ.popleft()
    box[x][y] = cnt
    if cnt == m:
        ansX = x
        ansY = y
    
    nextDir = (dir + 1) % 4
    xx = x + dx[nextDir]
    yy = y + dy[nextDir]
    if 0<=xx<n and 0<=yy<n:
        if (box[xx][yy] == 0):
            dQ.append((xx,yy,nextDir,cnt+1))
        else:
            if 0<=x+dx[dir]<n and 0<=y+dy[dir]<n:
                dQ.append((x + dx[dir], y + dy[dir], dir, cnt+1))


for i in range(n):
    for j in range(n):
        print(box[i][j], end=' ')
    print()
print(ansX+1,ansY+1)


        
    
