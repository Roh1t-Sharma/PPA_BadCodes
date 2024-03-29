from abc import ABC, abstractmethod


# Abstract Product for Car
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass


# Abstract Product for Truck
class Truck(ABC):
    @abstractmethod
    def drive(self):
        pass


# Concrete Product for ElectricCar
class ElectricCar(Car):
    def drive(self):
        return "Driving an electric car"


# Concrete Product for GasolineCar
class GasolineCar(Car):
    def drive(self):
        return "Driving a gasoline car"


# Concrete Product for ElectricTruck
class ElectricTruck(Truck):
    def drive(self):
        return "Driving an electric truck"


# Concrete Product for GasolineTruck
class GasolineTruck(Truck):
    def drive(self):
        return "Driving a gasoline truck"


# Abstract Factory Interface
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_truck(self):
        pass


# Concrete Factory for Electric Vehicles
class ElectricVehicleFactory(VehicleFactory):
    def create_car(self):
        return ElectricCar()

    def create_truck(self):
        return ElectricTruck()


# Concrete Factory for Gasoline Vehicles
class GasolineVehicleFactory(VehicleFactory):
    def create_car(self):
        return GasolineCar()

    def create_truck(self):
        return GasolineTruck()


# Client code that uses the Abstract Factory
def client_code(factory: VehicleFactory):
    # Utilizes the factory to create abstract product instances
    car = factory.create_car()
    truck = factory.create_truck()
    print(car.drive())
    print(truck.drive())

if __name__ == "__main__":
    factory_type = "electric"  # Determines the type of factory to use
    if factory_type == "electric":
        factory = ElectricVehicleFactory()  # Concrete Factory instantiation
    else:
        factory = GasolineVehicleFactory()  # Alternative Concrete Factory instantiation

    client_code(factory)  # Pass the concrete factory to the client code
