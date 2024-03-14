import sys
input = sys.stdin.readline

n,m = map(int,input().split())
box = list(map(int,input().split()))
box.sort()
tot = sum(box)

if (tot % m == 0): 
    print(tot/m)
else:
    print(tot//m + 1)
