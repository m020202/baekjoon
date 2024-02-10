import heapq, sys
n = int(input())
hp = []
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    heapq.heappush(hp,(x1,y1,x2,y2))

# 현재 답에 들어있는 꽃의 시든 날짜
w = 0
z = 0
ans = []
tmp = True
while hp:
    x1,y1,x2,y2 = heapq.heappop(hp)
    if x1 < 3 or (x1 == 3 and y1 == 1):
        if w < x2 or (w == x2 and z < y2):
            w = x2
            z = y2
        continue
    else:
        heapq.heappush(hp,(x1,y1,x2,y2))
        break

if (w == 0 and z == 0):
    print(0)
    sys.exit()

if (w == 12):
    print(1)
    sys.exit()

ans.append((w,z))

# 임시로 시든 날짜가 가장 긴 꽃
tmpX = 0
tmpY = 0
tmp = True

while hp:
    x1,y1,x2,y2 = heapq.heappop(hp) 
    if x1 < w or (x1 == w and y1 <= z):
        tmp = False
        if tmpX < x2 or (tmpX == x2 and tmpY < y2):
            tmpX = x2
            tmpY = y2
    else:
        if (tmp == True):
            ans = []
            break
        tmp = True
        w = tmpX
        z = tmpY
        ans.append((w,z))
        if w == 12:
            break

        if x1 < w or (x1 == w and y1 <= z):   
            tmp = False        
            tmpX = x2
            tmpY = y2
        else:
            ans = []
            break


if ans:
    if ans[-1][0] != 12:
        if tmpX == 12:
            print(len(ans) + 1)
        else:
            print(0)
    else:
        print(len(ans))
else:
    print(0)

