

# keep both the cursors as zero
# ktraverse through the arry and arr the two element and store it in a variable curr
# increment the right side cursor until curr > sum
# when curr > sum increment right side and remove the item from starting ponut

def calculate_sum(array, sum):
    r = 0
    l = 0
    curr = 0
    for ins in array:
        if (curr == sum):
            return array[l], array[r], curr
        if (curr < sum):
            curr = curr + array[r]
            r = r + 1
        if (curr > sum):
            curr = curr - array[l]
            l = l+1
    return array[l], array[r], curr


array = [1, 4, 20, 3, 10, 5]
sum = 33
print(calculate_sum(array, sum))


def lenOfLongSubarr(arr, N, K):
    # Variable to store the answer
    maxlength = 0
    subarray = {}
    for i in range(0, N):
        # Variable to store sum of subarrays
        Sum = 0
        for j in range(i, N):
            # Storing sum of subarrays
            Sum += arr[j]
            # if Sum equals K
            if (Sum == K):
                print(arr[j], arr[i])
             # Update maxLength
                maxlength = max(maxlength, j - i + 1)

    # Return the maximum length
    return maxlength,subarray


# Driver Code
# Given input
arr = [10, 5, 2, 7, 1, 9]
n = len(arr)
k = 15

# Function Call
print("Length = ", lenOfLongSubarr(arr, n, k))
