from turtle import Turtle

class Scoreboard(Turtle):
    """
    A class representing the scoreboard in the game.
    """
    def __init__(self):
        """
        Initialise the scoreboard's attributes.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard with the current scores.
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """
        Increase the left player's score by 1 and update the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increase the right player's score by 1 and update the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()
