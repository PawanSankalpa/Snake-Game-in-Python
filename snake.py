from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_COLOR = "white"
SNAKE_SHAPE = "square"

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self,position):
        new_segment = Turtle()
        new_segment.shape(SNAKE_SHAPE)
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        #add a new segment to the snake tail
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def reset(self):
        for segment in self.segments:
            segment.goto(10000,10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.move()


    def head_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def head_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def head_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def head_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_tail(self):
        new_segment = Turtle()
        new_segment.shape(SNAKE_SHAPE)
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()

        new_segment.goto(self.segments[-1])
        self.segments.append(new_segment)





