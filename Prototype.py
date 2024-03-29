import copy


class Employee:
    def __init__(self, _name, _role, _department):
        self.name = _name
        self.role = _role
        self.department = _department

    def clone(self):
        return copy.copy(self)

    def deepclone(self):
        return copy.deepcopy(self)


# Creating a prototype
prototype = Employee("John Doe", "Manager", "IT")

# List to store employees
employees = []

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        role = input("Enter employee role: ")
        department = input("Enter employee department: ")

        # Create a new employee by cloning the prototype
        new_employee = prototype.clone()
        new_employee.name = name
        new_employee.role = role
        new_employee.department = department

        employees.append(new_employee)
        print("\nEmployee added successfully.")

    elif choice == "2":
        if not employees:
            print("\nNo employees found.")
        else:
            print("Employees:")
            for employee in employees:
                print(f"\nName: {employee.name}, Role: {employee.role}, Department: {employee.department}")

    elif choice == "3":
        print("\nExiting...")
        break

    else:
        print("\nInvalid choice. Please try again.")
