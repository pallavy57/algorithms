# houses = ["Eric's house", "Kenny's house",
#           "Kyle's house", "Stan's house", "Pallavi's house", "James's house"]


houses=[67, 76, -35, 87, 87]


def deliver_presents_recursively(houses):
    if (len(houses) > 1):
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

        i = j = k = 0

    #    store the smaller element in the k position of array
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                houses[k] = first_half[i]
                i += 1
            else:
                houses[k] = second_half[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in arr[k]
        while i < len(first_half):
            houses[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            houses[k] = second_half[j]
            j += 1
            k += 1


   
def deliver_presents_recursively2(houses):
    if (len(houses) > 1):
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]
        deliver_presents_recursively2(first_half)
        deliver_presents_recursively2(second_half)

        i = j = k = 0

    #   store the smaller element in the k position of array
        while i < len(first_half) and j < len(second_half):
            if first_half[i] > second_half[j]:
                houses[k] = first_half[i]
                i += 1
            else:
                houses[k] = second_half[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in arr[k]
        while i < len(first_half):
            houses[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            houses[k] = second_half[j]
            j += 1
            k += 1


deliver_presents_recursively(houses)
# print(houses)
array1 = [" "] * len(houses)
array2 = [" "] * len(houses)
m = len(houses)//2
arr1 = houses[m:]
arr2 = houses[:m]

kk = 0
while(kk < len(arr1)):
    deliver_presents_recursively2(arr1)
    deliver_presents_recursively(arr2)
    kk += 1
print(arr1,arr2)