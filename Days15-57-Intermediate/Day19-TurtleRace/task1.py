from turtle import Turtle, Screen

tt = Turtle()
screen = Screen()


def move_forwards():
    tt.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
