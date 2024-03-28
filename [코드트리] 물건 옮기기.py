import sys
input = sys.stdin.readline
n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
dic = {}
for i,j in box:
    dic[i] = -1

ans = 0
for i,j in box:
    if dic[i] == -1:
        dic[i] = j
    else:
        if dic[i] != j:
            ans += 1
            dic[i] = j

print(ans)
