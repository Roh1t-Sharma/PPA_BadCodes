class Employee:
    def __init__(self, _name, _role, _department):
        self.name = _name
        self.role = _role
        self.department = _department

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

        new_employee = Employee(name, role, department)

        employees.append(new_employee)
        print("\nEmployee added successfully.")

    elif choice == "2":
        if not employees:
            print("\nNo employee found.")
        else:
            print("\nEmployees:")
            for employee in employees:
                print(f"\nName: {employee.name}, Role: {employee.role}, Department: {employee.department}")

    elif choice == "3":
        print("\nExiting...")
        break

    else:
        print("\n Invalid choice. Please try again.")
