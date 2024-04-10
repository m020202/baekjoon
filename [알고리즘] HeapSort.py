box = [0,10,7,4,3,5,2,1]
ans = [0] * len(box)

def promote(h,hStop, vacant):
    if h <= hStop:
        vacStop = vacant
    else:
        left = vacant * 2
        right = vacant * 2 + 1
        if box[left] >= box[right]:
            box[vacant] = box[left]
            vacStop = promote(h-1,hStop,left)
        else:
            box[vacant] = box[right]
            vacStop = promote(h-1,hStop,right)
        
    return vacStop

def bubbleHeap(root, k, vacant):
    if vacant == root:
        box[vacant] = k
    else:
        vacParent = vacant // 2
        if box[vacParent] <= k:
            box[vacant] = box[vacParent]
            bubbleHeap(root, k, vacParent)
        else:
            box[vacant] = k

def fixHeapFast(vacant,k,h):
    if h == 0:
        box[vacant] = k
    elif h == 1 and vacant * 2 > len(box)-1:
        box[vacant] = k
    elif h == 1 and vacant * 2 == len(box)-1:
        if k <= box[vacant*2]:
            box[vacant] = box[vacant*2]
            box[vacant*2] = k
    else:
        hStop = h // 2
        vacStop = promote(h,hStop,vacant)
        vacParent = vacStop // 2
        if (box[vacParent] <= k):
            box[vacStop] = box[vacParent]
            bubbleHeap(vacant,k,vacParent)
        else:
            fixHeapFast(vacStop,k,hStop)

def deleteMax(i):
    global box,ans
    ans[i] = box[1]
    box[1] = box[-1]
    box.pop()
    if len(box) > 1:
        k = box[1]
        vacant = 1
        h = -1
        cur = len(box) - 1
        while cur:
            cur //= 2
            h += 1
        fixHeapFast(vacant,k,h)


def heapsort():
    global box
    for i in range(len(box)-1, 0, -1):
        deleteMax(i)
heapsort()

print(ans)
