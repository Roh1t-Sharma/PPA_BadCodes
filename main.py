class UserProfile:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def display_user(self):
        print(f"Name: {self.name}, Email: {self.email}, Age: {self.age}")

    def update_email(self, new_email):
        self.email = new_email
        print("Email updated to: ", self.email)

    def update_name(self, new_name):
        self.name = new_name
        print("Name updated to: ", self.name)

# Handling user operations
def add_user(name, email, age, users):
    user = UserProfile(name, email, age)
    users.append(user)
    print(f"Added: {name}")

def display_users(users):
    for user in users:
        user.display_user()

users = []
add_user("Rohit Sharma", "Rohit@example.com", 21, users)
add_user("User 2", "Sharma@example.com", 28, users)

# Updating user info directly
users[0].update_email("R_Sharma@mail.com")
users[1].update_name("Sharma Rohit")

display_users(users)
