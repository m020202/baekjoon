n,k = map(int,input().split())
box = list(map(int,input().split()))

for _ in range(k):
    for i in range(n-1):
        if box[i+1] < box[i]:
            tmp = box[i]
            box[i] = box[i+1]
            box[i+1] = tmp
    
for i in box:
    print(i, end= ' ')
