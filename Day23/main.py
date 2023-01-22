from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

game_on = True

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.onkey(player.move_up, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()