import random
from turtle import Turtle, Screen

tt = Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tt.forward(100)
        tt.right(angle)

for shape_side_n in range(3, 10):
    tt.color(random.choice(colours))
    draw_shape(shape_side_n)