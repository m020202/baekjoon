n = int(input())
box = []
dic = {}
for _ in range(n):
    cur = list(map(str,input()))
    for i in cur:
        dic[i] = 0
    box.append(cur)

for i in box:
    for j in range(len(i)):
        cur = i[j]
        dic[cur] += pow(10,len(i)-1 - j)

ch = []
for i in dic:
    ch.append([dic[i],i])
ch.sort(reverse=True)

num = 9
for i in ch:
    dic[i[1]] = num
    num -= 1

ans = 0

for i in box:
    for j in range(len(i)):
        cur = i[j]
        ans += (dic[cur] * pow(10,len(i) - 1 - j))

print(ans)
