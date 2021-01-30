
# Assignment 5

"""
Define a method that accepts a list as an argument
and returns True if one of the first 4 elements
in the list is a 6. The list length may be less than 4.


first3([1, 2, 6, 3, 4]) → True
first3([1, 2, 3, 4, 6]) → False
first3([1, 2, 3, 4, 5]) → False

"""

def find_6(my_list,limit):

    '''
    search the first 'limit' elements. If any of them == 6 then return True.  Otherwise return False.
    '''

    if (limit > len(my_list)):
        limit = len(my_list)

    for i in range(limit):
        if (my_list[i] == 6):
         return(True)
    return(False)

print(find_6([1, 2, 3, 6],4))
print(find_6([1, 2, 3, 4, 6],4))
print(find_6([1, 2, 3, 6, 5],4))
print(find_6([1, 2, 3, 4, 6],5))





'''
def first3(numbers):

    end = len(numbers)

    if end > 4:
        end = 4

    for i in range(end): # loop over index 0,1,2,3
        if numbers[i] == 6:
            return True

    # if we get here, the loop is over and we didn't find a 6
    return False


print(first3([1,2,6,3,0,0])) # true
print(first3([1,2,3,3,0,6])) # false
print(first3([6])) # true
print(first3([])) # false
'''


























# Solution:

# def first3(numbers):
#     # First figure the end for the loop
#     end = len(numbers)
#     if end > 4:
#         end = 4
#
#     for i in range(end):  # loop over index [0, 1, 2, 3]
#         if numbers[i] == 6:
#             return True
#     return False
