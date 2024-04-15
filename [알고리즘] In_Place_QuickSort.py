E = [5,4,3,2,1]

def partitioning(S,p):
    lt = 0
    rt = len(S) - 1
    while True:
        while S[lt] < S[p] and lt < len(S):
            lt += 1
        while S[rt] > S[p] and rt >= 0:
            rt -= 1
        if lt == rt:
            p = lt
            break
        else:
            tmp = S[lt]
            S[lt] = S[rt]
            S[rt] = tmp

    return (S[:p], S[p:])
        

# p = idx
def quickSort(S,p):
    if len(S) == 1:
        return S
    L,EUG = partitioning(S,p)
    if len(L) > 1:
        L = quickSort(L,len(L)-1)
    if len(EUG) > 1:
        EUG = quickSort(EUG,len(EUG)-1)
    
    return L + EUG

print(quickSort(E,len(E)-1))
