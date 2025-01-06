from turtle import Turtle

# Initial positions for the snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Distance the snake moves with each step
MOVE_DISTANCE = 10
# Direction constants in degrees
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        """Initialise the snake object with segments and set the head."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the snake with initial segments."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("purple")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Move the snake forward by moving each segment to the position of the previous one."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change the snake's direction to up if it is not currently heading down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down if it is not currently heading up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to left if it is not currently heading right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to right if it is not currently heading left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
