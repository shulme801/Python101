# Assignment 1

"""

Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True

"""

def twelver(a, b):
    if (a == 12) or (b == 12) or (a + b == 12):
        return(True)
    else:
        return(False)

print(twelver(3, 12))
print(twelver(4, 9))
print(twelver(9,3))
print("That's all, folks!")








def twelver(a, b):
    return (a == 12 or b == 12 or a+b == 12)
































# Solution:
# def twelver(a, b):
#   return (a == 12 or b == 12 or a+b == 12)