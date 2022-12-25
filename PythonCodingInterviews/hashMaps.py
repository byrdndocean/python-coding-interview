# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)

myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice": 90, "bob": 70}
print(myMap)
