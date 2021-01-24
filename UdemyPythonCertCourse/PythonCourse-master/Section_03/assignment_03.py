# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
# Your Code Below:

def multi_merge(in_list,in_string):
    return(in_list+in_string.split()+list(in_string))

print(multi_merge([5,4,3,2,1,0],"Why do fools fall in love\n?"))



















'''
def multi_merge(list_a, str):
    return list_a + str.split() + list(str)

print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))
'''

























# Solution:

# def multi_merge(list_a, str):
#     return list_a + str.split() + list(str)
#
# print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))
