# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""

def sum78(in_list):
    """
    DOCSTRING Return the sum of the numbers in the list, except ignore sections of
              numbers starting with a 7 and extending to the next 8. Note that this code
              correctly handles the situation when a list is passed in whose first element is 8.
              The instructor's solution does not handle this situation.
              This function uses a comprehension to turn all the list element into integers.
              If the list passed in has 0 elements, it returns 0.
              I still need to modify the function to reject input of non-numbers (e.g., print(sum78(['foo','bar']))).

    """
    sum = 0
    num_list = [int(x) for x in in_list if (x>0)]
   
    range7 = False
    for i in range(len(num_list)):
        if (num_list[i] == 7):
            range7 = True

        if (not range7 and num_list[i] !=8):
            sum += num_list[i]

        if (range7 and num_list[i] == 8):
            range7 = False
            
    return(sum)
    
print(sum78([1, 2.2, 2]))
print(sum78([1, 2, 2, 7, 99, 99, 8]))
print(sum78([1, 1, 7, 8, 2]))
print(sum78([7]))
print(sum78([8]))
print(sum78([8,1]))
print(sum78([7,8]))
print(sum78([7,88,8]))



"""
# Solution:

# def sum78(nums):
#     sum = 0
#     inRange = False
#
#     for i in range(len(nums)):
#         if nums[i] == 7:
#             inRange = True
#
#         if not inRange:
#             sum += nums[i]
#
#         if inRange and nums[i] == 8:
#             inRange = False
#
#     return sum
"""
