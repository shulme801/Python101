from machines.vehicle_stuff import Vehicle, Truck

# car1   = Vehicle('sedan', 'Toyota')
truck1 = Truck("Big Rig", "Mercedes")
truck2 = Truck("Small Rig", "Chevy")
truck3 = Truck("Big Rig", "Toyota")

print("Here's the vehicle count after truck3 is created {0}".format(truck3.get_vehicle_count()))
truck1.drive()