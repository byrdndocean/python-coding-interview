# Reversing an Array
# nums = [1, 2, 3]
# nums.reverse()
# print(nums)


# Sorting an Array
# arr = [5, 4, 7, 3, 8]
# arr.sort()
# print(arr)

# Sorting an Array in descending order
# arr.sort(reverse=True)
# print(arr)


# Sorting a list of strings
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)


# Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)
