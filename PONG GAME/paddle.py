from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.up()

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 50)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 50)
