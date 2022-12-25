# Dict comprehension
# myMap = {i: 2*i for i in range(3)}
# print(myMap)


# Looping through maps
myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)
