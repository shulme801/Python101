# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""
def last2(my_str):
    '''
    DOCSTRING: Count the number of times that a substring consisting of the last 2 chars is present in the rest of the string.
                Do not count the last two chars of the string as an occurrence.
                If the string has less than 3 chars, the number of times the last 2 chars can appear in the rest of the string is
                by definition 0.
    '''
    
    my_str    = str(my_str) #make sure we're dealing with an actual string
    str_count = 0
    str_len   = len(my_str)
    if (str_len > 3):
        str_len -= 2
        target_str = my_str[-2:]
        for i in range(0,str_len,1):
            sub_str = my_str[i:i+2]
            # print('sub_str = '+sub_str)
            # print('target_str = '+target_str)
            if (sub_str == target_str):
                str_count += 1
        
    return(str_count)

print(last2('bompshubompshubomp'))
print(last2('h1xxh1'))
print(last2('xaxxaxaxx'))
print(last2('axxxxaaxx'))
print(last2('axxxaaxx'))
print(last2('xx'))
print(last2('xxx'))


"""
def last2(str):

    if len(str) <= 2:
        return 0

    # last 2 chars can also be extracted with str[-2:]
    last2 = str[len(str) - 2:]
    count = 0

    for i in range(len(str) - 2):
        sub = str[i : i+2]
        if sub == last2:
            count = count + 1

    return count


print(last2('hixxhi')) #→ 1
print(last2('xaxxaxaxx')) #→ 1
print(last2('axxxxaaxx')) #→ 3
"""






















# Solution

# def last2(str):
#     # Screen out too-short string case.
#     if len(str) < 2:
#         return 0
#
#     # last 2 chars, can be written as str[-2:]
#     last2 = str[len(str) - 2:]
#     count = 0
#
#     # Check each substring length 2 starting at i
#     for i in range(len(str) - 2):
#         sub = str[i:i + 2]
#         if sub == last2:
#             count = count + 1
#
#     return count
