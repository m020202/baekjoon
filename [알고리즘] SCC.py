import sys
input = sys.stdin.readline

G = {}
R = {}
ans = {}
ch1 = {}
ch2 = {}

n = int(input())
box = list(map(str,input().split()))
box.sort()
for i in box:
    G[i] = []
    R[i] = []
    ans[i] = ''
    ch1[i] = 0
    ch2[i] = 0
for _ in range(n):
    cur = list(map(str,input().split()))
    G[cur[0]] += cur[2:]

stack = []
def DFS(cur):
    if ch1[cur] == 1:
        return
    ch1[cur] = 1
    for i in G[cur]:
        DFS(i)
    
    stack.append(cur)

def DFS2(cur, lead):
    if ch2[cur] == 1:
        return
    ch2[cur] = 1
    for i in R[cur]:
        DFS2(i,lead)
    ans[cur] = lead

for i in box:
    if ch1[i] == 0:
        DFS(i)

for i in stack:
    print(i, end= ' ')
print()

for i in G:
    for j in G[i]:
        R[j].append(i)

while (stack):
    cur = stack.pop()
    if ch2[cur] == 0:
        DFS2(cur,cur)

for i in ans:
    print(ans[i],end=' ')
