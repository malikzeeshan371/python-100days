from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
# making the snake to move
while game_is_on:
    screen.update()
    # deciding the speed of the snake
    time.sleep(0.10)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect colision in the wall
    if snake.head.xcor() > 430 or snake.head.xcor() < -430 or snake.head.ycor() > 430 or snake.head.ycor() < -430:
        game_is_on = False
        scoreboard.game_over()

    #Detect colision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


























screen.exitonclick()