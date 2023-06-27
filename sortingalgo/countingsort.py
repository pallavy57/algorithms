
def Counting_Sort(arr):
    size = len(arr)
    output = [0] * size

    
# Initialize count array
    count = [0] * 10
    
 # Store the count of each elements in count array    
    for i in range(0, size):
        count[arr[i]] += 1
   
# Store the cummulative count    
    for i in range(1, 10):
        # print(count[i], count[i - 1] )
        count[i] += count[i - 1]


# place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1 

# Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]           


array = [9, 8, 4, 5, 8, 9, 3, 2, 3, -1]
print("The original array is: ", array)
Counting_Sort(array)
# print("Array after sorting is: ", array)

