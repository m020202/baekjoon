from collections import deque
n = int(input())
box = list(map(str,input()))
num = [int(input()) for _ in range(n)]
dQ = deque(box)
stack = []
while dQ:
    cur = dQ.popleft()
    tot = 0
    if cur.isalpha():
        stack.append(num[ord(cur) - 65])
        continue
    if cur == '*':
        tot = stack.pop() * stack.pop()
    elif cur == '/':
        tmp = stack.pop()
        tot = stack.pop() / tmp
    elif cur == '+':
        tot = stack.pop() + stack.pop()
    else:
        tmp = stack.pop()
        tot = stack.pop() - tmp
    stack.append(tot)

ans = stack[-1]
ans = float(ans)
print("{:.2f}".format(ans))
