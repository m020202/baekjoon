t = int(input())
for _ in range(t):
    cur = list(map(str,input()))
    lt = 0
    rt = len(cur)-1
    tmp = False
    ans = True
    num = 0
    while(lt < rt):
        if cur[lt] == cur[rt]:
            lt += 1
            rt -= 1
        else:
            if tmp == True:
                ans = False
                break
            else:
                if cur[lt+1] == cur[rt]:
                    tmp = True
                    lt += 2
                    rt -= 1
                elif cur[lt] == cur[rt-1]:
                    tmp = True
                    lt += 1
                    rt -= 2
                else:
                    ans = False
                    break
    
    if ans == False:
        num = 2
    elif ans == True and tmp == False:
        num = 0
    elif ans == True and tmp == True:
        num = 1
    
    if num == 2:
        lt = 0
        rt = len(cur)-1
        tmp = False
        ans = True
        num = 0
        while(lt < rt):
            if cur[lt] == cur[rt]:
                lt += 1
                rt -= 1
            else:
                if tmp == True:
                    ans = False
                    break
                else:
                    if cur[lt] == cur[rt-1]:
                        tmp = True
                        lt += 1
                        rt -= 2
                    elif cur[lt+1] == cur[rt]:
                        tmp = True
                        lt += 2
                        rt -= 1
                    else:
                        ans = False
                        break
        
        if ans == False:
            num = 2
        elif ans == True and tmp == False:
            num = 0
        elif ans == True and tmp == True:
            num = 1
    print(num)
