import re

my_list = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', ['john', 'robert'], 'banana'], 'd']
my_list[6][2][1] = 'joe'
print("\nHere's the new name {0}\n".format(my_list[6][2][1]))
