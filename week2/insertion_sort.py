def insertionSort(L):
    n = len(L)
    if n<1:
        return L
    for i in range(n):
        j = i
        while(j>0 and L[j]< L[j-1]):
            (L[j], L[j-1]) = (L[j-1], L[j])
            j = j -1
    return L

#recursive approach
def insert(L, v):
    n = len(L)
    if n==0:
        return v
    if v >= L[-1]:
        return L+[v]
    else:
        return insert(L[:-1], v) + L[-1:]
    
def iSort(L):
    n = len(L)
    if n<1:
        return L
    L = insert(iSort(L[-1:]), L[-1])
    return L