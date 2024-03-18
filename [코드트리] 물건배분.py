import sys
input = sys.stdin.readline

n,m = map(int,input().split())
box = list(map(int,input().split()))

ans = 0
cnt = 0
for i in box:
    if cnt + i > m:
        ans += 1
        cnt = i
    else:
        cnt += i

print(ans+1)
