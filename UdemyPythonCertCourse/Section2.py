import re

my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['john', 'robert'], 'banana'], 'd']
my_list[6][2][1] = 'joe'
print("\nHere's the new name {0}\n".format(my_list[6][2][1]))
newStr = str(my_list)
print("\nHere's newStr {0}".format(newStr))
myTuple = (1, 2, 3, "foobar", [1, 2, 3], "foobar")
# myTuple[3] = "foobar"
myTuple [4][1] = "foobar"
print("\nmyTuple is now {0}\n".format(myTuple))
count = myTuple.count("foobar")
print("\nNumber of 'foobars' is {0}\n".format(count))