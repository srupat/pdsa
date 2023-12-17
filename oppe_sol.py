def find_first_occurence(A, k):
    low = 0
    high = len(A) - 1
    while high >= low:
        mid = (high + low) // 2

        if A[mid-1] < A[mid] and A[mid] == k:
            return mid
        
        if A[mid] < k:
            low = mid + 1

        else:
            high = mid - 1

    return -1

def peak_unimodal(A):
    low = 0
    high = len(A) - 1
    while high>= low:
        mid = (high + low) // 2

        if A[mid-1] < A[mid] > A[mid + 1]:
            return mid
        
        if A[mid-1] < A[mid]:
            low = mid + 1

        else:
            high = mid -1

    return -1

# print(find_first_occurence([1,1,1,1,2,2,2,3,3,3,3,3,4,4], 2))

print(peak_unimodal([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]))