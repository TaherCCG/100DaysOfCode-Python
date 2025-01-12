from turtle import Turtle

class Paddle(Turtle):
    """
    A class representing the paddle in the game.
    """
    def __init__(self, position):
        """
        Initialise the paddle's attributes and set its position.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """
        Move the paddle up by 20 units.
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Move the paddle down by 20 units.
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
