import sys
input = sys.stdin.readline

n = int(input())

ch = [0] * (n+1)
ch[0] = 1
ch[1] = 1

for i in range(2,n+1):
    ch[i] = ch[i-1] + ch[i-2] + 1

print(ch[-1] % 1000000007)
