def my_sum(*args):
    '''
    DOCSTRING Playing with the unpack operator
    '''
    result = 0
    for x in args:
        result += x
    return result

def concatenate_keys(**kwargs):
    '''
    DOCSTRING Playing with unpacking a dictionary keys
    '''

    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs:
        result += arg
    return result

def concatenate_values(**kwargs):
    '''
    DOCSTRING Playing with unpacking a dictionary values
    '''

    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

list_1 = [1, 2, 3]
list_2 = [4, 5]
list_3 = [6, 7, 8,9]

print(my_sum(*list_1, *list_2, *list_3))
print(concatenate_keys(a="real", b="Python", c="Is", d="Great", e="!"))
print(concatenate_values(a="real", b="Python", c="Is", d="Great", e="!"))