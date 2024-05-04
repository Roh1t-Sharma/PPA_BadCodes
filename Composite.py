class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        print(f"File: {self.name}, Size: {self.size}kb")


class Directory:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, obj):
        self.children.append(obj)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()


# Usage:
f1 = File("File1.txt", 210)
f2 = File("File2.txt", 102)
d1 = Directory("Dir1")
d1.add(f1)
d1.add(f2)
d1.display()
