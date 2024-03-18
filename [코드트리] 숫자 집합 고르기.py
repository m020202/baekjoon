import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int,input().split()))
box.insert(0,0)

def dfs(num,goal):
    if num == goal:
        return True
    else:
        ch[num] = 1
        cur = box[num]
        if ch[cur] == 0:
            return dfs(cur,goal)
        else:
            return False
        
ans = 0
lst = []
for i in range(1,n+1):
    ch = [0] * (n+1)
    if (dfs(box[i],i)):
        ans += 1
        lst.append(box[i])

print(ans)
lst.sort()
for i in lst:
    print(i, end=' ')
