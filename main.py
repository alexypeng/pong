from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

s = Screen()
s.tracer(0)

s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")

left = Paddle("left")
right = Paddle("right")
ball = Ball()

scoreboard = Scoreboard()

s.update()

s.listen()

s.onkeypress(fun=left.up, key="w")
s.onkeypress(fun=left.down, key="s")
s.onkeypress(fun=right.up, key="Up")
s.onkeypress(fun=right.down, key="Down")

game_is_on = True
while game_is_on:
    s.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce("wall")

    if (abs(ball.ycor() - right.ycor()) < 51 and 330 < round(ball.xcor()) < 332 or
            abs(ball.ycor() - left.ycor()) < 51 and round(ball.xcor()) == -330):
        ball.bounce("paddle")
        ball.increase_speed()

    if ball.xcor() > 380:
        ball.bounce("paddle")
        ball.centre()
        scoreboard.l_point()
    if ball.xcor() < -390:
        ball.bounce("paddle")
        ball.centre()
        scoreboard.r_point()

s.exitonclick()
