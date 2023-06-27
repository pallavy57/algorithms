def search(arr, n, x):
    low = 0
    high = len(arr) - 1
    while (low < high):
        mid = (high + low)//2
        # check if element is mid
        if arr[mid] == x:
            return x  # found the element

        # check which part of array is sorted
        if arr[mid] > arr[low]:  # left part is sorted
            if arr[low] <= x < arr[mid]:
                high = mid - 1  # change the high to the mid -1/ go to the left half
            else:
                low = mid + 1  # change the low to mid + 1 and go to the right half

        else:
            if (arr[mid] < x <= arr[high]):  # confirming the element is there in right half
                low = mid + 1
            else:
                high = mid - 1
    return -1            
