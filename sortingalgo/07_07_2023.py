# run a loop to compare the current element before it
# swap the current element  if it smaller previous element
# move ahead after the comparision is done


def function_two(array1):

    for i in range(0, len(array1)-1):
        min_ind = i
        for j in range(i + 1, len(array1)):
            if array1[j] < array1[min_ind]:
                min_ind = j
        array1[min_ind], array1[i] = array1[i], array1[min_ind]
    return array1


array1 = [2, 3, 4, 6, 66, 7, 1, 78]
# print(function_two(array1))

# run a loop to compare element after it to one iteration less than the list length
# if current element is smaller than min element update the min element
# swap the min element with i th element


def function_one(array1):
    for i in range(0, len(array1)):
        min_elem = array1[i]
        j = i-1
        while (j >= 0 and min_elem < array1[j]):
            array1[j+1] = array1[j]
            j = j - 1
        array1[j + 1] = min_elem

    return array1


array1 = [2, 3, 4, 6, 66, 7, 1, 78]

print(function_one(array1))
# have two lsts compare element in each index of two lists
# store the smaller element in the third list
# after one list is exhausted put all the other elements of the non exhausted list in the third list


def merge_arrays(array2, array3):
    array4 = [0] * (len(array2) + len(array3))
    i = 0
    j = 0
    k = 0

    while (i < len(array2) and j < len(array3)):
        if (array2[i] < array3[j]):
            array4[k] = array2[i]
        else:
            array4[k] = array3[j]
        i = i + 1
        j = j + 1
        k = k+1
    while (j < len(array3)):
        array4[k] = array3[j]
        j = j+1
    while (i < len(array2)):
        array4[k] = array2[i]
        i = i+1


array2 = [2, 3, 4]
array3 = [45, 56, 77, 89, 90]
merge_arrays(array2, array3)

# remove duplicates


def sortTheArray(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if (arr[j] < arr[min_index]):
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def removeDup(arr):
    returnedArr = sortTheArray(arr)
    arraytemp = [0] * len(returnedArr)
    i = 0
    k = 0
    j = len(arraytemp)-1
    while (i < len(arr)):
        if (arraytemp[k-1] == arr[i]):
            i = i+1
        else:
            arraytemp[k] = arr[i]
            i = i+1
            k = k+1

    while (j > 0):
        if (arraytemp[j] == 0):
            del arraytemp[j]
        j = j-1
    return arraytemp


# array8 = [2, 3, 4, 5, 1, 5]
array8 = [2, 3, 4, 5, 0, 0, 0, 1, 5]
print(removeDup(array8))
