# Assignment 4:
"""
In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
"""

my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]

my_list[2][0][3] = "x"
my_list[3]= "television"
print(my_list)

old_tuple = my_list.pop(2)
print(old_tuple)
el_1 = old_tuple[0]
print(el_1)











# Solution:
# my_list[2][0][3] = 'x'
# my_list[3] = 'Television'
# print(my_list)