def greet_person(person_name = "buddy"):
    """
        DOCSTRING: Print a personalized greeting.
        INPUT: person_name
        OUTPUT: hello...person_name
    """
    print("\nHello there {0}! How are you?\n".format(str(person_name)))

def remainder(dividend = 0, divisor = 1):
    """
        DOCSTRING: Divide dividend by divisor and return the remainder.
        INPUT: dividend: converted to int
        INPUT: divisor: converted to int
        OUTPUT: remainder: int
    """
    foo = int(dividend)
    bar = int(divisor)
    return(int(foo % bar))
    

print(greet_person.__doc__)
greet_person(99)
greet_person("Stephen")
print(remainder.__doc__)
print("\nHere's the remainder function, 42 mod 11 = {0}\n".format(remainder(42,11)))
print("\nTry divide by 0, 42 mod 0 = {0}\n".format(remainder(42,0)))