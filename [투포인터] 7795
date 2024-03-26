import sys
input = sys.stdin.readline
box = []
for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    rt = 0
    lt = 0
    ans = 0
    while (lt < n):
        if rt == m:
            ans += rt
            lt += 1
            continue
        if a[lt] > b[rt]:
            rt += 1
        else:
            lt += 1
            ans += rt
    print(ans)
