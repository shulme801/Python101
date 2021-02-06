class Vehicle:
    # this variable should not be changed outside of the class specification.
    # this is a class attribut
    vehicle_counter = 0

    def __init__ (self, body_type, make):
        self.vehicle_body = body_type
        self.vehicle_make = make
        Vehicle.vehicle_counter += 1

    def get_vehicle_count(self):
        return Vehicle.vehicle_counter

    def drive(self):
        print("Vehicle driving!")

class Truck(Vehicle):
    def drive(self):
        print("truck driving")
       