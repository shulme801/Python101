# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""
def string_match(str_a, str_b):
    '''
    DOCSTRING:
    '''
    str_a = str(str_a)
    str_b = str(str_b)

    # find the length of the shortest string
    shortest = min(len(str_a), len(str_b))
    count    = 0
    if (shortest >= 2):
        for i in range(shortest-1): # make 2 char substrings from pos {0,1}
            if (str_a[i:i+2] == str_b[i:i+2]):
                count +=1
    return(count)



print(string_match('xxcaazz','xxbaaz'))
print(string_match('abc','abc'))
print(string_match('abc','axc'))








'''
def string_match(a, b):

    # Figure out which string is shorter
    shorter = min(len(a), len(b))

    count = 0

    for i in range(shorter - 1):
        a_sub = a[i: i+2] # gives us substring of size 2
        b_sub = b[i: i+2]
        if a_sub == b_sub:
            count = count + 1

    return count
'''






























# Solution
# def string_match(a, b):
#     # Figure which string is shorter.
#     shorter = min(len(a), len(b))
#     count = 0
#
#     # Loop i over every substring starting spot.
#     # Use length-1 here, so can use char str[i+1] in the loop
#     for i in range(shorter - 1):
#         a_sub = a[i:i + 2]
#         b_sub = b[i:i + 2]
#         if a_sub == b_sub:
#             count = count + 1
#
#     return count
