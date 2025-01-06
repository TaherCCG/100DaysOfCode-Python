from turtle import Screen
from snake import Snake
import time

# Set up the screen for the Snake game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("CCG Snake Game")
screen.tracer(0)

# Create a snake object
snake = Snake()

# Set up key bindings for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Pause the game for a short period

    # Move the snake
    snake.move()

# Exit the screen when clicked
screen.exitonclick()
