# Initialize arr of size n with default value of 1
# n = 5
# arr = [1] * n
# print(arr)
# print(len(arr))


# Careful: -1 is not out of bounds
# it's the last value
# arr = [1, 2, 3]
# print(arr[-1])

# Indexing -2 is the second to last value, etc
# print(arr[-2])


# ///////////////////////////////////////////////////////////

# Sublists (aka slicing)
# arr = [1, 2, 3, 4]
# print(arr[1:3])
# print(arr[0:])

# ///////////////////////////////////////////////////////////

# Unpacking
# a, b, c = [1, 2, 3]
# print(a, b, c)


# ////////////////////////////////////////////////////////////////

# Looping through arrays
nums = [1, 2, 3]

# Using index
# for i in range(len(nums)):
#     print(nums[i])


# Without index
# for n in nums:
#     print(n)


# With index and value
# for i, n in enumerate(nums):
#     print(i, n)


# Loop through multiple arrays simultaneously with unpacking
# nums1 = [1, 3, 5]
# nums2 = [2, 4, 6]
# for n1, n2 in zip(nums1, nums2):
#     print(n1, n2)
