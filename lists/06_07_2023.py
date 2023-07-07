
# linear Approach
def findFirstAndLast(arr, n, x):
    new_arr = [0]*n
    count = 0
    first = -1
    last = -1
    for i in range(n):
        if (arr[i] == x):
            count = count + 1
            new_arr[i] = count
            first = i
            break
    for i in range(n):
        if (arr[i] == x):
            count = count + 1
            new_arr[i] = count
            last = i

    return first, last


# array = [1, 3, 5, 5, 5, 5, 67, 123 67, 125]
array = [1, 3, 5, 5, 5, 5, 7, 123, 123, 125]
x = 123
low = 0
high = len(array) - 1
findFirstAndLast(array, len(array), x)

# effeicient appraoch


# efficient linear Approach
def findFirstAndLastE(arr, n, x):
    fposition = -1
    lposition = -1
    left = 0
    right = n - 1
    mid = left + (right - left)//2
    count = 0
    for i in range(left, mid):
        if (arr[i] == x):
            if (fposition == -1):
                fposition = i

            count = count + 1
            lposition = fposition + (count-1)

    for i in range(mid, right):
        if (arr[i] == x):
            if (fposition == -1):
                fposition = i
            count = count + 1
            lposition = fposition + (count-1)

    print(fposition, lposition)


# array = [1, 3, 5, 5, 5, 5, 67, 123 67, 125]
array = [1, 3, 5, 5, 5, 5, 7, 123, 123,  125]
x = 123
print(findFirstAndLastE(array, len(array), x))


def binarySearch(arr, low, high,  n, x):

    if (high >= low):
        mid = low + (high - low) // 2
        if (arr[mid] == x):
            return mid
        if (arr[mid] > x):
            return binarySearch(arr, low, mid-1,  n, x)
        else:
            return binarySearch(arr, mid+1, high,  n, x)
    return -1


def countOnes(arr, low, high, n):
    first_ind = binarySearch(arr, low, high, n, 1)
    print(first_ind)
    if first_ind == -1:
        return 0
    count = 1
    for i in range(0, first_ind):
        if (arr[first_ind] == arr[i]):
            count = count + 1
    for i in range(first_ind + 1, n):
        if (arr[first_ind] == arr[i]):
            count = count + 1
    return count


array3 = [1, 1, 1, 1, 1, 1, 1]
n = len(array3)
x = 2
countOnes(array3, 0, n-1, n)


def countOccurrences(arr, n, x):
    first_ind = binarySearch(arr, 0, len(arr)-1, n, x)
    if first_ind == -1:
        return 0
    count = 1
    for i in range(0, first_ind):
        if (arr[first_ind] == arr[i]):
            count = count + 1
    for i in range(first_ind + 1, n):
        if (arr[first_ind] == arr[i]):
            count = count + 1
    return count


array2 = [1, 1, 2, 2, 2, 2, 3]
n = len(array2)
x = 2
countOccurrences(array2, n, x)
