# Defines a Ball class for game balls with position and speed attributes.
class Ball:
    def __init__(self):
        # Initializes a ball with default position and speed.
        self.position = 0
        self.speed = 0

    # Method to set or reset ball's position and speed, and print its initialization.
    def initialize(self, position, speed):
        self.position = position
        self.speed = speed
        print(f"Ball thrown from point {self.position} with the speed {self.speed}")

    # Moves the ball according to its speed and prints its new position.
    def move(self):
        self.position += self.speed
        print(f"Ball moved to point {self.position}")

    # Resets the ball's attributes to their default values for reuse.
    def reset(self):
        self.position = 0
        self.speed = 0

# Manages a pool of Ball objects to minimize the creation and destruction of instances.
class BallPool:
    def __init__(self):
        # Lists to track available (unused) balls and balls currently in use.
        self.available_balls = []
        self.in_use_balls = []

    # Retrieves a ball from the pool or creates a new one if necessary.
    def get_ball(self, position, speed):
        if self.available_balls:
            # Reuses a ball if available, popping it from the available list.
            ball = self.available_balls.pop()
            print("Reusing existing ball.")
        else:
            # Creates a new ball if none are available for reuse.
            ball = Ball()
            print("Creating new ball.")
        # Initializes or reinitializes the ball with the given position and speed.
        ball.initialize(position, speed)
        # Marks the ball as in use by adding it to the in-use list.
        self.in_use_balls.append(ball)
        return ball

    # Returns a ball to the pool for future reuse.
    def release_ball(self, ball):
        # Removes the ball from the in-use list.
        self.in_use_balls.remove(ball)
        # Resets the ball to its default state.
        ball.reset()
        # Adds the ball back to the available list for future reuse.
        self.available_balls.append(ball)
        print("Ball released and available for reuse.")

# Creates a single instance of the BallPool to manage ball resources.
pool = BallPool()

# Function to simulate firing a ball, using the BallPool for resource management.
def throw_Ball(position, speed):
    # Retrieves a ball from the pool, initializing it with the specified position and speed.
    ball = pool.get_ball(position, speed)
    # Simulates moving the ball.
    ball.move()
    # Releases the ball back to the pool after use.
    pool.release_ball(ball)

# Simulates firing balls, demonstrating the reuse of ball objects.
throw_Ball(0, 1)
throw_Ball(2, 1)
throw_Ball(4, 1) # This may reuse a ball if one has been released.
