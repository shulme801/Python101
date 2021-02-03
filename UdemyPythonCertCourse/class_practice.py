class Vehicle:
    '''
    DOCSTRING Example of class 
    '''

    vehicle_counter = 0

    def __init__(self, body_type, make):
        self.vehicle_body  = body_type
        self.vehicle_make  = make
        Vehicle.vehicle_counter += 1

Vehicle.color = 'green' # WRONG!!
car1  = Vehicle('jeep', 'toyota')
car2  = Vehicle('truck', 'mercedes')
car3  = Vehicle('sedan', 'mercedes')
car4  = Vehicle('sport', 'honda')
car5  = Vehicle('SUV', 'Lexus')
car6  = Vehicle('truck', 'ford')

# print(car1.vehicle_make)
# print(car2.vehicle_make)

print(type(car1))
car1.color = 'purple' #wrong
print(car1.color)
print(car4.color)
print(car5.vehicle_counter)