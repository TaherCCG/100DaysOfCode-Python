from turtle import Turtle, Screen

tt = Turtle()
########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    tt.forward(10)
    tt.penup()
    tt.forward(10)
    tt.pendown()