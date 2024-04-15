E = [5,4,3,2,1]
srt = [0] * len(E)

def merge(E,f,mid,l):
    i = f
    j = mid + 1
    cur = f
    while(i <= mid and j <= l):
        if E[i] <= E[j]:
            srt[cur] = E[i]
            i += 1
            cur += 1
        else:
            srt[cur] = E[j]
            j += 1
            cur += 1
    
    if i <= mid:
        rng = mid - i + 1
        for k in range(0,rng):
            srt[cur] = E[i]
            cur += 1
            i += 1
    if j < l:
        rng = l - j + 1
        for k in range(0,rng):
            srt[cur] = E[j]
            cur += 1
            j += 1
    
    for i in range(f,l+1):
        E[i] = srt[i]

def mergeSort(E,f,l):
    if f < l:
        mid = (f + l) // 2
        mergeSort(E,f,mid)
        mergeSort(E,mid+1,l)
        merge(E,f,mid,l)
        return
    
mergeSort(E,0,4)
print(E)
