class Component:
    """Abstract component class with a common interface for File and Directory."""
    def __init__(self, name):
        self.name = name

    def display(self):
        raise NotImplementedError("This method should be implemented by the subclass!")

class File(Component): # Leaf node
    """File class representing individual files."""
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def display(self):
        print(f"File: {self.name}, Size: {self.size}kb")

class Directory(Component): # Composite
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()

def create_component():

    component_type = input("Enter 'file' to create a file, or 'dir' to create a directory: ")
    name = input("Enter name: ")

    if component_type.lower() == 'file':
        while True:
            size_input = input("Enter size (in kb): ")
            try:
                size = int(size_input)
                break
            except ValueError:
                print(f"Invalid size '{size_input}'. Please enter a numeric value.")
        return File(name, size)
    elif component_type.lower() == 'dir':
        return Directory(name)
    else:
        print("Invalid type. Creating a directory by default.")
        return Directory(name)

def main(): # client
    root = Directory("Root")
    while True:
        print("\nCurrent structure:")
        root.display()
        choice = input("Do you want to add a component to the root directory? (yes/no): ")
        if choice.lower() != 'yes':
            break
        component = create_component()
        root.add(component)

    print("\nFinal structure of the project:")
    root.display()

if __name__ == "__main__":
    main()
