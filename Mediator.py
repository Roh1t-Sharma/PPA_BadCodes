# Mediator Interface
from abc import ABC, abstractmethod


# Defines the interface for the mediator
class ChatRoomMediator(ABC):
    @abstractmethod
    def send_text(self, user, message):
        pass


# Concrete Mediator
class ChatRoom(ChatRoomMediator):
    # Implements the mediator interface
    def send_text(self, user, message):
        # Displays the message from the user
        print(f"[{user.name}]: {message}")


# Colleague Interface
class User:
    # Initializes the user with a name and a reference to the mediator
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    # Sends a message through the mediator
    def send_text(self, message):
        self.mediator.send_text(self, message)


# Concrete Colleague
class ChatUser(User):
    # Initializes the chat user with a name and a reference to the mediator
    def __init__(self, name, mediator):
        super().__init__(name, mediator)


# Usage
if __name__ == "__main__":
    # Create a chat room (mediator)
    chatRoom = ChatRoom()

    # Create users and associate them with the chat room
    user1 = ChatUser("Rohit", chatRoom)
    user2 = ChatUser("Angel", chatRoom)

    # Loop to take user input and send messages
    while True:
        message1 = input(f"{user1.name}: ")
        user1.send_text(message1)

        message2 = input(f"{user2.name}: ")
        user2.send_text(message2)

        # Exit condition
        if message1.lower() == 'bye' or message2.lower() == 'bye':
            print("Exited Chat.")
            break
