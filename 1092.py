n = int(input())
box = list(map(int,input().split()))
box.sort()
m = int(input())
ship = list(map(int,input().split()))
ship.sort()

ch = []
for i in box:
    ch.append([0,i])

ans = 0
while ship:
    cur = ship.pop()
    for i in ch:
        if i[1] >= cur:
            i[0] += 1
            break
    else:   
        ans = -1
        break
    ch.sort(key = lambda x : (x[0],-x[1]))

if ans == -1:
    print(-1)
else:
    print(ch[-1][0])
