from turtle import Turtle

class Ball(Turtle):
    """
    A class representing the ball in the game.
    """
    def __init__(self):
        """
        Initialise the ball's attributes.
        """
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 0.1
        self.y_move = 0.1
        self.move_speed = 0.1

    def move(self):
        """
        Move the ball to a new position.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverse the ball's y-direction.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverse the ball's x-direction and increase speed.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Reset the ball to the centre and bounce.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
