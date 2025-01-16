from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen for the Snake game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("CCG Snake Game")
screen.tracer(0)

# Create the snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh the food's position
        snake.extend()  # Extend the snake
        scoreboard.increase_score()  # Increase the score

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False  # End the game
        scoreboard.game_over()  # Display game over message

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display game over message

# Exit the screen when clicked
screen.exitonclick()
