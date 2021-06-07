from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, " normal")


class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scorebord()

    def update_scorebord(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increse_score(self):
        self.score += 1
        self.clear()
        self.update_scorebord()
