from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from setup import Setup
import time

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
paddle.goto(350, 0)

paddle2 = Paddle()
paddle2.goto(-350, 0)

ball = Ball()
timmy = Setup()
score = Score()

screen.listen()
screen.onkey(paddle.go_up, "k")
screen.onkey(paddle.go_down, "m")
screen.onkey(paddle2.go_up, "a")
screen.onkey(paddle2.go_down, "z")

function = True
while function:
    screen.update()
    time.sleep(0.05)
    ball.move()
    score.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()
    if ball.distance(paddle) < 50 and ball.xcor() > 340:
        ball.path()
    if ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.path()
    if ball.xcor() == 380:
        score.score_l()
    if ball.xcor() == -380:
        score.score_r()
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.home()
        ball.move()
    if score.r_score == 5 or score.l_score == 5:
        score.move()
        score.gameover()
        function = False
screen.exitonclick()
