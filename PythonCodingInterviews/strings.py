# Strings are similar to arrays
# s = "abc"
# print(s[0:2])


# Strings are immutable
# This won't work
# s[0] = "A"


# So this creates a new string
# s += "def"
# print(s)


# Valid numeric strings can be converted into integers
# print(int("123") + int("123"))

# And numbers can be converted to strings
# print(str(123) + str(123))


# In rare cases you may need the ASCII value of a character
# print(ord("a"))
# print(ord("b"))


# Combine a list of strings (with an empty string delimiter)
strings = ["ab", "cd", "ef"]
print("".join(strings))
