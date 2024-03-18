import sys
input = sys.stdin.readline
n = int(input())
ch = [0] * (n+1)

for i in range(2,n+1):
    for j in range(i*2,n+1,i):
        ch[j] = 1

cnt = 0
for i in range(2,n+1):
    if ch[i] == 0:
        cnt += 1

print(cnt)
