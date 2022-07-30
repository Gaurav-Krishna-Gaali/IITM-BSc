def Binarysearch(A, key):
    A.sort()
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if (key == A[mid]):
            return mid
        if (key < A[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return 0


Binarysearch([2, 1, 3, 11, 4], 11)
