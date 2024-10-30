from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snakkke")
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")


gameon=True
while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #to detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #detect collison with wall
    if snake.head.xcor()>280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        gameon=False


    #to detect collision with its own tail
    for part in snake.parts:
        if part==snake.head:
            pass
        elif snake.head.distance(part)<10:
            gameon=False
            scoreboard.game_over()

screen.exitonclick()

