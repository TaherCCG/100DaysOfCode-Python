from turtle import Turtle, Screen
import random

# Set up the initial race condition
is_race_on = False
# Create a screen for the race
screen = Screen()
screen.setup(width=500, height=400)
# Ask user to place their bet on a turtle
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
print(user_bet)
# List of colours for the turtles
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
# Starting Y positions for each turtle
y_position = (-100, -60, -20, 20, 60, 100)
# List to hold all turtles
all_turtles = []

# Create and position each turtle
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

# Start the race if the user has placed a bet
if user_bet:
    is_race_on = True

# Continue the race while it is on
while is_race_on:
    for new_turtle in all_turtles:
        # Check if a turtle has crossed the finish line
        if new_turtle.xcor() > 230:
            is_race_on = False
            winner = new_turtle.pencolor()
            # Check if the user's bet matches the winning turtle
            if winner == user_bet:
                print(f"You've won! The winner is {winner}!!")
            else:
                print(f"You lost! The winner is {winner}!!")

        # Move the turtle a random distance forward
        random_distance = random.randint(0, 10)
        new_turtle.forward(random_distance)

# Close the screen when clicked
screen.exitonclick()
