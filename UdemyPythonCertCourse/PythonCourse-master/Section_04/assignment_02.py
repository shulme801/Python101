# Assignment 2

"""
Create a method called pay_extra that accepts 2 parameters:
 working, and hour. This method will be used to decide whether
 an employee will receive extra pay or not. If an employee is working
 during the hrs of 8pm until 8am in the morning, that means they
 should be paid extra. In that situation the method should return true,
 otherwise it should return false.

 NOTE: the hour parameter should be from 0-23.
        So 8AM is hour 8, and 8PM is hour 20.

Example:
    pay_extra(True, 11) -> false
    pay_extra(False, 5) -> false
    pay_extra(True, 6)  -> true
"""

def pay_extra(working, hour):
    if (working):
        if (hour >= 20):
            return(True)
        elif (hour < 8):
            return(True)
        else:
            return(False)
    else:
        return(False)

print(pay_extra(True,11))
print(pay_extra(False, 5))
print(pay_extra(True, 6))
print(pay_extra(True, 21))
print(pay_extra(True, 8))






'''
def pay_extra(working, hour):
    return (working and (hour < 8 or hour > 20))
'''

























# Solution
# def pay_extra(working, hour):
#     return (working and (hour < 8 or hour > 20))