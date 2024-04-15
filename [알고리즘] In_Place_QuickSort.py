
E = [4,3,1,2,5]
def partition(E,l,r,p):
    pivot = E[p]
    while True: 
        while (l < r):
            if E[l] >= pivot:
                break
            l += 1
        while (l < r):
            if E[r] < pivot:
                break
            r -= 1

        if l == r:
            tmp = E[l]
            E[l] = pivot
            E[p] = tmp
            p = l
            break
        else:
            if E[l] == pivot:
                p = r
            tmp = E[l]
            E[l] = E[r]
            E[r] = tmp
    return p
    
def quickSort(E,l,r):
    if l < r:
        p = (l + r) // 2
        p = partition(E,l,r,p)
        quickSort(E,l,p)
        quickSort(E,p+1,r)
        return

quickSort(E,0,4)
print(E)
