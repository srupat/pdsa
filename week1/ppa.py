def find_Min_Difference(L, P):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i]< L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L

l = [3,1,6,2]
print(find_Min_Difference(l, 5))