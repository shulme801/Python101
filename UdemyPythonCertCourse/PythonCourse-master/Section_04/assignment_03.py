# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""
def sequence(my_list):
    num_list = len(my_list)-2
    for i in range(num_list):
        if ((my_list[i] == 1) and (my_list[i+1] == 2) and (my_list[i+2] ==3)):
            return(True)
    return(False)
print(sequence([1, 1, 2, 3, 1]))
print(sequence([]))
print(sequence([1, 1, 2, 4, 1]))
print(sequence([1, 1, 2, 1, 2, 3]))
print(sequence([1, 2]))
        










'''
def sequence(num_list):
    for i in range(len(num_list)-2):
        if num_list[i] == 1 and num_list[i+1] == 2 and num_list[i+2] == 3:
            return True

    return False
'''
# print(sequence([]))































# Solution:

# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False
