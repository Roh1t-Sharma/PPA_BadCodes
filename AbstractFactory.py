from abc import ABC, abstractmethod


# Abstract base classes for Cars and Trucks
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass


class Truck(ABC):
    @abstractmethod
    def drive(self):
        pass


# Concrete implementations for Electric and Gasoline Cars
class ElectricCar(Car):
    def drive(self):
        return "Driving an electric car"


class GasolineCar(Car):
    def drive(self):
        return "Driving a gasoline car"


# Concrete implementations for Electric and Gasoline Trucks
class ElectricTruck(Truck):
    def drive(self):
        return "Driving an electric truck"


class GasolineTruck(Truck):
    def drive(self):
        return "Driving a gasoline truck"


# Abstract factory class
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_truck(self):
        pass


# Concrete factory for Electric Vehicles
class ElectricVehicleFactory(VehicleFactory):
    def create_car(self):
        return ElectricCar()

    def create_truck(self):
        return ElectricTruck()


# Concrete factory for Gasoline Vehicles
class GasolineVehicleFactory(VehicleFactory):
    def create_car(self):
        return GasolineCar()

    def create_truck(self):
        return GasolineTruck()


# Client code
def client_code(factory: VehicleFactory):
    car = factory.create_car()
    truck = factory.create_truck()
    print(car.drive())
    print(truck.drive())


if __name__ == "__main__":
    factory_type = "Gasoline"  # Could be "gasoline" or "electric"
    if factory_type == "electric":
        factory = ElectricVehicleFactory()
    else:
        factory = GasolineVehicleFactory()

    client_code(factory)
