from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.bgcolor('black')
my_screen.setup(width=800, height=600)
my_screen.title('Pong')
my_screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(key='Up', fun=r_paddle.up)
my_screen.onkey(key='Down', fun=r_paddle.down)

my_screen.onkey(key='w', fun=l_paddle.up)
my_screen.onkey(key='s', fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with r_Paddle and l_Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Detect when right paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Detect when left paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

my_screen.exitonclick()
