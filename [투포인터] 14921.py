import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int,input().split()))

lt = 0
rt = n-1
ans = box[lt] + box[rt]
while (lt < rt):
    cur = box[lt] + box[rt]
    if abs(ans) > abs(cur):
        ans = cur
    
    if cur < 0:
        lt += 1
    elif cur > 0:
        rt -= 1
    else:
        ans = 0
        break

print(ans)
