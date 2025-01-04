import random
from turtle import Turtle, Screen

tt = Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tt.pensize(15)
tt.speed("fastest")

for _ in range(200):
    tt.color(random.choice(colours))
    tt.forward(30)
    tt.setheading(random.choice(directions))
