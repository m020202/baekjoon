import sys
input = sys.stdin.readline
n = int(input())
box = []
def recursive(num):
    box.append(num)
    if (num == 369):
        return
    else:
        if num < 369:
            return recursive(num + 2)
        else:
            return recursive(num - 2)

if (n % 2 == 0):
    recursive(n+1)
else:
    recursive(n)

box.sort()
for i in box:
    print(i, end=' ')
