# rotate the array

def reverseArr(arr, l, r):
    arr[l], arr[r] = arr[r], arr[l]
    return arr


def rotate_array(arr, rotating_factor):
    if (rotating_factor == 0):
        return -1
    rotating_factor = rotating_factor % len(arr)

    reverseArr(arr, 0, rotating_factor - 1)
    reverseArr(arr, rotating_factor, len(arr)-1)
    reverseArr(arr, 0, len(arr)-1)
    return 1

# Find the minimum element in the array.
# Now, if the array is sorted and then rotated,
# then all the elements before the minimum element will be in increasing order
# and all elements after the minimum element will also be in increasing order.
# Check if all elements before the minimum element are in increasing order.
# Check if all elements after the minimum element are in increasing order.
# Check if the last element of the array is smaller than the starting element,
#  as this would make sure that the array has been rotated at least once.
# If all of the above three conditions satisfies then print YES otherwise print NO


def findMinMaxIndex(arr):
    base_ele = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if (arr[i] < base_ele):
            base_ele = arr[i]
            min_index = i
    return min_index


def findMaxIndexDiff(arr):
    max_index_diff = -1
    for i in range(0, len(arr)):
        for j in range(0, len(arr[::-1])):
            if (arr[j] > arr[i] and max_index_diff < (j-i)):
                max_index_diff = j-i

    return max_index_diff
# Utility Functions to get max
# and minimum of two integers


def max(a, b):
    if (a > b):
        return a
    else:
        return b


def min(a, b):
    if (a < b):
        return a
    else:
        return b


def maxIndexDiff(arr, n):
    maxDiff = 0
    LMin = [0] * n
    RMax = [0] * n

    # Construct LMin[] such that
    # LMin[i] stores the minimum
    # value from (arr[0], arr[1],
    # ... arr[i])
    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])

    # Construct RMax[] such that
    # RMax[j] stores the maximum
    # value from (arr[j], arr[j + 1],
    # ..arr[n-1])
    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(arr[j], RMax[j + 1])

    # Traverse both arrays from left
    # to right to find optimum j - i
    # This process is similar to
    # merge() of MergeSort
    i, j = 0, 0
    maxDiff = -1
    while (j < n and i < n):
        if (LMin[i] <= RMax[j]):
            maxDiff = max(maxDiff, j - i)
            j = j + 1
        else:
            i = i + 1

    return maxDiff


def maxIndexDiff(arr, n):
    maxDiff = -1
    for i in range(0, n):
        j = n - 1
        while (j > i):
            if arr[j] > arr[i] and maxDiff < (j - i):
                maxDiff = j - i
            j -= 1

    return maxDiff


def checkRotatedAndSorted(arr):
    isSortedAndRotated1 = False
    isSortedAndRotated2 = False
    eles = findMinMaxIndex(arr)

    for i in range(0, eles):
        if (arr[i] < arr[i+1]):
            isSortedAndRotated1 = True

    for i in range(eles, len(arr)-1):
        if (arr[i] < arr[i+1]):
            isSortedAndRotated2 = True

    if (arr[len(arr)-1] < arr[eles - 1] and isSortedAndRotated1 and isSortedAndRotated2):
        return True
    else:
        return False


# array = [65, 6, 74, 94, 56, 89, 9, 63, 75, 25, 34, 68, 93, 48, 16]
# array = [1, 10]
# array = [70, 83 ,82, 39,81]
array = [82, 63, 44, 74, 82, 99, 82]
print(checkRotatedAndSorted(array))

# rotating_factor = 1
# rotate_array = rotate_array(array, rotating_factor)
# max_index_diff = findMaxIndexDiff(array)
# print(max_index_diff)
# arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
# n = len(array)
# maxDiff = maxIndexDiff(array, n)
# print(maxDiff)
n = len(array)
# maxDiff = maxIndexDiff(array, n)
# print(maxDiff)



