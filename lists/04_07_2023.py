
def findMajority(arr):
    # take majority as first element
    majority_ele = 0
    count = 1
    for i in range(len(arr)):
        if (arr[majority_ele] == arr[i]):
            count = +1
        else:
            count -= 1
        if (count == 0):
            # set the new majority
            majority_ele = i
            count = 1
    return arr[majority_ele]


def printMajority(arr, majority_ele):
    count = 0
    for i in range(len(arr)):
        if arr[i] == majority_ele:
            count += 1
    if count > len(arr)/2:
        return arr[majortity_ele], count
    else:
        return -1


def printElementCount(array):
    new_array = [0]*len(array)
    for i in range(len(array)):
        for j in range(i, len(array)):
            if (array[i] == array[j]):
                new_array[i] = new_array[i] + 1
    return new_array


def printElementCount2(array):
    new_array = [0] * len(array)
    j = 0
    for i in range(1, len(array)):
        if (array[i] == new_array[j]):
            new_array[i] = new_array[j] + 1
        j += 1
    return new_array


def fillPrefixSum(arr, n):
    prefixSum = [0] * n
    prefixSum[0] = arr[0]

    # Adding present element
    # with previous element
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]
    return prefixSum


if __name__ == "__main__":

    # arr = [1, 1, 2, 1, 3, 5, 1]
    # majortity_ele = findMajority(arr)
    # print(printMajority(arr, majortity_ele))
    # array = [1, 1, 2, 1, 3, 5, 1]
    # print(printElementCount(array))

    arr = [10, 4, 16, 20]
    n = len(arr)

    prefixSum = [0 for i in range(n + 1)]

    print(fillPrefixSum(arr, n))

    array = [1, 1, 2, 1, 3, 5, 1]
    print(printElementCount2(array))
