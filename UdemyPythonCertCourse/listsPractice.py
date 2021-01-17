"""
my_List = [1,2,3,4,5]
myVar = my_List.pop(0)
print("\nJust popped {0}".format(myVar))
# print(my_List)
my_List[0] = ['hello','goodbye']
my_List.append("This is a sentence")
print("\n my_List is now {0}\n".format(my_List))
sentence = my_List.pop()
print("\nJust popped my_List's last element and my_List is now {0}".format(my_List)+"\n")
print("\nAnd sentence is {0}".format(sentence))
myList = [4,5,3,1,2]
print("\nmyList is initially {0}\n".format(myList))
myList.sort()
howdy = myList.reverse()
print("\nAfter sort and reverse, my list is {0}\n".format(myList))
print("\nand the reverse function call returned {0}\n".format(howdy))
"""
# Try reverse and sort methods with string elements in the list
myList = ['a','c','q','ce','d','b','bq','qbed','qaed','z']
print("\nmyList is initially {0}\n".format(myList))
#
howdy = myList.sort()
print("\nAfter sort, my list is {0}\n".format(myList))
print("\nand the sort function call returned {0}\n".format(howdy))