import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
num = n * m * k
ans = 1
def recursive(num):
    global ans
    if num == 0:
        return 
    else:
        cur = num % 10
        if cur != 0:
            ans *= cur
        return recursive(num//10)

recursive(num)
print(ans)
    
