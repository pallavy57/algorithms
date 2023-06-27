
def binary_search(arr, low, high, x):
    
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        if(mid >= len(arr)):
            high = len(arr)
            return binary_search(arr, low, high, x)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
            return binary_search(arr, low, high, x)
        else:
            low = mid + 1
            return binary_search(arr, low, high, x)

    else:
        # Element is not present in the array
        return -1


def finitesearch(arr, x):
    i = 1
    listss = []
    while i < len(arr):
        if (arr[i] == x):
            return binary_search(arr, (i//2) + 1, i + 1, x)
        if (x % 2 == 0):
            i = i * 2
        else:
            i = i * 3

        # 31-> 33-> 67
    return binary_search(arr, i//2, i, x)


def create_dynamic_array():
    lst = []
    # Works for 10, million records
    for q in range(100):
        lst.append(q)
    return lst


lists = create_dynamic_array()
y=97
response = finitesearch(lists, y)
print(response)
if (response != -1):
    print(lists[:y])
