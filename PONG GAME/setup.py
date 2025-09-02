from turtle import Turtle


class Setup(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,400)
        self.setheading(270)
        self.color("white")
        for _ in range(10):
            self.fd(50)
            self.up()
            self.fd(50)
            self.down()
        self.up()
        self.goto(-400, -300)
        self.down()
        self.goto(400, -300)
        self.goto(400, 300)
        self.goto(-400, 300)
        self.goto(-400, -300)
        self.up()
        self.goto(-100, 0)
        self.down()
        self.circle(100)
