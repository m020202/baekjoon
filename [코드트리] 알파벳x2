box = list(map(str,input()))

ans = 0
ch1 = [0] * 26
for i in range(len(box)):
    cur = box[i]
    cnt = 0
    ch1[ord(cur) - 65] = 1
    ch = [0] * 26
    for j in range(i+1, len(box)):
        if box[j] == cur:
            break
        else:
            num = ord(box[j]) - 65
            if ch1[num] == 0:
                ch[num] += 1
                cnt += 1
                if ch[num] == 2:
                    cnt -= 2
    ans += cnt

print(ans)
