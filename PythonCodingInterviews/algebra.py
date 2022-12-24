# Division is decimal by default
import math
print(5/2)

# Double slash rounds down
print(5 // 2)

# CAREFUL: most languages round towards 0 by default so negative numbers will round down
print(-3 // 2)

# Workaround for rounding towards zero is to use decimal division and then convert to int.
print(int(-3 / 2))


# ///////////////////////////////////////////////////////////////////
# Modding is similar to most languages
print(10 % 3)

# Except for negative values
print(-10 % 3)

# To be consistent with other languages modulo
print(math.fmod(-10, 3))


# /////////////////////////////////////////////////////////////
# More math helpers
# Floor  (rounds down)
# Ceil  (rounds up)
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))


# ////////////////////////////////////////////////////////////////

# Max Integer
float("inf")

# Min Integer
float("-inf")


# Python numbers are infinite so they never overflow
print(math.pow(2, 200))

# But still less than infinity
print(math.pow(2, 200) < float("inf"))
