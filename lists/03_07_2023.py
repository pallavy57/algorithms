import math

# Function to find the longest subarray


def longestEvenOddSubarray(a, n):

    # Length of longest
    # alternating subarray
    ans = 1
    longsubarray = []

    # Iterate in the array
    for i in range(n):
        cnt = 1

        # Iterate for every subarray
        for j in range(i + 1, n):
            if ((a[j - 1] % 2 == 0 and a[j] % 2 != 0)
                    or (a[j - 1] % 2 != 0 and a[j] % 2 == 0)):
                cnt = cnt+1
            else:
                break
        # store max count
        ans = max(ans, cnt)

    # Length of 'longest' can never be 1 since
    # even odd has to occur in pair or more
    # so return 0 if longest = 1
    if (ans == 1):
        return 0
    return ans


# Driver code
a = [1, 2, 3, 4, 5, 7, 8]

n = len(a)

longestEvenOddSubarray(a, n)

# get all the subarrays
# get the max sum of the subarrays
# get the max of max of sum of the subarrays


def return_sum_largest_subarray(array_02):
    res = array_02[0]
    for i in range(len(array_02)):
        curr = 0
        for j in range(1, len(array_02)):
            # to go to the 0 index after the last index reached
            index = (i+j) % len(array_02)
            curr = curr + array_02[j]
        if (curr > res):
            res = curr
    return res


array_02 = [5, -2, 3, 4]
# array_02 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
return_sum_largest_subarray(array_02)


def return_largest_subarray(array_02):
    compared_ele = array_02[0]
    base_ele = array_02[0]
    for i in range(len(array_02)):
        if (compared_ele > array_02[i]):
            compared_ele = compared_ele + array_02[i]
        elif (compared_ele == array_02[0]):
            compared_ele = base_ele
        else:
            compared_ele = array_02[i]

    return max(compared_ele, base_ele)


    # return subarrays
# array_02 = [5, -2, 3, 4]
array_02 = [11, 10, -20, 5, -3, -5, 8, -13, 10]
print(return_largest_subarray(array_02))


def overall_circular(array02):
    normal_max = 0
    arr_sum = 0
    for i in range(len(array02)):
        arr_sum += array02[i]
        array02[i] = -array02[i]
        normal_max = return_largest_subarray(array_02)
        circular_max = arr_sum + normal_max
        print(circular_max)
    return max(circular_max, normal_max)


array_02 = [8, -4, 3, -5, 4]
print(overall_circular(array_02))
