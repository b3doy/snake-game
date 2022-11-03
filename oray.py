from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
STEP_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Oray:
    def __init__(self):
        self.orays = []
        self.create()
        self.hulu = self.orays[0]

    def create(self):
        for pos in START_POS:
            self.add_oray(pos)
            

    def add_oray(self, pos):
        oray = Turtle(shape="square")
        oray.color("white")
        oray.up()
        oray.goto(pos)
        self.orays.append(oray)
    
    def extend(self):
        self.add_oray(self.orays[-1].position())


    def move(self):
        # Configure that last part is move forward first, then so on
        # to make sure that the snake is move forward directly
        # even it has to turn around.
        for oray_num in range(len(self.orays) - 1, 0, -1):
            x_baru = self.orays[oray_num - 1].xcor()
            y_baru = self.orays[oray_num - 1].ycor()
            self.orays[oray_num].goto(x_baru, y_baru)
        self.hulu.fd(STEP_FORWARD)
    
    def up(self):
        if self.hulu.heading() != DOWN:
            self.hulu.setheading(UP)

    def down(self):
        if self.hulu.heading() != UP:
            self.hulu.setheading(DOWN)

    def left(self):
        if self.hulu.heading() != RIGHT:
            self.hulu.setheading(LEFT)

    def right(self):
        if self.hulu.heading() != LEFT:
            self.hulu.setheading(RIGHT)