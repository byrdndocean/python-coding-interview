# Can be used as key for hash map/set
myMap = {(1, 2): 3}
print(myMap[(1, 2)])


mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)


# Lists can't be keys
myMap[[3, 4]] = 5  # this won't work
