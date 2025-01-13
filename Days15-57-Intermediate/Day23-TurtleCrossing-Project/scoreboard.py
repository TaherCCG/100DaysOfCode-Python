"""
Scoreboard class for the turtle crossing game, handles level display and game over message.
"""

from turtle import Turtle

# Define font
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """
        Initialise the scoreboard, set the level to 1 and prepare the display position.
        """
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard with the current level.
        """
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """
        Increase the level by 1 and update the scoreboard.
        """
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Display the 'GAME OVER' message at the center of the screen.
        """
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
