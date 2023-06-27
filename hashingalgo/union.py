# traverse through a list
# check if the element has appeared previously
# if yes then continue/igmore
# if not they look for that element in another array
array = [23, 34, 34, 23, 45, 66, 77, 56, 45]
array_compare = [23, 56, 45, 67, 45, 44]


def common_distinct_ele(array):
    res = []
    ress = [1] * len(array)
    print(ress)
    for i in range(len(array)):

        flag = False
        for j in range(0, i):
            if (array[i] == array[j]):
                ress[i] += 1
                flag = True
                break
        if (flag == True):
            for k in range(len(array_compare)):
                if (array[i] == array[k]):
                    res.append(array[i])
                    break

    return res, ress


response = common_distinct_ele(array)
# print(response)


# Insert all the elements in the set of the first array
# traveese through other array and search for that element in the set
# if yes then increment the count and remove the element from set


# two element as input and return count of distinct (duplicate are counted as once) elements in both arrays

# create a combined array and add elements to that array from both the arrays
# traverse this array and check if this element i is present in left side of the array or not
# if yes then break the loop
# if no then increment the counter


array22 = [2, 3, 8, 15, -8]

# find if the array contains a pairs which are sum of a given number
# traverse an array
# check the right side of the array for every element that it forms the given pair or not

def checkzerosum(array22, x):
    for i in range(len(array22)):
        for j in range(i+1 , len(array22)):
            if (array22[i] + array22[j] == x):
                return True
    return False

print(checkzerosum(array22, 17))

# check if there is a subarray(contingious element from the start) with sum 0 in the array
# run two loops and compare each element with next element
# check the sum of i and j if o then true or else false


# find the subarray with a sum given in the main array
