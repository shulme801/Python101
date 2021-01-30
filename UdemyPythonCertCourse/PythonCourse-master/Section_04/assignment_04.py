# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""
def grow_string(my_str):
    grown = ""
    for i in range(len(my_str)):
        grown = grown+my_str[:i+1]
        print('iteration {0}. string is {1}'.format(i,grown))
        
    return(grown)

print(grow_string('Code'))
print(grow_string(''))
print(grow_string('a'))













'''
def grow_string(str):

    result = ""

    for i in range(len(str)):
        result = result + str[:i + 1]

    return result

print(grow_string("Imtiaz"))

'''





























# Solution:

# def grow_string(str):
#   result = ""
#   # On each iteration, add the substring of the chars 0..i
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result

