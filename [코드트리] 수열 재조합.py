import sys, copy
input = sys.stdin.readline
n = int(input())
box = list(int(input()) for _ in range(n))
box2 = copy.deepcopy(box)
box2.sort(reverse=True)
stack = []
ans = []
for i in box:
    if stack and stack[-1] == i:
        ans.append("-")
        stack.pop()
        continue
    tmp = False
    while box2:
        cur = box2.pop()
        stack.append(cur)
        ans.append("+")
        if cur == i:
            tmp = True
            stack.pop()
            ans.append("-")
            break
    if tmp == False:
        print("NO")
        sys.exit(0)

for i in ans:
    print(i)
    
