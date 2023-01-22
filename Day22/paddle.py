from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__('square')
        self.pu()
        self.color('white')
        self.shapesize(5, 1)
        self.speed(0)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        