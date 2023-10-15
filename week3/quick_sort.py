def quicksort(L, l, r): # sort L[l:r]
    if r - l <= 1:
        return L
    (pivot, lower, upper) = (L[l], l+1, r+1)
    for i in range(l+1, r):
        if L[i]>pivot:
            upper+=1
        else:
            (L[i], L[lower]) = (L[lower], L[i])
            (lower, upper) = (lower+1, upper+1)
    #move pivot between lower and upper parts
    (L[l], L[lower-1]) = (L[lower-1], L[l])
    lower-=1

    quicksort(L, l, lower)
    quicksort(L, lower+1, upper)

    return L