
def maxdf(arr):
    diff = []
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if (arr[i] > arr[j]):
                diff.append(arr[i] - arr[j])
            else:
                diff.append(arr[j] - arr[i])

    return max(diff)


array = [2, 1, 5, 3]
arry2 = [-10, 4, -9, -5]
maxdf(array)


def maxSubArray(arr):
    res = arr[0]
    for i in range(len(arr)):
        sum = 0
        for j in range(i+1, len(arr)):
            sum = sum + arr[j]
            res =max(res, sum)

    return res


arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
print(maxSubArray(arr))

# O(n) solution in Python3 for finding
# maximum sum of a subarray of size k

# Returns maximum sum in
# a subarray of size k.
def maxSum(arr, n, k):

	# k must be smaller than n
	if (n < k):
	
		print("Invalid")
		return -1
	
	# Compute sum of first
	# window of size k
	res = 0
	for i in range(k):
		res += arr[i]

	# Compute sums of remaining windows by
	# removing first element of previous
	# window and adding last element of
	# current window.
	curr_sum = res
	for i in range(k, n):
	
		curr_sum += arr[i] - arr[i-k]
		res = max(res, curr_sum)

	return res

# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
