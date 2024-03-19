import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
box = [[0] * n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cur = 0

ansX = 0
ansY = 0

def dfs(x,y,dir,cnt):
    global ansX, ansY
    box[x][y] = cnt
    if cnt == m:
        ansX = x
        ansY = y
    
    nextDir = (dir + 1) % 4
    xx = x + dx[nextDir]
    yy = y + dy[nextDir]
    if 0<=xx<n and 0<=yy<n:
        if (box[xx][yy] == 0):
            return dfs(xx,yy,nextDir,cnt+1)
        else:
            if 0<=x+dx[dir]<n and 0<=y+dy[dir]<n:
                return dfs(x + dx[dir], y + dy[dir], dir, cnt+1)

box[n//2][n//2] = 1
dfs(n//2-1, n//2, 0, 2)
for i in range(n):
    for j in range(n):
        print(box[i][j], end=' ')
    print()
print(ansX+1,ansY+1)


        
    
