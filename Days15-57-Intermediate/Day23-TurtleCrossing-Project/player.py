"""
Player class for the turtle crossing game, handles player movement and position checks.
"""

from turtle import Turtle

# Define constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        """
        Initialise the player with a turtle shape, set its starting position and heading.
        """
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """
        Move the player up by a defined distance.
        """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """
        Move the player to the starting position.
        """
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """
        Check if the player has reached the finish line.
        
        Returns:
            bool: True if the player has crossed the finish line, False otherwise.
        """
        return self.ycor() > FINISH_LINE_Y
