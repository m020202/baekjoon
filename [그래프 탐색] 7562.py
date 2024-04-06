from collections import deque
import sys
input = sys.stdin.readline
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]
n = int(input())
box = []
for _ in range(n):
    l = int(input())
    x,y = map(int,input().split())
    xx, yy = map(int,input().split())
    ch = [[-1] * l for _ in range(l)]
    dQ = deque()
    dQ.append((x,y))
    ch[x][y] = 0
    while dQ:
        curX, curY = dQ.popleft()
        for i in range(8):
            nextX = curX + dx[i]
            nextY = curY + dy[i]
            if 0<=nextX<l and 0<=nextY<l:
                if ch[nextX][nextY] == -1:
                    ch[nextX][nextY] = ch[curX][curY] + 1
                    dQ.append((nextX,nextY))
                else:
                    if ch[nextX][nextY] > ch[curX][curY] + 1:
                        ch[nextX][nextY] = ch[curX][curY] + 1
                        dQ.append((nextX,nextY))
    
    box.append(ch[xx][yy])
for i in box:
    print(i)
