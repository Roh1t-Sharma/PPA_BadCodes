# Base class for Car
class Car:
    def drive(self):
        return "Driving a car"

# Base class for Truck
class Truck:
    def drive(self):
        # Method to simulate driving a truck
        return "Driving a truck"

# Client code to create vehicle instances
vehicle_type = "truck"  # The type of vehicle to create
if vehicle_type == "car":
    vehicle = Car()  # Create an instance of Car
elif vehicle_type == "truck":
    vehicle = Truck()  # Create an instance of Truck

print(vehicle.drive())