from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.goto(0, 400)
        self.color("white")
        self.up()

    def score_l(self):
        self.l_score += 1

    def score_r(self):
        self.r_score += 1

    def move(self):
        self.clear()
        self.goto(-100, 300)
        self.write(f"{self.l_score}", True, "center", ("Courier", 40, "normal"))
        self.goto(100, 300)
        self.write(f"{self.r_score}", True, "center", ("Courier", 40, "normal"))

    def gameover(self):
        self.home()
        self.write(f"GAME OVER", True, "center", ("Courier", 50, "normal"))
