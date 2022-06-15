# Week6 grpa1

def merge(result, arr):
    (m, n) = (len(result), len(arr))
    (res, i, j, k) = ([], 0, 0, 0)
    while k < m+n:
        if m == i:
            res.extend(arr[j:])
            break
        elif n == j:
            res.extend(result[i:])
            break
        elif result[i] < arr[j]:
            res.append(result[i])
            i, k = i+1, k+1
        else:
            res.append(arr[j])
            j, k = j+1, k+1
    return res


def mergeKLists(L):
    result = []
    size = len(L)
    while(size != 0):
        result = merge(result, L[size-1])
        size -= 1
    return result


# week 6 grpa 2
def maxLessThan(root, K):
    max = root.value
    temp = root
    while (not temp.isempty()):
        if (temp.value and K < temp.value):
            temp = temp.left
        elif (temp.value and K >= temp.value):
            max = temp.value
            temp = temp.right
    if (K >= max):
        return max
    else:
        return None


# Week6 grpa3
def mh(a, k):
    l = 2*k+1
    r = 2*k+2
    mini = k
    if l < len(a) and a[l] > a[k]:
        mini = l
    if r < len(a) and a[r] > a[mini]:
        mini = r
    if mini != k:
        a[k], a[mini] = a[mini], a[k]
    mh(a, mini)


def min_max(arr):
    x = int((len(arr)//2)-1)
    for i in range(x, -1, -1):
        mh(arr, i)
