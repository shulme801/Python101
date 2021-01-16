# Assignment 5:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    NOTE: chars variable can contain any even number of characters.
          the len() function can be used to figure out the length of a string

    Example:
    ---------------
    chars = "<[<||>]>"
    word = "mirror"
    result - should contain the following string: <[<|mirror|>]>

"""




# Your code below:
chars = "<<[]]]>" # this could be a very long string with an even length.
word = "Cool"
splitChar= int(len(chars)/2)
result = chars[:splitChar]+word+chars[splitChar:]
print("\nNew string is "+result+"\n")

# Expected Result Printed: <<[Cool]]]


































# Solution Below:
# size = len(chars)
# idx = int(size/2) # dividing results in a float datatype.
# print(chars[:idx] + word + chars[idx:])


