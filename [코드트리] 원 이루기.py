import sys
input = sys.stdin.readline

n = int(input())

cur = 1
for i in range(n-1):
    print(cur, end=' ')
    if cur == 1: cur = 2
    else: cur = 1

if cur == 2:
    print(2)
else:
    print(3)
