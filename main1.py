class Ball:
    # Constructor to initialise a new Ball with a position and speed.
    def __init__(self, position, speed):
        self.position = position  # Set the starting position of the Ball.
        self.speed = speed  # Set the speed of the Ball.
        # Print statement to indicate a new Ball has been created.
        print(f"Ball thrown from point {self.position} with the speed {self.speed}")

    # Method to simulate the movement of the Ball based on its speed.
    def move(self):
        self.position += self.speed  # Update the position of the Ball based on its speed.
        # Print the new position of the Ball after moving.
        print(f"Ball moved to {self.position}")

# A function to simulate throwing a Ball in the game.
def throw_Ball(position, speed):
    ball = Ball(position, speed)  # Create a new Ball instance with the given position and speed.
    ball.move()  # to call the move method to simulate the Ball's movement.

# Firing Balls with specific positions and speeds.
throw_Ball(0, 1)  # Throw the first Ball from position 0 with speed 1.
throw_Ball(2, 1)  # Throw the second Ball from position 2 with speed 1.
throw_Ball(3, 2)
