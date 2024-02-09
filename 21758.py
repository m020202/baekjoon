n = int(input())
box = list(map(int,input().split()))
ans = 0
sum_box = sum(box)

# case 1 둘 다 왼쪽에서 오기
cur1 = 0
num = sum_box - box[0]
ch = 0
for i in range(1,n):
    ch += box[i]
    num1 = num - ch
    num2 = num - box[i]
    cur1 = max(cur1, (num1 + num2))

# case 2 둘 다 오른쪽에서 오기
cur2 = 0
num = sum_box - box[-1]
ch = 0
for i in range(n-2,-1,-1):
    ch += box[i]
    num1 = num - ch
    num2 = num - box[i]
    cur2 = max(cur2,(num1 + num2))

# case 3 양 쪽에서 오기
lt = box[1]
rt = sum_box - box[-1] - box[0]
cur3 = lt + rt
for idx in range(2,n-1):
    lt += box[idx]
    rt -= box[idx-1]
    cur3 = max(cur3, lt + rt)

ans = max(cur1,cur2,cur3)

print(ans)

