myList = ['b','d','a','z','x']
anotherList = [1,2,3,4,5]
# Get a 'd','b','a' into a list
myList.sort()
myList.reverse()
newList = myList[2:]
print("\nThis is the sorted myList {0}\n".format(myList))
anotherList.reverse()

newList = newList + anotherList[2:]
print("\nThis is the newList {0}\n".format(newList))
