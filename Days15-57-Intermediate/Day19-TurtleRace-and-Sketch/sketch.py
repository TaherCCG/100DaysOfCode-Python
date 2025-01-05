# Etch-A-Sketch using the turtle module
from turtle import Turtle, Screen

tt = Turtle()
screen = Screen()

def move_forwards():
    """Move the turtle forward by 10 units."""
    tt.forward(10)

def move_backwards():
    """Move the turtle backward by 10 units."""
    tt.backward(10)

def turn_right():
    """Turn the turtle clockwise by 10 degrees."""
    tt.right(10)

def turn_left():
    """Turn the turtle anti-clockwise by 10 degrees."""
    tt.left(10)

def clear():
    """Clear the screen and reset the turtle to the home position."""
    tt.clear()
    tt.penup()
    tt.home()
    tt.pendown()

# Listen for key presses
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

# Close the screen when clicked
screen.exitonclick()
