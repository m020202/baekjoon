import sys
input = sys.stdin.readline

n,m = map(int,input().split())

def decimal(n,m):
    ch = [0] * (m+1)
    ch[1] = 1
    for i in range(2,m+1):
        for j in range(i*2, m+1, i):
            ch[j] = 1
    cnt = 0
    for i in range(n,m+1):
        if ch[i] == 0:
            cnt += 1

    return cnt

print(decimal(n,m))
