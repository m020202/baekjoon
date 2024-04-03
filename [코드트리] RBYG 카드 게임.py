import sys
import copy
box = []
for _ in range(5):
    a,b = map(str,input().split())
    b = int(b)
    box.append((a,b))

box.sort(key=lambda x : (x[0], x[1]))

# 같은 색, 연속적
if box[0][0] == box[-1][0] and box[-1][1] - box[0][1] == 4:
    print(box[-1][1] + 900)
    sys.exit(0)

dic = {}
for a,b in box:
    dic[b] = 0

for a,b in box:
    dic[b] += 1

# 4장의 숫자가 같을 때  
if len(dic.keys()) == 1:
    print(800+box[0][0])
elif len(dic.keys()) == 2:
    for i in dic:
        if dic[i] == 4:
            print(800 + i)
            sys.exit(0)

# 3장, 2장씩 숫자 같을 때
ans = 700
if (len(dic.keys())) == 2:
    for i in dic:
        if dic[i] == 3:
            ans += i * 10
        else:
            ans += i
    print(ans)
    sys.exit(0)

# 5장의 카드 색깔 같을 때
if box[0][0] == box[-1][0]:
    print(600 + box[-1][1])
    sys.exit(0)

# 5장의 카드 숫자가 연속적일 때
box2 = copy.deepcopy(box)
box2.sort(key= lambda x : x[1])

for i in range(4):
    if box[i][1] + 1 != box[i+1][1]:
        break
else:
    print(500 + box[-1][1])
    sys.exit(0)

# 5장 중 3장의 숫자가 같을 때
for i in dic.keys():
    if dic[i] == 3:
        print(400 + i)
        sys.exit(0)

# 5장 중 2장, 2장씩 숫자가 같을 때
ch = []
for i in dic.keys():
    if dic[i] == 2:
        ch.append(i)
if len(ch) == 2:
    ch.sort()
    print(ch[-1] * 10 + ch[0] + 300)
    sys.exit(0)

# 5장 중 2장만 같을 떄
elif len(ch) == 1:
    print(200 + ch[0])
    sys.exit(0)

print(100 + box2[-1][1])
