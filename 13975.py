import heapq
t = int(input())

def func(hp):
    ans = 0
    while len(hp) > 1:
        cur = heapq.heappop(hp)
        cur2 = heapq.heappop(hp)
        num = cur + cur2
        ans += num
        heapq.heappush(hp,num)
    return ans

for _ in range(t):
    k = int(input())
    box = list(map(int,input().split()))
    hp = []
    for i in box:
        heapq.heappush(hp,i)
    print(func(hp))
