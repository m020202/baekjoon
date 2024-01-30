import copy
import sys
n,m = map(int,input().split())
box = []
cctv = []
ans = sys.maxsize

for _ in range(n):
    box.append(list(map(int,input().split())))

def finding(box):
    global ans
    cnt = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                cnt += 1
    ans = min(ans,cnt)
    
def v5(x,y,cnt,box2):
    box = copy.deepcopy(box2)
    for i in range(x-1,-1,-1):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(x+1,n):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(y-1,-1,-1):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    for i in range(y+1,m):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    
    if cnt == len(cctv)-1:
        finding(box)
        return
    num,i,j = cctv[cnt+1]
    if num == 1:
        v1(i,j,cnt+1,box)
    elif num == 2:
        v2(i,j,cnt+1,box)
    elif num == 3:
        v3(i,j,cnt+1,box)
    elif num == 4:
        v4(i,j,cnt+1,box)
    else:
        v5(i,j,cnt+1,box)

def v4(x,y,cnt,box2):    
    box = copy.deepcopy(box2)
    for i in range(x-1,-1,-1):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(y-1,-1,-1):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    for i in range(y+1,m):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    
    box = copy.deepcopy(box2)
    for i in range(x-1,-1,-1):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(x+1,n):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(y+1,m):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    
    box = copy.deepcopy(box2)
    for i in range(x+1,n):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(y-1,-1,-1):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    for i in range(y+1,m):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)

    box = copy.deepcopy(box2)
    for i in range(x-1,-1,-1):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(x+1,n):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(y-1,-1,-1):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    
def v3(x,y,cnt,box2):
    box = copy.deepcopy(box2)
    for i in range(x-1,-1,-1):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(y+1,m):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)

    box = copy.deepcopy(box2)
    for i in range(x+1,n):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(y+1,m):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    
    box = copy.deepcopy(box2)
    for i in range(x+1,n):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(y-1,-1,-1):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)

    
    box = copy.deepcopy(box2)
    for i in range(x-1,-1,-1):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(y-1,-1,-1):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    

def v2(x,y,cnt,box2):
    box = copy.deepcopy(box2)
    for i in range(x-1,-1,-1):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    for i in range(x+1,n):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    
    box = copy.deepcopy(box2)
    for i in range(y-1,-1,-1):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    for i in range(y+1,m):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    
    
def v1(x,y,cnt,box2):
    box = copy.deepcopy(box2)
    for i in range(x-1,-1,-1):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    
    box = copy.deepcopy(box2)
    for i in range(x+1,n):
        if box[i][y] == 0:
            box[i][y] = -1
        elif box[i][y] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    
    box = copy.deepcopy(box2)
    for i in range(y-1,-1,-1):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    
    box = copy.deepcopy(box2)
    for i in range(y+1,m):
        if box[x][i] == 0:
            box[x][i] = -1
        elif box[x][i] == 6:
            break
    if cnt == len(cctv)-1:
        finding(box)
    else:
        num,i,j = cctv[cnt+1]
        if num == 1:
            v1(i,j,cnt+1,box)
        elif num == 2:
            v2(i,j,cnt+1,box)
        elif num == 3:
            v3(i,j,cnt+1,box)
        elif num == 4:
            v4(i,j,cnt+1,box)
        else:
            v5(i,j,cnt+1,box)
    

for i in range(n):
    for j in range(m):
        if box[i][j] == 0 or box[i][j] == 6:
            continue
        cctv.append((box[i][j],i,j))

if (len(cctv) > 0):
    cur,i,j = cctv[0]

    if (cur == 1):
        v1(i,j,0,box)
    elif cur == 2:
        v2(i,j,0,box)
    elif cur == 3:
        v3(i,j,0,box)
    elif cur == 4:
        v4(i,j,0,box)
    else:
        v5(i,j,0,box)
else:
    finding(box)

print(ans)
