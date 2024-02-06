import copy, sys
n = int(input())
cur = list(map(int,input()))
goal = list(map(int,input()))
ans = -1

# 시작 스위치 누를 때
c1 = copy.deepcopy(cur)
c1[0] = 1 - c1[0]
c1[1] = 1 - c1[1]
cnt = 1

for i in range(1,n):
    if c1[i-1] == goal[i-1]:
        continue
    for j in range(i-1,i+2):
        if j == n:
            break
        c1[j] = 1 - c1[j]
    cnt += 1

if c1 == goal:
    ans = cnt


c1 = copy.deepcopy(cur)
cnt = 0

for i in range(1,n):
    if c1[i-1] == goal[i-1]:
        continue
    for j in range(i-1,i+2):
        if j == n:
            break
        c1[j] = 1 - c1[j]
    cnt += 1

if c1 == goal:
    if ans == -1:
        ans = cnt
    else:
        ans = min(ans,cnt)
    
print(ans)
