# UserProfile class focuses on user data, aligning with Single Responsibility Principle (SRP).
class UserProfile:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # DRY principle applied: Consolidates updating name and email into one method.
    # Also aligns with KISS by simplifying updates to user profiles.
    def update_profile(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email

    # Implements a simple string representation, keeping it simple (KISS).
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"

# UserProfileManager class adheres to the SRP by handling user collection management.
class UserProfileManager:
    def __init__(self):
        self.users = []  # Manages a list of UserProfile instances.

    # Adds a user to the list, following KISS and YAGNI by implementing just what is necessary.
    def add_user(self, name, email, age):
        user = UserProfile(name, email, age)
        self.users.append(user)
        print(f"Added: {name}")

    # Updates user information, adhering to DRY by reusing UserProfile's update_profile method.
    # Also respects the OCP by allowing future extensions without modifying this method.
    def update_user(self, index, name=None, email=None):
        if 0 <= index < len(self.users):
            self.users[index].update_profile(name, email)
            print(f"User {self.users[index].name}'s profile updated.")
        else:
            print("User not found.")

    # Displays all users, keeping the implementation straightforward (KISS)
    def display_users(self):
        for user in self.users:
            print(user)

# Implementing the refactored code with UserProfileManager
user_manager = UserProfileManager()
user_manager.add_user("Rohit Sharma", "Rohit@example.com", 21)
user_manager.add_user("User 2", "Sharma@example.com", 28)

# Updating user information in a more streamlined manner (DRY & KISS).
user_manager.update_user(0, email="R_Sharma@mail.com")
user_manager.update_user(1, name="Sharma Rohit")

# Displaying users, directly utilizing the __str__ method in UserProfile (KISS).
user_manager.display_users()
