from collections import deque
E = [5,4,3,2,1]

def merge(f,mid,l):  
    global E
    left = E[f:mid+1]
    right = E[mid+1:l+1]
    left = deque(left)
    right = deque(right)
    cur = f

    while (cur < l+1):
        if len(left) == 0:
            E[cur] = right.popleft()
            cur += 1
            continue
        elif len(right) == 0:
            E[cur] = left.popleft()
            cur += 1
            continue

        if left[0] < right[0]:
            E[cur] = left.popleft()
        else:
            E[cur] = right.popleft()
        cur += 1
    print(E)
    return 

def mergeSort(f,l):
    global E
    if f < l:
        mid = (f+l)//2
        mergeSort(f,mid)
        mergeSort(mid+1,l)
        merge(f,mid,l)
mergeSort(0,4)
print(E)

