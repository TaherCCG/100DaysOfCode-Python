# Hirst Painitng Project

import turtle as turtle_module
import random

# Set the turtle screen to use RGB colors
turtle_module.colormode(255)

tt = turtle_module.Turtle()
tt.speed("fastest")
tt.penup()
tt.hideturtle()

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tt.setheading(225)
tt.forward(300)
tt.setheading(0)
number_of_dots = 100

for dot in range(1, number_of_dots + 1):
    tt.dot(20, random.choice(color_list))
    tt.forward(50)

    if dot % 10 == 0:
        tt.setheading(90)
        tt.forward(50)
        tt.setheading(180)
        tt.forward(500)
        tt.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
