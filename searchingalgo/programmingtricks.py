# # how to access the array and count frequqncy of each element in the array
# arr = [1, 2, 8, 3, 2, 2, 2, 5, 1]
# fr = [0] * len(arr)

# for i in range(0, len(arr)):
#     fr[arr[i]] = fr[arr[i]] + 1
# print(fr)


# # how to avoid list index out of range error in python
# languages = ['Python', 'JavaScript', 'Java']

# i = 0

# # while i <= len(languages):
# #     print(languages[i])
# #     i += 1

# # do not use =
# while i < len(languages):
#     print(languages[i])
#     i += 1

# # use range operator
# languages = ['Python', 'JavaScript', 'Java']
# for language in range(len(languages)):
#     print(languages[language])
# # how does recursion works

# # houses = ["Eric's house", "Kenny's house",
# #           "Kyle's house", "Stan's house", "Pallavi's house", "James's house"]


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

deliver_presents_recursively(houses)