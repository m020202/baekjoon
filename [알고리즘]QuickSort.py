E = [5,4,3,2,1]

def partitioning(S,p):
    L = []
    E = []
    G = []
    for i in range(len(S)):
        if S[i] < p:
            L.append(S[i])
        elif S[i] > p:
            G.append(S[i])
        else:
            E.append(S[i])
    return (L,E,G)

def quickSort(S,p):
    if len(S) == 1:
        return S
    L,E,G = partitioning(S,p)
    if len(L) > 1:
        L = quickSort(L,L[len(L)-1])
    if len(G) > 1:
        G = quickSort(G,G[len(G)-1])
    
    return L + E + G

print(quickSort(E,E[-1]))
