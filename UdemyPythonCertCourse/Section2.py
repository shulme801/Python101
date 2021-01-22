import re

my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['john', 'robert'], 'banana'], 'd']
my_list[6][2][1] = 'joe'
print("\nHere's the new name {0}\n".format(my_list[6][2][1]))
newStr = str(my_list)
print("\nHere's newStr {0}".format(newStr))
myTuple = (1, 2, 3, "Some Data", [1, 2, 3])
myTuple[4][1] = 99
print(myTuple[4][1])
print("\nmyTuple is now {0}\n".format(myTuple))
