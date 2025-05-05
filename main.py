from food import Food
from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard

"""constants"""
SCREEN_WIDTH = 600
SCREEN_LENGTH = 600

"""creating the screen"""
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_LENGTH)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

"""class naming"""
snake = Snake()
food = Food()
scoreboard = Scoreboard()

"""giving commands"""
screen.listen()
screen.onkey(snake.head_up, "Up")
screen.onkey(snake.head_down, "Down")
screen.onkey(snake.head_left, "Left")
screen.onkey(snake.head_right, "Right")

"""play"""
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    """ detect collision with food"""
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_the_score()
        scoreboard.update_scoreboard()
        food.refresh()

    """detect collision with wall"""
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        scoreboard.reset()
        snake.reset()

    """detect collision with tail"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()
