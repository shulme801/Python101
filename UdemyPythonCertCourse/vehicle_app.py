from machines.vehicle_stuff import Vehicle, Truck, Motorcycle

# car1   = Vehicle('sedan', 'Toyota')
truck1 = Truck("Big Rig", "Mercedes")
car1   = Vehicle("Sedan", "Chevy")
moto1  = Motorcycle("Sports", "Honda")

for v in [truck1, car1, moto1]:
    v.drive()

def perform_tasks(vehicle_object):
    vehicle_object.drive()

perform_tasks(truck1)
perform_tasks(moto1)
perform_tasks(car1)
