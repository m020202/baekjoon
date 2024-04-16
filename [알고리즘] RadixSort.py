a = [48081, 97342, 90287, 90583, 53202, 65215, 78397]

def radixSort():
    for cur in range(6):
        bkt = [[] for _ in range(0,10)]
        while a:
            num = a.pop()
            div = num
            for _ in range(cur):
                div //= 10
            idx = div % 10
            bkt[idx].append(num)

        for i in range(9,-1,-1):
            while bkt[i]:
                a.append(bkt[i].pop())
        print(a)

radixSort()
print(a)
