import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int,input().split()))
box.sort()
m = int(input())
box2 = list(map(int,input().split()))

def binarySearch(lt,rt, cur):
    if (lt > rt):
        print(0)
    else:
        m = (lt + rt) // 2
        if box[m] == cur:
            print(1)
        elif box[m] > cur:
            binarySearch(lt,m-1,cur)
        else:
            binarySearch(m+1,rt,cur)

for i in box2:
    binarySearch(0,n-1,i)

