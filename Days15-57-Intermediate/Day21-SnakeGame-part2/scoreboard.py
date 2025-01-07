from turtle import Turtle

# Alignment and font settings for the scoreboard
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        """Initialise the scoreboard with a starting score of 0 and display it at the top of the screen."""
        super().__init__()
        self.score = 0
        self.color("purple")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard with the current score."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display 'GAME OVER' message in the centre of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.clear()
        self.update_scoreboard()
