from collections import deque 

n = int(input())
box = []
for _ in range(n):
    box.append(int(input()))
box.sort()
dQ1 = deque()
dQ2 = deque()

for i in box:
    if i >= 0:
        dQ1.append(i)
    else:
        dQ2.append(i)

ans = 0
num = 0
tmp = False

while dQ1:
    cur = dQ1.pop()

    if (cur == 1):
        ans += cur
        continue

    if (tmp == True):
        ans += (cur * num)
        tmp = False
        continue
    
    if (cur > 1):
        if dQ1 and dQ1[-1] > 1:
            tmp = True
            num = cur
        else:
            ans += cur
    elif (cur == 0):
        if dQ2 and len(dQ2)%2 == 1:
                dQ2.pop()


while dQ2:
    cur = dQ2.popleft()
    if (tmp == True):
        ans += (cur * num)
        tmp = False
    else:
        tmp = True
        num = cur

if tmp == True:
    ans += num

print(ans)
