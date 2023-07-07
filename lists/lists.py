# find the second largest element in an array


def getSecondlargest(arr):
    # check if array is empty
    if (len(arr) == 0):
        return None
    unique = removeduplicates(arr)
    largest = getlargest(unique)
    print("largest", largest)
    removedArray = removeLargest(arr, largest)
    return getlargest(removedArray)


def removeLargest(arr, largest):
    size = len(arr)
    for i in range(size):
        for j in range(1, size):
            if (i >= size):
                i = 0
            if (j >= size):
                j = 0
            if (arr[i] == largest):
                del [arr[i]]
                size = len(arr)
    return arr


def getlargest(arr):
    res = None
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                res = arr[i]
            else:
                res = arr[j]
    print(res)
    return res


def findOcc(arr, x):
    l = 0
    r = len(arr)
    while l <= r:
        mid = (l + r) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return arr[mid]
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        # If x is smaller, ignore right half
        else:
            r = mid - 1
    # If we reach here, then the element
    # was not present
    return -1


def removeduplicates(arr):
    size = len(arr)
    for i in range(size):
        for j in range(1, size):
            if (i >= size):
                i = 0
            if (j >= size):
                j = 0
            if (len(set(arr)) == len(arr)):
                return arr
            if (arr[i] == arr[j]):
                if (arr.count(arr[j]) > 1):
                    del [arr[j]]
                    size = len(arr)


array = [876786, 876786, 88979, 7687]
print(getSecondlargest(array))


# check if the list is sorted
def checkIfSorted(arr):
    l = 0
    r = len(arr)
    mid = (l+r)//2


array = [876786,  88979, 7687, 876786]
arr2 = [76, 87]

print((array + arr2) * 2)
print(checkIfSorted(array))
# rotate a list by one


def leftRotate(l, d):
    for i in range(0, d):
        l.append(l.pop(0))


l = [10, 20, 30, 40, 50]
d = 3
leftRotate(l, d)


############ max sum difference #################
def maxsum(arr):
    res, max_end = arr [0]
    for i in range(1, len(arr)):
        max_end = max(max_end + arr[i], arr[i])
        res = max(max_end, arr[i])
    return res    


arr = [-3, 8, -2, 4, -5, 6]
print(maxsum(arr))
