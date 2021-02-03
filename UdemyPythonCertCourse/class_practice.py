class Vehicle:
    '''
    DOCSTRING Example of class 
    '''

    # the following should not be changed.  It's meant to be static
    num_wheels = 4
    color = 'red'

    def __init__(self, body_type, make):
        self.vehicle_body  = body_type
        self.vehicle_make  = make

Vehicle.color = 'green'
car1  = Vehicle('jeep', 'toyota')
car2  = Vehicle('truck', 'mercedes')
car3  = Vehicle('sedan', 'mercedes')
car4  = Vehicle('sport', 'honda')
car5  = Vehicle('SUV', 'Lexus')
car5  = Vehicle('truck', 'ford')

# print(car1.vehicle_make)
# print(car2.vehicle_make)

print(type(car1))
car1.color = 'purple'
print(car1.color)
print(car4.color)