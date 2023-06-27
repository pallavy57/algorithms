# sort an array
# rotate and array by two
# create an array with the high and low of where the element is present
# show the array
def sorting_array(array):
    if (len(array) > 1):
        mid = len(array)//2
        r = array[:mid]
        p = array[mid:]

        sorting_array(r)
        sorting_array(p)

        i = j = k = 0
        while (i < len(r) and j < len(p)):
            if (r[i] > p[j]):
                array[k] = r[i]
                i = i + 1

            else:
                array[k] = p[j]
                j = j + 1

            k = k + 1

        while (j < len(p)):
            array[k] = p[j]
            j += 1
            k += 1

        while (i < len(r)):
            array[k] = r[i]
            i += 1
            k += 1


# Print the array
def printList(array):
    output = []
    for i in range(len(array)):
        output.append(array[i])
    return output


def rotate(arr, l, r):
    while (l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l = l + 1
        r = r - 1
    return arr


def rotate_by_two(arr, k):
    k = k % len(arr)

    # reverse the arr
    c = rotate(arr, 0, len(arr)-1)

    # revrse the arr from 0 to k -1
    l, r = 0, k - 1
    rotate(c, l, r)

    # revrse the arr from k to len(arr)-1
    l, r = k, len(arr)-1
    return rotate(c, l, r)


def reverseorder(arr):
    l = 0
    r = len(arr) - 1

    while (l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


def decidesortingdir(lists):
    isdesc = None
    left = 0
    right = left + 1
    while (left < len(lists)-1):
        if (lists[left] > lists[right]):
            isdesc = True
            left += 1
            right = left + 1
        else:
            isdesc = None
            return isdesc
    return isdesc


def lsearch(arr):
    # check if it is sorted if not then sort it
    sorting_array(arr)
    c = printList(arr)
    is_descnding = decidesortingdir(c)
    if (is_descnding == True):  # sorted in descending
        t = reverseorder(arr)
        # return thr ascending order list
        return t
    else:
        # return thr ascending order list
        return arr


def search_by_element(arr, ele):
    # return the range which has the element in ascending order
    r = lsearch(arr)
 # apply binary search on that half
    low = 0
    high = len(r) - 1
    mid = (high + low)//2
    while (low <= high):
        mid = (high + low)//2
        if (r[mid] == ele):
            return mid, r
        elif (r[mid] > ele):
            high = mid - 1
        elif (r[mid] < ele):
            low = mid+1
    return -1


# Driver program
if __name__ == '__main__':
    array = [44, 55, 2, 4, 13, 67, 90, 34, 487, 875, 244]


def comined_operations(array):
    # sort an array
    sorting_array(array)
    c = printList(array)
    # rotate and array by two
    q = rotate_by_two(c, 2)

    # # create an array with the high and low of where the element is present
    r = search_by_element(q, 33)
    if (r != -1):
        print(q[:r[1][r[0]]])


comined_operations(array)





def find_the_element(arr, x):
    i = 1
    while (i < len(arr)):
        if (arr[i] == x):
            return x
        else:
            i = i + 1


def main_func(arr, x):

    low = 0
    high = len(arr)-1
    mid = (low + high)//2

    if (x > arr[mid]):
        sorting_array(arr)
        c = printList(arr)
        return find_the_element(c, x)
    else:
        return find_the_element(arr, x)


arr = [65, 487, 78, 98, 99, 98, 98, 65, 87, 76, 26, 9999, 65465, 878]


def create_dynamic_array():
    lst = []
    # Works for 10, million records
    for q in range(1000000):
        lst.append(q)
    return lst


lists = create_dynamic_array()
y = 99844
d = main_func(lists, y)
print(lists[:d])
# what is a batch job
