# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# print(len(arr)-1)

# (//) is primarily used when you require an integer
# or need to return the smallest integer less than
# or equal to the input.

# if you have an array and you are adding an element but the length of the array exceeds, the count = count % len(arr)
# this will give the positions from the initials of the array and you can put the elements there


def reverlogic(arr, l, r):
    while (l < r):
        # swap the elements
        arr[l], arr[r] = arr[r], arr[l]
        l = l + 1
        r = r - 1
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8]


def reverse_arr(nums, k):
    a = []
    k = k % len(nums)
    l, r = 0, len(nums) - 1

    # while the end points have not swapped or met each other
    a = reverlogic(nums, l, r)

    # reverse the first k elements
    l, r = 0, k-1
    reverlogic(a, l, r)

    # reverse the len(Arr) - k element or rest elements
    l, r = k, len(nums)-1
    return reverlogic(a, l, r)


print(reverse_arr(arr, 4))
