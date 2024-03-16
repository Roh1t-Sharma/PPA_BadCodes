from abc import ABC, abstractmethod


# Abstract base class for Vehicles
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        # Abstract method to be implemented by subclasses
        pass


# Concrete implementation of Vehicle for Car
class Car(Vehicle):
    def drive(self):
        # Implementation of driving behavior for a car
        return "Driving a car"


# Concrete implementation of Vehicle for Truck
class Truck(Vehicle):
    def drive(self):
        # Implementation of driving behavior for a truck
        return "Driving a truck"


# Abstract base class for VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        # Abstract factory method to create a vehicle
        pass


# Factory for creating Car instances
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()


# Factory for creating Truck instances
class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()


# Client code that uses factories to create vehicles
def client_code(factory: VehicleFactory):
    # The factory creates a vehicle instance
    vehicle = factory.create_vehicle()
    # Output the result of the vehicle's drive method
    print(vehicle.drive())


if __name__ == "__main__":
    vehicle_type = "bike"  # The type of vehicle to create
    if vehicle_type == "car":
        factory = CarFactory()  # Create a CarFactory instance
    elif vehicle_type == "truck":
        factory = TruckFactory()  # Create a TruckFactory instance

    client_code(factory)  # Pass the factory to the client code
