from turtle import Turtle

FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 0
        self.pu()
        self.goto(-235, 265)
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align="Center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align='center', font=FONT)