class Car:
    def drive(self):
        return "Driving a car"

class Truck:
    def drive(self):
        return "Driving a truck"

# Directly creating instances
vehicle_type = "truck"
if vehicle_type == "car":
    vehicle = Car()
elif vehicle_type == "truck":
    vehicle = Truck()

print(vehicle.drive())
