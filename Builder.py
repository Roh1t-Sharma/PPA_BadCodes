class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.engine = None
        self.color = None
        self.features = []

    def display_configuration(self):
        print("Car Configuration:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Engine: {self.engine}")
        print(f"Color: {self.color}")
        print(f"Features: {', '.join(self.features)}")

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def add_feature(self, feature):
        self.car.features.append(feature)
        return self

    def build(self):
        return self.car

def get_car_input():
    print("Build Your Custom Car")
    make = input("Enter car make (e.g., Toyota, Ford): ")
    model = input("Enter car model (e.g., Corolla, Mustang): ")
    engine = input("Enter engine type (e.g., V6, Electric): ")
    color = input("Enter car color: ")
    features = input("Enter additional features (comma separated, e.g., Sunroof, GPS, Heated seats): ").split(', ')

    return make, model, engine, color, features

# Example usage
while True:
    print("\nCar Builder System")
    print("1. Build Custom Car")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        make, model, engine, color, features = get_car_input()

        builder = CarBuilder()
        custom_car = (builder.set_make(make)
                              .set_model(model)
                              .set_engine(engine)
                              .set_color(color)
                              .add_feature(', '.join(features))
                              .build())

        custom_car.display_configuration()

    elif choice == "2":
        print("\nExiting...")
        break

    else:
        print("\nInvalid choice. Please try again.")
